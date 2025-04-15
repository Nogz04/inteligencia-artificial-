import random

class Util:

    numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    size = len(numero)

    @staticmethod
    def gerar_Cidade(size):
        cidade = ''
        for i in range(size):
            cidade += str(Util.numero[random.randrange(Util.size)])

        return cidade
