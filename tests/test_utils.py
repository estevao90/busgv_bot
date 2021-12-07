"""
Testes de utilitários
"""
import pytest
from freezegun import freeze_time
from tests.base import Base
from app.utils import is_feriado


class TestUtils(Base):

    @staticmethod
    @pytest.mark.parametrize('data,feriado', [('01/01', True),
                                              ('25/02', True),
                                              ('23/03', False),
                                              ('11/06', True),
                                              ('23/12', False),
                                              ('25/12', True)])
    def test_is_feriado(data, feriado):
        with freeze_time("2020-01-01"):
            assert is_feriado(data) == feriado
