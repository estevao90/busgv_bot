"""
Testes do proxy da API do gvbus
"""
from unittest import mock
from tests.base import Base
from tests.dados_teste import DadosTeste
from app.gvbus_proxy import GvbusProxy
from app.contexto import Contexto


class TestGvbusProxy(Base):

    @staticmethod
    @mock.patch('app.gvbus_proxy.GvbusProxy._GvbusProxy__set_horarios_api',
                return_value=False)
    def test_erro_na_api(_):
        dados_teste = DadosTeste()
        gvbusproxy = GvbusProxy(dados_teste.get_random_linha_gvbus())

        resultado = gvbusproxy.obter_horario_contexto(Contexto())

        assert resultado == 'Erro ao consultar horário na API da CETURB/ES.'

    @staticmethod
    def test_linha_inexistente():
        dados_teste = DadosTeste()
        gvbusproxy = GvbusProxy(dados_teste.get_random_linha_inexistente())

        resultado = gvbusproxy.obter_horario_contexto(Contexto())

        assert resultado == 'Linha não encontrada. Verifique o número no site da CETURB/ES.'

    @staticmethod
    def test_linha_contexto():
        dados_teste = DadosTeste()
        gvbusproxy = GvbusProxy(dados_teste.get_random_linha_gvbus())

        resultado = gvbusproxy.obter_horario_contexto(Contexto())
        print(resultado)

        assert False
