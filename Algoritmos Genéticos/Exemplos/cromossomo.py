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
               
            if (i < len(self.palavra) and self.palavra[i] == estado_final[i]):
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
    def selecionar(populacao, nova_populacao, taxa_selecao):
        qtd_selecionados = int(len(populacao) * taxa_selecao / 100)
        nova_populacao.extend(populacao[:qtd_selecionados])

    @staticmethod
    def reproduzir(populacao, nova_populacao, taxa_reproducao, estado_final):
        qtd_necessaria = len(populacao) - len(nova_populacao)
        for _ in range(qtd_necessaria):
            pai1 = random.choice(populacao[:len(populacao)//2])
            pai2 = random.choice(populacao[:len(populacao)//2])
            
            ponto_corte = random.randint(1, len(estado_final)-1)
            filho_palavra = pai1.palavra[:ponto_corte] + pai2.palavra[ponto_corte:]
            
            nova_populacao.append(Cromossomo(filho_palavra, estado_final))
    
    @staticmethod
    def mutar(nova_populacao, estado_final):
        for individuo in nova_populacao:
            if random.random() < 0.1:  
                idx = random.randint(0, len(estado_final)-1)
                letra = Util.letras[random.randrange(Util.tamanho)]
                palavra_lista = list(individuo.palavra)
                palavra_lista[idx] = letra
                individuo.palavra = ''.join(palavra_lista)
                individuo.aptidao = individuo.calcular_aptidao(estado_final)