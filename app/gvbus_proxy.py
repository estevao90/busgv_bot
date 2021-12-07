"""
Realiza a interação entre o bot e a API da CETURB/ES
"""
import requests


class GvbusProxy():
    __GVBUS_URL = 'https://sistemas.es.gov.br/webservices/ceturb/onibus/api'

    def __init__(self, linha):
        self.linha = int(linha)
        self.__horarios = None

    def __set_horarios_api(self):
        if self.__horarios is None:
            try:
                url_horarios = f'{GvbusProxy.__GVBUS_URL}/buscahorarios/{self.linha}'
                res_horarios = requests.get(url_horarios, timeout=2)
                url_observacoes = f'{GvbusProxy.__GVBUS_URL}/BuscaHorarioObse/{self.linha}'
                res_observacoes = requests.get(url_observacoes, timeout=2)

                if res_horarios.status_code == 200 and res_observacoes.status_code == 200:
                    self.__horarios = Horarios(
                        res_horarios.json(), res_observacoes.json(), self.linha)
                    return True
                return False
            except requests.exceptions.RequestException:
                return False
        return True

    def obter_horario_contexto(self, contexto):
        status = self.__set_horarios_api()
        if not status:
            return 'Erro ao consultar horário na API da CETURB/ES.'

        if self.__horarios.is_inexistente():
            return '''
            Linha não encontrada. Verifique o número correto no site da [CETURB/ES](https://ceturb.es.gov.br).
            '''

        return self.__horarios.get_str_horario_contexto(contexto)


class Horarios():
    @staticmethod
    def get_desc_dia_contexto(str_dia, is_contexto, lista_horarios, contexto):
        return '{dest}\U0001F550 {str}: {hrs}{dest}'.format(
            dest=('*' if is_contexto else ''), str=str_dia,
            hrs=contexto.get_proximos_horarios(lista_horarios))

    def __init__(self, horarios, observacoes, linha):
        self.linha = linha
        self.__desc_linha = None

        self.__desc_terminal_ida = None
        self.__desc_terminal_volta = None

        self.__horarios_dia_util_ida = []
        self.__horarios_sabado_ida = []
        self.__horarios_domingo_ida = []

        self.__horarios_dia_util_volta = []
        self.__horarios_sabado_volta = []
        self.__horarios_domingo_volta = []

        self.__observacoes = {}

        for item in horarios:
            if not self.__desc_linha:
                self.__desc_linha = item.get('Descricao_Linha')

            if item.get('Terminal_Seq') == 1:  # Ida
                if not self.__desc_terminal_ida:
                    self.__desc_terminal_ida = item.get('Desc_Terminal')
                self.preencher_horarios(item)

            elif item.get('Terminal_Seq') == 2:  # Volta
                if not self.__desc_terminal_volta:
                    self.__desc_terminal_volta = item.get('Desc_Terminal')
                self.preencher_horarios(item, False)

        for item in observacoes:
            self.__observacoes[item.get('Tipo_Orientacao')] = item.get(
                'Descricao_Orientacao')

    def preencher_horarios(self, item, ida=True):
        hora = HoraPartida(item.get('Hora_Saida'), item.get('Tipo_Orientacao'))
        if item.get('TP_Horario') == 1:  # dias úteis
            if ida:
                self.__horarios_dia_util_ida.append(hora)
            else:
                self.__horarios_dia_util_volta.append(hora)
        elif item.get('TP_Horario') == 2:  # sábado
            if ida:
                self.__horarios_sabado_ida.append(hora)
            else:
                self.__horarios_sabado_volta.append(hora)
        elif item.get('TP_Horario') == 3:  # domingo
            if ida:
                self.__horarios_domingo_ida.append(hora)
            else:
                self.__horarios_domingo_volta.append(hora)

    def get_descricao_linha(self):
        if self.is_inexistente():
            return f'{self.linha} - Inexistente'
        return f'{self.linha} - {self.__desc_linha}'

    def is_inexistente(self):
        return self.__desc_linha is None

    def is_circular(self):
        return self.__desc_terminal_volta is None

    def get_str_horario_contexto(self, contexto):
        str_horarios = f'''
        *\U0001F68C {self.get_descricao_linha()}*
        \U0001F4CD {self.__desc_terminal_ida}
        {Horarios.get_desc_dia_contexto(
                       'Dia útil', contexto.is_dia_util(), self.__horarios_dia_util_ida, contexto)}
        {Horarios.get_desc_dia_contexto(
                       'Sábado', contexto.is_sabado(), self.__horarios_sabado_ida, contexto)}
        {Horarios.get_desc_dia_contexto(
                       'Dom/Feriado', contexto.is_domingo(), self.__horarios_domingo_ida, contexto)}
        '''

        if not self.is_circular():
            str_horarios += f'''
        \U0001F4CD {self.__desc_terminal_volta}
        {Horarios.get_desc_dia_contexto(
                       'Dia útil', contexto.is_dia_util(), self.__horarios_dia_util_volta,
                       contexto)}
        {Horarios.get_desc_dia_contexto(
                       'Sábado', contexto.is_sabado(), self.__horarios_sabado_volta,
                       contexto)}
        {Horarios.get_desc_dia_contexto(
                       'Dom/Feriado', contexto.is_domingo(), self.__horarios_domingo_volta,
                       contexto)}
        '''

        if contexto.orientacoes.intersection(self.__observacoes):
            str_horarios += '''
        \U00002757 OBSERVAÇÃO
        '''
            for item in sorted(contexto.orientacoes.intersection(self.__observacoes)):
                str_horarios += f'''{item}: {self.__observacoes[item]}
        '''

        return str_horarios

    def __str__(self):
        return f'''
            linha: {self.get_descricao_linha()}
            ida: {self.__desc_terminal_ida}
            UTS: {len(self.__horarios_dia_util_ida)}\tSAB: {len(self.__horarios_sabado_ida)}\tDOM: {len(self.__horarios_domingo_ida)}
            volta: {self.__desc_terminal_volta}
            UTS: {len(self.__horarios_dia_util_volta)}\tSAB: {len(self.__horarios_sabado_volta)}\tDOM: {len(self.__horarios_domingo_volta)}
            '''


class HoraPartida():
    def __init__(self, hora, orientacao):
        self.hora = hora
        self.orientacao = orientacao.strip()
