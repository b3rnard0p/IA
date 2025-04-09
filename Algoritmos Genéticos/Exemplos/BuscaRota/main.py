from Cidade import Cidade

estado_final = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tamanho_populacao = 10
quantidade_geracoes = int(input('Quantidade de gerações: '))
taxa_selecao = int(input('Taxa de seleção [25 a 40]: '))
taxa_reproducao = 100 - taxa_selecao
taxa_mutacao = int(input('Taxa de mutação (gerações entre mutações): '))

populacao = []
nova_populacao = []

Cidade.gerar_populacao(populacao, tamanho_populacao, estado_final)
populacao.sort(key=lambda cidade: cidade.aptidao)
Cidade.exibir_populacao(populacao, 0)

for i in range(1, quantidade_geracoes + 1):
    nova_populacao.clear()
    
    Cidade.selecionar_por_torneio(populacao, nova_populacao, taxa_selecao)
    Cidade.reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final)
    
    if i % taxa_mutacao == 0:
        Cidade.mutar(nova_populacao, estado_final)
    
    populacao.clear()
    populacao.extend(nova_populacao)
    
    populacao.sort(key=lambda cidade: cidade.aptidao)
    
    Cidade.exibir_populacao(populacao, i)
    
    if populacao[0].aptidao == 0:
        print("\nSolução ótima encontrada!")
        break