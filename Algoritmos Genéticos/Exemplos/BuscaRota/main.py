from Cidade import Cidade

def main():
    # Variáveis
    num_cidades = 9
    tamanho_populacao = 50
    quantidade_geracoes = int(input('Quantidade de gerações: '))
    taxa_selecao = 30

    # Inicializa a população
    populacao = Cidade.gerar_populacao(tamanho_populacao, num_cidades)
    historico_aptidao = []
    estagnacao_prolongada = 0

    # Ordena a geração por aptidão
    populacao.sort(key=lambda cidade: cidade.aptidao)
    Cidade.exibir_populacao(populacao, 0)
    historico_aptidao.append(populacao[0].aptidao)

    # Armazena as populações
    for i in range(1, quantidade_geracoes + 1):
        nova_populacao = []
        
        # Coloca os melhores para a próxima geração
        elite_size = max(1, tamanho_populacao // 10)
        nova_populacao.extend(populacao[:elite_size])
        
        #Seleciona os melhores por torneio
        selecionados = Cidade.selecionar_por_torneio(
            populacao, 
            int(tamanho_populacao * taxa_selecao / 100) - elite_size
        )
        nova_populacao.extend(selecionados)
        
        # Reprodução
        filhos = Cidade.reproduzir(
            populacao,
            tamanho_populacao - len(nova_populacao),
            num_cidades
        )
        nova_populacao.extend(filhos)
        
        # Mutação
        populacao = Cidade.aplicar_mutacao(
            nova_populacao,
            elite_size,
            10,
            estagnacao_prolongada
        )
        
        # Atualiza a lista 
        populacao.sort(key=lambda cidade: cidade.aptidao)
        melhor_atual = populacao[0].aptidao
        historico_aptidao.append(melhor_atual)
        
        # Verifica a estagnação
        populacao, estagnacao_prolongada = Cidade.lidar_com_estagnacao(
            populacao,
            tamanho_populacao,
            num_cidades,
            historico_aptidao
        )
        
        # Exibição
        Cidade.exibir_populacao(populacao, i)
        
        if populacao[0].aptidao == 0:
            print("\nSolução ótima encontrada!")
            print("Estado final descoberto:")
            print(populacao[0])
            break

if __name__ == "__main__":
    main()
