"""
Testes de utilitários
"""
import pytest
from tests.base import Base
from app.utils import is_feriado


class TestUtils(Base):

    @staticmethod
    @pytest.mark.parametrize('data,feriado', [('01/01', True),
                                              ('23/03', False),
                                              ('25/12', True),
                                              ('27/12', False)])
    def test_is_feriado(data, feriado):
        assert is_feriado(data) == feriado
