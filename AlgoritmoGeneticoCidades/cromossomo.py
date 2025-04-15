import random
from Util import Util

class Cromossomo:

    def __init__(self, cidade, estado_final):
        self.cidade = cidade
        self.aptidao = self.calcular_aptidao(estado_final)

    #representa a heurísitica dinamica da solução
    def calcular_aptidao(self, estado_final):
        penalidade = 0

        # Penalidade por ordem incorreta
        for i in range(len(estado_final) - 1):
            if self.cidade[i] > self.cidade[i+1]:
                penalidade += 10

        # Contagem de ocorrencias de cada cidade
        contagem = {}
        for c in self.cidade:
            if c in contagem:
                contagem[c] += 1
            else:
                contagem[c] = 1

        # Penalidade por repeticao
        for qtd in contagem.values():
            if qtd > 1:
                num_pares = (qtd * (qtd - 1)) // 2
                penalidade += num_pares * 20

        return penalidade

    def __str__(self):
        return f'{self.cidade} - {self.aptidao}'

    def __eq__(self, outro):
        if isinstance(outro, Cromossomo):
            return self.cidade == outro.cidade
        return False

    @staticmethod
    def gerar_cidades(cromossomos, quantidade, estado_final):
        for i in range(quantidade):
            nova_cidade = Util.gerar_Cidade(len(estado_final))
            individuo = Cromossomo(nova_cidade, estado_final)
            cromossomos.append(individuo)

    @staticmethod
    def exibir_cidades(cromossomos, geracao):
        print('Geracao...', geracao)
        for individuo in cromossomos:
            print(individuo)

    @staticmethod
    def selecao_torneio(cromossomos, novos_cromossomos, taxa_selecao):
        
        #definir quantos serao selecionados
        qtd_selecionados = int(len(cromossomos) * taxa_selecao / 100)
        torneio = list()

        #elistimo - o mais apto sempre é selecionado
        novos_cromossomos.append(cromossomos[0])

        i = 1
        while i < qtd_selecionados:
            s1 = cromossomos[random.randrange(len(cromossomos))]

            while True:
                s2 = cromossomos[random.randrange(len(cromossomos))]
                if not s1 == s2:
                    break

            while True:
                s3 = cromossomos[random.randrange(len(cromossomos))]
                if not s3 == s1 and not s3 == s2:
                    break

            torneio.extend([s1, s2, s3])
            torneio.sort(key=lambda crom: crom.aptidao)

            if torneio[0] not in novos_cromossomos:
                novos_cromossomos.append(torneio[0])
                i += 1

            torneio.clear()

    @staticmethod
    def reproduzindo(cromossomos, novos_cromossomos, taxa_reproducao, estado_final):
        #definir a quantidade de reproduzidos
        qtd_reproduzidos = int(len(cromossomos) * taxa_reproducao / 100)

        for i in range(int(qtd_reproduzidos / 2) + 1):
            #sorteia um pai entre os primeiros 20% da populacao
            pai = cromossomos[random.randrange(len(cromossomos))]

            while True:
                mae = cromossomos[random.randrange(len(cromossomos))]
                if not pai == mae:
                    break

            cidade_pai = pai.cidade
            cidade_mae = mae.cidade

            metade_pai = cidade_pai[:len(cidade_pai)//2]
            resto_pai = cidade_pai[len(cidade_pai)//2:]

            metade_mae = cidade_mae[:len(cidade_mae)//2]
            resto_mae = cidade_mae[len(cidade_mae)//2:]

            filho1 = metade_pai + resto_mae
            filho2 = metade_mae + resto_pai

            novos_cromossomos.append(Cromossomo(filho1, estado_final))
            novos_cromossomos.append(Cromossomo(filho2, estado_final))

            # Removendo os excessos
            while len(novos_cromossomos) > len(cromossomos):
                novos_cromossomos.pop()

    @staticmethod
    def mutacao(cromossomos, estado_final):
        qtd_mutantes = random.randrange(1, int(len(cromossomos) / 5))

        while qtd_mutantes > 0:
            posicao_mutante = random.randrange(len(cromossomos))
            mutante = cromossomos[posicao_mutante]
            print('\nMutando...', mutante)

            #mutando
            cidade_mutante = mutante.cidade
            caractere_mutante = cidade_mutante[random.randrange(len(cidade_mutante))]
            novo_caractere = Util.numero[random.randrange(Util.size)]

            nova_cidade = cidade_mutante.replace(caractere_mutante, novo_caractere)

            novo_mutante = Cromossomo(nova_cidade, estado_final)
            cromossomos[posicao_mutante] = novo_mutante
            qtd_mutantes -= 1
