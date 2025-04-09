from Cidade import Cidade
import random

def main():
    num_cidades = 9
    tamanho_populacao = 50
    quantidade_geracoes = int(input('Quantidade de gerações: '))
    taxa_selecao = 30
    taxa_reproducao = 70

    populacao = []
    historico_aptidao = []
    estagnacao_prolongada = 0

    def gerar_rota_valida(num_cidades):
        return random.sample(range(1, num_cidades+1), num_cidades)

    for _ in range(tamanho_populacao):
        rota = gerar_rota_valida(num_cidades)
        populacao.append(Cidade(rota))

    populacao.sort(key=lambda cidade: cidade.aptidao)
    Cidade.exibir_populacao(populacao, 0)
    historico_aptidao.append(populacao[0].aptidao)

    for i in range(1, quantidade_geracoes + 1):
        nova_populacao = []
        
        elite_size = max(1, tamanho_populacao // 10)
        nova_populacao.extend(populacao[:elite_size])
        
        while len(nova_populacao) < tamanho_populacao * taxa_selecao / 100:
            participantes = random.sample(populacao, 3)
            vencedor = min(participantes, key=lambda x: x.aptidao)
            nova_populacao.append(vencedor)
        
        while len(nova_populacao) < tamanho_populacao:
            pai = random.choice(populacao[:tamanho_populacao//2])
            mae = random.choice(populacao[:tamanho_populacao//2])
            
            size = num_cidades
            start, end = sorted(random.sample(range(size), 2))
            
            filho1 = [-1]*size
            filho2 = [-1]*size
            
            filho1[start:end+1] = pai.rota[start:end+1]
            filho2[start:end+1] = mae.rota[start:end+1]
            
            current_pos_mae = (end + 1) % size
            current_pos_pai = (end + 1) % size
            
            for pos in range(size):
                if filho1[pos] == -1:
                    while mae.rota[current_pos_mae] in filho1:
                        current_pos_mae = (current_pos_mae + 1) % size
                    filho1[pos] = mae.rota[current_pos_mae]
                    current_pos_mae = (current_pos_mae + 1) % size
                    
                if filho2[pos] == -1:
                    while pai.rota[current_pos_pai] in filho2:
                        current_pos_pai = (current_pos_pai + 1) % size
                    filho2[pos] = pai.rota[current_pos_pai]
                    current_pos_pai = (current_pos_pai + 1) % size
            
            nova_populacao.append(Cidade(filho1))
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(Cidade(filho2))
        
        taxa_mutacao_base = 10
        taxa_mutacao = min(50, taxa_mutacao_base + estagnacao_prolongada * 5)
        
        for individuo in nova_populacao[elite_size:]:
            if random.random() < taxa_mutacao / 100:
                if random.random() < 0.7:
                    start, end = sorted(random.sample(range(len(individuo.rota)), 2))
                    individuo.rota[start:end+1] = reversed(individuo.rota[start:end+1])
                else:
                    start, end = sorted(random.sample(range(len(individuo.rota)), 2))
                    sub_rota = individuo.rota[start:end+1]
                    random.shuffle(sub_rota)
                    individuo.rota[start:end+1] = sub_rota
                
                individuo.aptidao = individuo.calcular_aptidao()
        
        populacao = nova_populacao
        populacao.sort(key=lambda cidade: cidade.aptidao)
        
        melhor_atual = populacao[0].aptidao
        historico_aptidao.append(melhor_atual)
        
        if len(historico_aptidao) > 10:
            historico_aptidao.pop(0)
            
            if all(apt == melhor_atual for apt in historico_aptidao[-5:]):
                estagnacao_prolongada += 1
                print(f"\nEstagnação prolongada nível {estagnacao_prolongada}! Aplicando medidas especiais...")
                
                substituicao = max(3, tamanho_populacao // 3)
                for j in range(1, substituicao + 1):
                    populacao[-j] = Cidade(gerar_rota_valida(num_cidades))
                
                for individuo in populacao[tamanho_populacao//4:-substituicao]:
                    start, end = sorted(random.sample(range(len(individuo.rota)), 2))
                    individuo.rota[start:end+1] = reversed(individuo.rota[start:end+1])
                    individuo.aptidao = individuo.calcular_aptidao()
            else:
                estagnacao_prolongada = max(0, estagnacao_prolongada - 1)
        
        Cidade.exibir_populacao(populacao, i)
        
        if populacao[0].aptidao == 0:
            print("\nSolução ótima encontrada!")
            print("Estado final descoberto:")
            print(populacao[0])
            break

        if estagnacao_prolongada >= 10:
            print("\nEstagnação crítica! Reiniciando população...")
            melhor = populacao[0]
            populacao = [melhor]
            for _ in range(tamanho_populacao - 1):
                rota = gerar_rota_valida(num_cidades)
                populacao.append(Cidade(rota))
            estagnacao_prolongada = 0

if __name__ == "__main__":
    main()