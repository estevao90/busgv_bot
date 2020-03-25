"""
Realiza a interação entre o bot e a API da CETURB/ES
"""
import requests


class GvbusProxy:
    __GVBUS_URL = 'https://sistemas.es.gov.br/webservices/ceturb/onibus/api'

    def __init__(self, linha):
        self.linha = int(linha)
        self.__horarios = None

    def __set_horarios_api(self):
        if self.__horarios is None:
            try:
                url = '{}/{}/{}'.format(self.__GVBUS_URL,
                                        'buscahorarios', self.linha)
                res = requests.get(url, timeout=2)

                if res.status_code == 200:
                    self.__horarios = Horarios(res.json())
                    return True
                return False
            except requests.exceptions.RequestException:
                return False

    def obter_horario_contexto(self):
        status = self.__set_horarios_api()
        if not status:
            return 'Erro ao consultar horário na API da CETURB/ES.'

        # ajustando ao contexto
        return 'Em implementação'


class Horarios:
    def __init__(self, json_api):
        for item in json_api:
            pass
            # print(item)
