"""
Funções úteis
"""
from datetime import datetime
from pytz import timezone

__FERIADOS_FIXOS_ES = ['01/01', '21/04', '01/05',
                       '07/09', '12/10', '02/11', '15/11', '25/12']


def get_str_data_formatada(formato):
    fuso = timezone('America/Sao_Paulo')
    return datetime.now().astimezone(fuso).strftime(formato)


def is_feriado(data):
    """
    data no formato dd/mm
    """
    # Verificar se é uma data fixa
    if data in __FERIADOS_FIXOS_ES:
        return True

    # TODO Feriados variáveis
    # Carnaval, Sexta-feira santa, Páscoa, Nossa senhora da penha e Corpus Christi

    return False
