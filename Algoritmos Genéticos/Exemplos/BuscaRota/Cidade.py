import random

class Cidade:
    def __init__(self, rota, estado_final):  
        self.rota = rota
        self.aptidao = self.calcular_aptidao(estado_final)

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for _ in range(tamanho_populacao):
            rota_gerada = random.choices(estado_final, k=len(estado_final))
            individuo = Cidade(rota_gerada, estado_final)
            populacao.append(individuo)

    def calcular_aptidao(self, estado_final):
        nota = 0
        
        # Penalidade por posição incorreta
        for i in range(len(self.rota)):
            if i < len(estado_final):
                if self.rota[i] != estado_final[i]:
                    nota += 10
        
        # Verificar restrição de cidades menores conectadas a maiores
        for i in range(len(self.rota) - 1):
            cidade_atual = self.rota[i]
            cidade_proxima = self.rota[i+1]
            
            
            if cidade_atual > cidade_proxima:
                nota += 30 
        
        # Penalidade por cidades repetidas (se houver)
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
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        qtd_reproduzidos = taxa_reproducao * len(populacao) // 100

        i = 0
        while i < qtd_reproduzidos:            
            pai = populacao[random.randrange(len(populacao))]
                
            while True:            
                mae = populacao[random.randrange(len(populacao))]
                if mae != pai:
                    break               

            ponto1 = random.randint(0, len(estado_final) - 2)
            ponto2 = random.randint(ponto1 + 1, len(estado_final) - 1)
            
            filho1 = pai.rota[:ponto1] + mae.rota[ponto1:ponto2] + pai.rota[ponto2:]
            filho2 = mae.rota[:ponto1] + pai.rota[ponto1:ponto2] + mae.rota[ponto2:]
            
            
            nova_populacao.append(Cidade(filho1, estado_final))
            nova_populacao.append(Cidade(filho2, estado_final))
            i = i + 2
                 
        while len(nova_populacao) > len(populacao):
            nova_populacao.pop()
    
    @staticmethod
    def mutar(populacao, estado_final):
        qtd_mutantes = random.randrange(len(populacao) // 5)        
        
        while qtd_mutantes > 0:
            posicao_mutante = random.randrange(len(populacao))
            mutante = populacao[posicao_mutante]
            
            if len(mutante.rota) >= 2:
                idx1, idx2 = random.sample(range(len(mutante.rota)), 2)
                nova_rota = mutante.rota.copy()
                nova_rota[idx1], nova_rota[idx2] = nova_rota[idx2], nova_rota[idx1]
                
                populacao[posicao_mutante] = Cidade(nova_rota, estado_final)
            
            qtd_mutantes -= 1