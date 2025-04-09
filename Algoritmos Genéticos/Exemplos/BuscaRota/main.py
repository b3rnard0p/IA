from Cidade import Cidade

def main():
    num_cidades = 9
    tamanho_populacao = 50
    quantidade_geracoes = int(input('Quantidade de gerações: '))
    taxa_selecao = 30
    taxa_reproducao = 70

    populacao = Cidade.gerar_populacao(tamanho_populacao, num_cidades)
    historico_aptidao = []
    estagnacao_prolongada = 0

    populacao.sort(key=lambda cidade: cidade.aptidao)
    Cidade.exibir_populacao(populacao, 0)
    historico_aptidao.append(populacao[0].aptidao)

    for i in range(1, quantidade_geracoes + 1):
        nova_populacao = []
        
        elite_size = max(1, tamanho_populacao // 10)
        nova_populacao.extend(populacao[:elite_size])
        
        selecionados = Cidade.selecionar_por_torneio(
            populacao, 
            int(tamanho_populacao * taxa_selecao / 100) - elite_size
        )
        nova_populacao.extend(selecionados)
        
        filhos = Cidade.reproduzir(
            populacao,
            tamanho_populacao - len(nova_populacao),
            num_cidades
        )
        nova_populacao.extend(filhos)
        
        populacao = Cidade.aplicar_mutacao(
            nova_populacao,
            elite_size,
            10,
            estagnacao_prolongada
        )
        
        populacao.sort(key=lambda cidade: cidade.aptidao)
        melhor_atual = populacao[0].aptidao
        historico_aptidao.append(melhor_atual)
        
        populacao, estagnacao_prolongada = Cidade.lidar_com_estagnacao(
            populacao,
            tamanho_populacao,
            num_cidades,
            historico_aptidao
        )
        
        Cidade.exibir_populacao(populacao, i)
        
        if populacao[0].aptidao == 0:
            print("\nSolução ótima encontrada!")
            print("Estado final descoberto:")
            print(populacao[0])
            break

        if estagnacao_prolongada >= 10:
            populacao = Cidade.reiniciar_populacao_por_estagnacao(
                populacao,
                tamanho_populacao,
                num_cidades
            )
            estagnacao_prolongada = 0

if __name__ == "__main__":
    main()
