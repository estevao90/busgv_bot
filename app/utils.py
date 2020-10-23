"""
Funções úteis
"""
from datetime import datetime, date
from pytz import timezone
from workalendar.america.brazil import BrazilVitoriaCity


class BrazilGrandeVitoria(BrazilVitoriaCity):
    include_servidor_publico = False
    include_fat_tuesday = True
    fat_tuesday_label = "Carnaval"


__CAL = BrazilGrandeVitoria()


def get_str_data_formatada(formato):
    fuso = timezone('America/Sao_Paulo')
    return datetime.now().astimezone(fuso).strftime(formato)


def is_feriado(data):
    """
    data no formato dd/mm
    """
    dia, mes = map(int, data.split('/'))
    data_ano = date.today().replace(day=dia, month=mes)
    return not __CAL.is_working_day(data_ano)
