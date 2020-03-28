"""
Testes da obtenção do contexto
"""
from tests.base import Base
from app.contexto import Contexto


class TestContexto(Base):

    @staticmethod
    def test_obter_contexto_atual():
        contexto = Contexto()
        assert contexto.is_valido()
