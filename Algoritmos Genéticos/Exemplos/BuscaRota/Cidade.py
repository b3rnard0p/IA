import random

class Cidade:
    def __init__(self, rota):  
        self.rota = rota
        self.aptidao = self.calcular_aptidao()

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, num_cidades):
        for _ in range(tamanho_populacao):
            rota_gerada = random.sample(range(1, num_cidades+1), num_cidades)
            individuo = Cidade(rota_gerada)
            populacao.append(individuo)

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
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        torneio = []
        qtd_selecionados = taxa_selecao * len(populacao) // 100
        
        melhor = min(populacao, key=lambda x: x.aptidao)
        nova_populacao.append(melhor)
        
        i = 1
        while i <= qtd_selecionados:
            c1 = populacao[random.randrange(len(populacao))]
            
            while True:            
                c2 = populacao[random.randrange(len(populacao))]
                if c2 != c1:
                    break
            
            while True:            
                c3 = populacao[random.randrange(len(populacao))]
                if c3 != c2 and c3 != c1:
                    break            

            torneio.append(c1)
            torneio.append(c2)
            torneio.append(c3)
            torneio.sort(key=lambda x: x.aptidao) 

            selecionado = torneio[0]

            if selecionado not in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1
            
            torneio.clear()     
                

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, num_cidades):
        qtd_reproduzidos = taxa_reproducao * len(populacao) // 100

        i = 0
        while i < qtd_reproduzidos:            
            pai = populacao[random.randrange(len(populacao))]
                
            while True:            
                mae = populacao[random.randrange(len(populacao))]
                if mae != pai:
                    break               

            ponto1 = random.randint(0, num_cidades - 2)
            ponto2 = random.randint(ponto1 + 1, num_cidades - 1)
            
            def crossover(p1, p2):
                filho = [-1] * num_cidades
                filho[ponto1:ponto2+1] = p1[ponto1:ponto2+1]
                
                current_pos = (ponto2 + 1) % num_cidades
                for gene in p2[ponto2+1:] + p2[:ponto2+1]:
                    if gene not in filho:
                        filho[current_pos] = gene
                        current_pos = (current_pos + 1) % num_cidades
                
                return filho
            
            filho1 = crossover(pai.rota, mae.rota)
            filho2 = crossover(mae.rota, pai.rota)
            
            nova_populacao.append(Cidade(filho1))
            nova_populacao.append(Cidade(filho2))
            i = i + 2
                 
        while len(nova_populacao) > len(populacao):
            nova_populacao.pop()
    
    @staticmethod
    def mutar(populacao):
        populacao.sort(key=lambda x: x.aptidao, reverse=True)
    
        qtd_mutantes = max(1, len(populacao) // 3)
    
        for i in range(qtd_mutantes):
            mutante = populacao[i]
            if len(mutante.rota) >= 2:
                idx1, idx2 = random.sample(range(len(mutante.rota)), 2)
                nova_rota = mutante.rota.copy()
                nova_rota[idx1], nova_rota[idx2] = nova_rota[idx2], nova_rota[idx1]
                populacao[i] = Cidade(nova_rota)
    
        populacao.sort(key=lambda x: x.aptidao)