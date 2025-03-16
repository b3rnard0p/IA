# Métodos de Busca e Otimização em Inteligência Artificial

## Introdução

Os algoritmos de busca e otimização são fundamentais na área de Inteligência Artificial. Eles são utilizados para encontrar soluções em espaços de estados, planejar ações e resolver problemas de decisão. Podem ser classificados em **cegos** (força bruta) ou **heurísticos** (guiados por conhecimento).

---

## 1) Métodos Cegos ou Força Bruta

> **Não utilizam conhecimento prévio do problema ou heurísticas para guiar a busca.**

### 🔵 Busca em Amplitude (Breadth-First Search - BFS)

- Explora o espaço de estados nível a nível.
- Começa pelo estado inicial e expande todos os seus filhos antes de avançar para os netos.
- **Vantagens:**
  - Sempre encontra a solução mais curta (ótima), caso o custo das ações seja uniforme.
  - Completa (garante encontrar solução se existir).
- **Desvantagens:**
  - Alto consumo de memória, já que precisa armazenar muitos nós simultaneamente.
---

### 🔵 Busca em Profundidade (Depth-First Search - DFS)

- Explora o espaço de estados indo o mais fundo possível antes de retroceder (backtracking).
- Segue um caminho até o final antes de tentar outros.
- **Vantagens:**
  - Baixo consumo de memória (precisa armazenar apenas o caminho atual).
  - Simples de implementar.
- **Desvantagens:**
  - Não garante encontrar a solução ótima.
  - Pode entrar em ciclos ou caminhos infinitos se o espaço de estados não for limitado.

---

## 2) Métodos Heurísticos

> **Utilizam uma função de avaliação (heurística) para orientar a busca em direção à solução mais promissora.**

### 🟢 Busca Gulosa (Greedy Search)

- Escolhe o próximo estado baseado apenas no valor da heurística (h(n)) — ou seja, na estimativa de custo até o objetivo.
- Sempre escolhe o nó que "parece" mais próximo do objetivo no momento.
- **Vantagens:**
  - Mais rápida que buscas cegas em muitos casos.
- **Desvantagens:**
  - Pode não encontrar a solução ótima.
  - Pode ficar presa em mínimos locais.

---

### 🟢 Subida de Encosta (Hill Climbing)

- Variante da busca gulosa que se comporta como uma escalada em uma paisagem de soluções.
- Move-se apenas para vizinhos que melhoram a função heurística.
- **Vantagens:**
  - Simples e rápida.
- **Desvantagens:**
  - Suscetível a mínimos locais (pode ficar "presa" em uma solução que não é a melhor globalmente).
  - Pode precisar de técnicas auxiliares como "reinicialização aleatória".

---

### 🟢 A* (A estrela)

- Combina o custo do caminho percorrido até o momento (g(n)) com a estimativa de custo até o objetivo (h(n)):  
  **f(n) = g(n) + h(n)**
- Considerada uma das buscas mais eficientes para encontrar o caminho ótimo.
- **Vantagens:**
  - Completa e ótima (se a heurística for admissível).
  - Bastante usada em problemas de roteamento e jogos.
- **Desvantagens:**
  - Pode consumir muita memória dependendo do espaço de estados.

---

### 🟢 Algoritmos Genéticos (Genetic Algorithms)

- Inspirados no processo de seleção natural.
- População de soluções (indivíduos) evolui ao longo de gerações por meio de operadores como **seleção**, **crossover** (recombinação) e **mutação**.
- **Vantagens:**
  - Útil em problemas com espaços de busca vastos e complexos.
  - Pode escapar de mínimos locais.
- **Desvantagens:**
  - Não garante encontrar a solução ótima.
  - Parâmetros como taxa de mutação e tamanho da população influenciam diretamente o desempenho.

---

### 🟢 Simulated Annealing (Recozimento Simulado)

- Inspirado no processo físico de recozimento de metais.
- Permite aceitar soluções piores com uma certa probabilidade, diminuindo essa chance ao longo do tempo (cooling schedule).
- **Vantagens:**
  - Capaz de escapar de mínimos locais.
  - Pode encontrar soluções próximas da ótima em problemas complexos.
- **Desvantagens:**
  - Parâmetros mal ajustados podem afetar o resultado.
  - Processo pode ser lento dependendo do problema.

---


## ⚙️ Quando usar cada um?

| Método                         | Melhor uso                                                    |
| ------------------------------ | ------------------------------------------------------------- |
| **Busca em Amplitude**          | Quando o objetivo é garantir a solução mais curta e há baixa ramificação. |
| **Busca em Profundidade**       | Quando há limitação de memória ou o espaço de busca é profundo. |
| **Busca Gulosa**                | Quando rapidez é mais importante que a qualidade da solução. |
| **Subida de Encosta**           | Quando há conhecimento prévio sobre o espaço de busca e este tem poucos mínimos locais. |
| **A\***                         | Quando é necessária uma solução ótima em tempo razoável. |
| **Algoritmos Genéticos**        | Problemas de otimização com espaços de busca grandes e complexos. |
| **Simulated Annealing**         | Problemas onde se deseja uma boa solução e minimizar mínimos locais. |
