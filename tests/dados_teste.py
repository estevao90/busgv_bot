"""
Classe de apoio e geração de dados para os testes
"""
import random
from faker import Faker


class DadosTeste():
    __LINHAS_SELETIVOS = [1801, 1802, 1804, 1805, 1806, 1808]

    def __init__(self):
        self.__faker = Faker()

    def get_random_linha_gvbus(self):
        regiao = random.randrange(500, 1000, 100)
        if regiao == 1000:
            return random.choice(DadosTeste.__LINHAS_SELETIVOS)
        return random.randrange(regiao + 3, regiao + 10)
