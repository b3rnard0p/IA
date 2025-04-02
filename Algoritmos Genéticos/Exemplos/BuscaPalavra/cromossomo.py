from util import Util
import random

class Cromossomo:
    def __init__(self, palavra, estado_final):  
        self.palavra = palavra
        self.aptidao = self.calcular_aptidao(estado_final)

    @staticmethod
    def gerar_populacao(populacao, tamanho_populacao, estado_final):
        for _ in range(tamanho_populacao):
            palavra_gerada = Util.gerar_palavra(len(estado_final))
            individuo = Cromossomo(palavra_gerada, estado_final)
            populacao.append(individuo)

    def calcular_aptidao(self, estado_final):
        nota = 0
        for i in range(len(estado_final)):
            if (estado_final[i] in self.palavra):
               nota += 5
               
            if (i < len(self.palavra) and (self.palavra[i] == estado_final[i])):
                nota += 50
            
        return nota
    
    def __str__(self):
        return f'{self.palavra} - {self.aptidao}'

    @staticmethod
    def exibir_populacao(populacao, numero_geracao):
        print(f'\nGeração {numero_geracao}:')
        for individuo in populacao:
            print(individuo)

    @staticmethod
    def selecionar_por_torneio(populacao, nova_populacao, taxa_selecao):
        torneio = []
        qtd_selecionados = taxa_selecao * len(populacao) // 100
        cromossomo = populacao[0]        
        nova_populacao.append(cromossomo) 
        
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
            torneio.sort(key=lambda x: x.aptidao, reverse=True) 

            selecionado = torneio[0]

            if selecionado not in nova_populacao:
                nova_populacao.append(selecionado)
                i += 1
            
            torneio.clear()     
                

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        sPai = sMae = sFilho1 = sFilho2 = ''
             
        qtd_reproduzidos = taxa_reproducao * len(populacao) // 100

        i = 0
        while i < qtd_reproduzidos:            
            pai = populacao[random.randrange(len(populacao))]
                
            while True:            
                mae = populacao[random.randrange(len(populacao))]
                if mae != pai:
                    break               

            sPai = pai.palavra
            sMae = mae.palavra
            
            sFilho1 = sPai[0 : len(sPai)//2] + sMae[len(sMae)//2 : len(sMae)]
            sFilho2 = sMae[0 : len(sMae)//2] + sPai[len(sPai)//2 : len(sPai)]

            nova_populacao.append(Cromossomo(sFilho1, estado_final))
            nova_populacao.append(Cromossomo(sFilho2, estado_final))
            i = i + 2
                 
        while len(nova_populacao) > len(populacao):
            nova_populacao.pop()
      
    
    @staticmethod
    def mutar(populacao, estado_final):
        qtd_mutantes = random.randrange(len(populacao) // 5)        
        
        while qtd_mutantes > 0:
            posicao_mutante = random.randrange(len(populacao))
            mutante = populacao[posicao_mutante]
            print("vai mutar ", mutante)
            
            valor_mutado = mutante.palavra

            caracter_mutante = mutante.palavra[random.randrange(len(mutante.palavra))]
            caracter_sorteado = Util.letras[random.randrange(Util.tamanho)]
            valor_mutado = valor_mutado.replace(caracter_mutante, caracter_sorteado, 1)          
            mutante = Cromossomo(valor_mutado, estado_final)
            
            populacao[posicao_mutante] = mutante
            qtd_mutantes -= 1
