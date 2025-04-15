import random
from cromosso import Cromossomo

class Main:
    
        estado_final = '123456789'

        quantidade_cromossomos = int(input('Quantidade de cromossomos: '))
        quantidade_geracoes = int(input('Quantidade de gerações: '))
        taxa_selecao = int(input('Taxa de seleção [25 a 75]: '))
        taxa_mutacao = int(input('Taxa de mutação: '))
        taxa_reproducao = 100 - taxa_selecao

        frequencia_mutacao = 100 - (quantidade_cromossomos * taxa_mutacao / 100)

        populacao = list()
        nova_populacao = list()

        historico_melhores = dict()  # Armazena o melhor de cada geração

        #estados totalmente aleatorios
        Cromossomo.gerar_cidades(populacao, quantidade_cromossomos, estado_final)
        populacao.sort(key=lambda c: c.aptidao)
        Cromossomo.exibir_cidades(populacao, 0)
        historico_melhores[0] = populacao[0].aptidao  # salva aptidão da geração 0 ou próximo

        for geracao in range(1, quantidade_geracoes):
            Cromossomo.selecao_torneio(populacao, nova_populacao, taxa_selecao)
            Cromossomo.reproduzindo(populacao, nova_populacao, taxa_reproducao, estado_final)

            # Mutação aleatória baseada em taxa
            if random.random() < (taxa_mutacao / 100):
                Cromossomo.mutacao(nova_populacao, estado_final)

            populacao.clear()
            populacao.extend(nova_populacao)
            nova_populacao.clear()
            populacao.sort(key=lambda c: c.aptidao)
            Cromossomo.exibir_cidades(populacao, geracao)
            historico_melhores[geracao] = populacao[0].aptidao  # salva melhor da geração atual

        # Estatística final - melhor geração
        melhor_geracao = min(historico_melhores, key=historico_melhores.get)
        melhor_aptidao = historico_melhores[melhor_geracao]

        print("\n====== ESTATÍSTICA FINAL ======")
        print(f'Aptidão mais próxima ou igual a 0: {melhor_aptidao}')

        
