# Introdução à Inteligência Artificial (IA)

## 1) Que tipo de problema a IA resolve?

- Problemas que exigem a presença de um especialista devido à complexidade ou quantidade de restrições.
- Problemas em que o estado final é desconhecido ou em que é necessário descobrir o **passo a passo** da solução.
- Problemas com grande volume de dados ou variáveis a serem analisadas simultaneamente.
- Problemas que envolvem incerteza, ambiguidade ou ambientes dinâmicos.

---

## 2) O que é Inteligência Artificial?

Área da Computação dedicada ao desenvolvimento de metodologias, técnicas e algoritmos que permitem a criação de sistemas capazes de simular comportamentos inteligentes ou resolver problemas que normalmente requereriam inteligência humana.

A IA busca automatizar tarefas cognitivas como:
- Raciocínio
- Tomada de decisão
- Percepção
- Aprendizado
- Adaptação

---

## 3) Principais subáreas da Inteligência Artificial

### Métodos de busca e otimização:
- **Cegos ou força bruta** (não utilizam conhecimento prévio):
  - Busca em Amplitude
  - Busca em Profundidade

- **Heurísticos** (usam função de avaliação para orientar a busca):
  - Busca Gulosa
  - Subida de Encosta (Hill Climbing)
  - A* (A estrela)
  - Algoritmos Genéticos
  - Simulated Annealing (Recozimento Simulado)

### Redes Neurais Artificiais (RNA)

  - Inspiradas no funcionamento do cérebro humano para reconhecimento de padrões, classificação e predição.
  
### Sistemas Multiagentes

  - Conjunto de agentes autônomos que interagem em um ambiente para alcançar objetivos individuais ou coletivos.

### Representação de Conhecimento e Raciocínio

  - Como representar o conhecimento sobre o mundo (fatos, regras, ontologias) e raciocinar sobre ele (dedução e inferência).

### Processamento de Linguagem Natural (PLN)

  - Capacitar sistemas a entender, interpretar e gerar linguagem humana de forma eficiente.
  
### Aprendizado de Máquina (Machine Learning)

  - Subárea focada em desenvolver algoritmos que permitam aos sistemas aprender a partir de dados.
---

## 4) O que é um sistema de comportamento inteligente?

Um sistema que atua de forma autônoma e adaptativa em ambientes complexos, composto por:

- **Base de conhecimento:** fatos, regras, crenças ou planos.
- **Raciocínio automatizado:** dedução e indução.
- **Aprendizado de Máquina:** aprendizado com base em dados e repetição.

---

## 5) Que tipo de problema as Redes Neurais Artificiais (RNA) resolvem?

- Problemas de **reconhecimento de padrões** em dados complexos ou não estruturados.
- Problemas em que o conhecimento de especialistas é difícil de transformar em regras explícitas.

Exemplos:
- Reconhecimento de voz e imagem
- Diagnósticos médicos
- Análise de padrões financeiros

---

## 6) Características de problemas de alta complexidade

- **Muitas restrições**
- **Grande espaço de estados**
- **Incerteza e ambiguidade**
- **Desconhecimento do estado final**
- **Ambientes dinâmicos**

---

## 7) Processo de modelagem de problemas em IA

### O que deve ser modelado:

- **Estados**:
  - Estado(s) inicial(is) e final(ais)
  - Cada estado representa uma configuração dos atributos em um ponto do processo.

- **Atributos**:
  - Variáveis que caracterizam o estado (ex.: posição, valores, condições).

- **Regras de transição**:
  - Métodos ou ações que permitem a mudança de um estado para outro.

- **Restrições**:
  - Limitações que definem quais transições ou estados são válidos.

- **Lista de visitados**:
  - Registro dos estados já explorados para evitar ciclos ou redundâncias.

- **Função meta ou objetivo**:
  - Função de avaliação que verifica se o estado final foi alcançado ou mede a proximidade da solução ideal.
