from cromossomo import Cromossomo

estado_final = input('Entre com a palavra do estado final: ')
tamanho_populacao = int(input('Tamanho da população: '))
quantidade_geracoes = int(input('Gerações: '))
taxa_selecao = int(input('Taxa de seleção [25 a 40]: '))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input('Taxa de mutação: '))

populacao = []
nova_populacao = []

# Primeira geração
Cromossomo.gerar_populacao(populacao, tamanho_populacao, estado_final)
populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
Cromossomo.exibir_populacao(populacao, 0)

for i in range(1, quantidade_geracoes + 1):
    nova_populacao.clear()
    
    Cromossomo.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
    Cromossomo.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)
    
    if i % taxa_mutacao == 0:
        Cromossomo.mutar(nova_populacao, estado_final)
    
    populacao.clear()
    populacao.extend(nova_populacao)
    
    populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
    
    Cromossomo.exibir_populacao(populacao, i)
