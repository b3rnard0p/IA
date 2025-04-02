from cromossomo import Cromossomo

estado_final = input('Entre com a palavra do estado final: ')
tamanho_populacao = int(input('Tamanho da população: '))
quantidade_geracoes = int(input('Gerações: '))
taxa_selecao = int(input('Taxa de seleção [25 a 40]: '))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input('Taxa de mutação: '))

populacao = list()
nova_populacao = list()

# Primeira geração
Cromossomo.gerar_populacao(populacao, tamanho_populacao, estado_final)
populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
Cromossomo.exibir_populacao(populacao, 0)

for i in range(1, quantidade_geracoes + 1):
    # Limpa a nova população para a próxima geração
    nova_populacao.clear()
    
    # Seleciona os melhores indivíduos
    Cromossomo.selecionar(populacao, nova_populacao, taxa_selecao)
    
    # Reproduz para completar a população
    Cromossomo.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)
    
    # Aplica mutação se necessário
    if i % taxa_mutacao == 0:
        Cromossomo.mutar(nova_populacao, estado_final)
    
    # Atualiza a população principal
    populacao.clear()
    populacao.extend(nova_populacao)
    
    # Ordena pela aptidão
    populacao.sort(key=lambda cromossomo: cromossomo.aptidao, reverse=True)
    
    # Exibe a população atual
    Cromossomo.exibir_populacao(populacao, i)