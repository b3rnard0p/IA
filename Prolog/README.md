# Prolog - Linguagem de Programação Lógica

Prolog (Programming in Logic) é uma linguagem de programação declarativa baseada na lógica formal. Desenvolvida na década de 1970 por Alain Colmerauer e Philippe Roussel, Prolog é especialmente utilizada em áreas que envolvem inteligência artificial e manipulação de conhecimento, como sistemas especialistas, processamento de linguagem natural e resolução de problemas lógicos.

## Características Principais

- **Linguagem Declarativa**: Em vez de especificar como fazer algo (como nas linguagens imperativas), o programador descreve *o que* deseja alcançar.
- **Baseado em Regras Lógicas**: Prolog utiliza fatos e regras lógicas para inferir novos conhecimentos.
- **Resolução de Consultas**: O Prolog resolve consultas (queries) baseando-se em um conjunto de fatos e regras, utilizando técnicas de inferência lógica como *backtracking*.

## Conceitos Fundamentais

1. **Fatos**: Declarações simples que são verdadeiras no domínio do problema.
2. **Regras**: Definem relacionamentos entre fatos. Uma regra é composta por uma cabeça (conclusão) e um corpo (condição).
3. **Consultas**: Perguntas feitas ao sistema para verificar a veracidade ou obter informações.
4. **Backtracking**: Processo pelo qual o Prolog tenta encontrar uma solução tentando todas as possibilidades de forma sistemática, voltando quando uma solução falha e tentando outra alternativa.

---

## Listas em Prolog

Listas são **estruturas de dados fundamentais** em Prolog. Elas são usadas para armazenar coleções de elementos e são tratadas como objetos de primeira classe.

### 📌 Sintaxe

```
[Elemento1, Elemento2, ..., ElementoN]
```
*Exemplo*: [a, b, c] é uma lista com três elementos.

### 📌 Lista Vazia
```
[]
```
###📌 Cabeça e Cauda

Cada lista é composta de Cabeça (Head) e Cauda (Tail):

```
[Head | Tail]

Exemplo:

[a, b, c] = [X | Y].

Resultado:

X = a

Y = [b, c]
```

###📌 Exemplos de Predicados com Listas

Verificar se um elemento está na lista
```
membro(X, [X | _]).
membro(X, [_ | T]) :- membro(X, T).
Concatenar duas listas
concatena([], L, L).
concatena([H|T], L2, [H|R]) :- concatena(T, L2, R).
Calcular o comprimento de uma lista
comprimento([], 0).
comprimento([_|T], N) :- comprimento(T, N1), N is N1 + 1.
Somar elementos de uma lista
soma([], 0).
soma([H|T], Total) :- soma(T, S), Total is H + S.
```

### Aplicações do Prolog

1. *Inteligência Artificial*: Usado em sistemas especialistas, raciocínio automatizado, e diagnóstico de problemas.

2. *Processamento de Linguagem Natural*: Prolog é eficaz para tarefas como análise sintática e semântica.

3. *Teoria dos Grafos e Resolução de Problemas*: Soluções para problemas de busca e otimização são comuns em Prolog.

4. *Representação de Conhecimento*: Usado para modelar e raciocinar sobre dados e fatos em diversas áreas.

### Vantagens
*: Linguagem compacta e fácil de ler.

*Solução Natural para Problemas Lógicos*: Ideal para tarefas que envolvem relações e regras complexas.

*Backtracking Automático*: Facilita a implementação de soluções que requerem busca exaustiva.

### Desvantagens
*Desempenho*: Prolog pode ser mais lento em algumas aplicações em comparação com linguagens imperativas.

*Curva de Aprendizado*: A programação lógica pode ser difícil de aprender para aqueles acostumados com linguagens imperativas.
