"""
Testes do proxy da API do gvbus
"""
from unittest import mock
from tests.base import Base
from tests.dados_teste import DadosTeste
from app.gvbus_proxy import GvbusProxy


class TestGvbusProxy(Base):

    @mock.patch('app.gvbus_proxy.GvbusProxy.__GVBUS_URL',
                'https://sistemas.es.gov.br/webservices/ceturb/onibus/api/erro')
    def test_erro_na_api(self):
        dados_teste = DadosTeste()
        gvbusproxy = GvbusProxy(dados_teste.get_random_linha_gvbus())

        resultado = gvbusproxy.obter_horario_contexto()

        assert resultado == 'teste'
