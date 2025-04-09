import random

class Cidade:
    def __init__(self, rota):  
        self.rota = rota
        self.aptidao = self.calcular_aptidao()

    @staticmethod
    def gerar_populacao(tamanho_populacao, num_cidades, permitir_repeticao=False):
        populacao = []
        for _ in range(tamanho_populacao):
            if permitir_repeticao:
                rota = [random.randint(1, num_cidades) for _ in range(num_cidades)]
            else:
                rota = random.sample(range(1, num_cidades+1), num_cidades)
            populacao.append(Cidade(rota))
        return populacao

    def calcular_aptidao(self):
        nota = 0
        
        for i in range(len(self.rota) - 1):
            cidade_atual = self.rota[i]
            cidade_proxima = self.rota[i+1]
            
            if cidade_atual > cidade_proxima:
                nota += 30 
        
        if len(self.rota) != len(set(self.rota)):
            nota += 20 * (len(self.rota) - len(set(self.rota)))
            
        return nota
    
    def __str__(self):
        nomes_cidades = {
            1: "Santa Maria",
            2: "Porto Alegre",
            3: "Caçapava Do Sul",
            4: "Jaguari",
            5: "Cruz Alta",
            6: "Capão da Canoa",
            7: "Bagé",
            8: "Alegrete",
            9: "Rio Grande"
        }
        rota_nomes = [nomes_cidades[num] for num in self.rota]
        return f'{rota_nomes} - {self.aptidao}'

    @staticmethod
    def exibir_populacao(populacao, numero_geracao):
        print(f'\nGeração {numero_geracao}:')
        for i, individuo in enumerate(populacao, 1):
            print(f"{i}. {individuo}")

    @staticmethod
    def selecionar_por_torneio(populacao, quantidade):
        selecionados = []
        while len(selecionados) < quantidade:
            participantes = random.sample(populacao, 3)
            vencedor = min(participantes, key=lambda x: x.aptidao)
            selecionados.append(vencedor)
        return selecionados

    @staticmethod
    def reproduzir(populacao, quantidade, num_cidades):
        filhos = []
        for _ in range(quantidade // 2):
            pai, mae = random.sample(populacao[:len(populacao)//2], 2)
            
            start, end = sorted(random.sample(range(num_cidades), 2))
            
            filho1 = [-1]*num_cidades
            filho2 = [-1]*num_cidades
            
            filho1[start:end+1] = pai.rota[start:end+1]
            filho2[start:end+1] = mae.rota[start:end+1]
            
            current_pos_mae = (end + 1) % num_cidades
            current_pos_pai = (end + 1) % num_cidades
            
            for pos in range(num_cidades):
                if filho1[pos] == -1:
                    while mae.rota[current_pos_mae] in filho1:
                        current_pos_mae = (current_pos_mae + 1) % num_cidades
                    filho1[pos] = mae.rota[current_pos_mae]
                    current_pos_mae = (current_pos_mae + 1) % num_cidades
                    
                if filho2[pos] == -1:
                    while pai.rota[current_pos_pai] in filho2:
                        current_pos_pai = (current_pos_pai + 1) % num_cidades
                    filho2[pos] = pai.rota[current_pos_pai]
                    current_pos_pai = (current_pos_pai + 1) % num_cidades
            
            filhos.extend([Cidade(filho1), Cidade(filho2)])
        
        return filhos[:quantidade]

    @staticmethod
    def aplicar_mutacao(populacao, elite_size, taxa_mutacao, estagnacao_prolongada):
        taxa_mutacao_ajustada = min(50, taxa_mutacao + estagnacao_prolongada * 5)
        
        for individuo in populacao[elite_size:]:
            if random.random() < taxa_mutacao_ajustada / 100:
                if random.random() < 0.7:
                    start, end = sorted(random.sample(range(len(individuo.rota)), 2))
                    individuo.rota[start:end+1] = reversed(individuo.rota[start:end+1])
                else:
                    start, end = sorted(random.sample(range(len(individuo.rota)), 2))
                    sub_rota = individuo.rota[start:end+1]
                    random.shuffle(sub_rota)
                    individuo.rota[start:end+1] = sub_rota
                
                individuo.aptidao = individuo.calcular_aptidao()
        return populacao

    @staticmethod
    def lidar_com_estagnacao(populacao, tamanho_populacao, num_cidades, historico_aptidao):
        estagnacao_prolongada = 0
        
        if len(historico_aptidao) > 10:
            historico_aptidao.pop(0)
            
            if all(apt == historico_aptidao[-1] for apt in historico_aptidao[-5:]):
                estagnacao_prolongada += 1
                print(f"\nEstagnação prolongada nível {estagnacao_prolongada}! Aplicando medidas especiais...")
                
                substituicao = max(3, tamanho_populacao // 3)
                for j in range(1, substituicao + 1):
                    populacao[-j] = Cidade(random.sample(range(1, num_cidades+1), num_cidades))
                
                for individuo in populacao[tamanho_populacao//4:-substituicao]:
                    start, end = sorted(random.sample(range(len(individuo.rota)), 2))
                    individuo.rota[start:end+1] = reversed(individuo.rota[start:end+1])
                    individuo.aptidao = individuo.calcular_aptidao()
            else:
                estagnacao_prolongada = max(0, estagnacao_prolongada - 1)
        
        return populacao, estagnacao_prolongada

    @staticmethod
    def reiniciar_populacao_por_estagnacao(populacao, tamanho_populacao, num_cidades):
        print("\nEstagnação crítica! Reiniciando população...")
        melhor = min(populacao, key=lambda x: x.aptidao)
        nova_populacao = [melhor]
        nova_populacao.extend(Cidade.gerar_populacao(tamanho_populacao-1, num_cidades))
        return nova_populacao
