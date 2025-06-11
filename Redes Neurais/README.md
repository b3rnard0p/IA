
# 🔹 O que são Redes Neurais?

Uma **Rede Neural Artificial (RNA)** é um modelo computacional inspirado no funcionamento do cérebro humano, composto por unidades de processamento chamadas **neurônios artificiais**, interconectados por **sinapses** (pesos). Elas são capazes de aprender padrões complexos de dados por meio de **ajuste iterativo desses pesos**.

---

## 🔹 Ligação com Inteligência Artificial

As Redes Neurais estão no coração de muitas técnicas de **Aprendizado de Máquina** e **Deep Learning**, permitindo que máquinas:

* **Reconheçam padrões** em imagens, áudios e textos.
* **Tomem decisões** e façam previsões com base em dados históricos.
* **Adaptem-se** a novos cenários por meio de treinamento contínuo.

---

## 🔹 O que é um Neurônio Artificial?

Um neurônio artificial é uma **função matemática** que processa entradas e gera uma saída:

* **Entradas (x₁, x₂, …, xₙ)**: valores que chegam de neurônios anteriores.
* **Pesos (w₁, w₂, …, wₙ)**: parâmetros que determinam a influência de cada entrada.
* **Bias (b)**: termo adicional que desloca a função de ativação.
* **Função de Ativação**: aplica-se sobre a soma ponderada, introduzindo não linearidades.

  * Exemplos: **ReLU**, **Sigmoid**, **Tanh**, **Softmax**.

> *Exemplo de cálculo:*
> saída = ativação(Σ (wᵢ · xᵢ) + b)

---

## 🔹 Aplicações de Redes Neurais

Redes Neurais são versáteis e se adaptam a diferentes domínios:

### Exemplos:

* **Visão Computacional**: detecção de objetos, segmentação de imagens, reconhecimento facial.
* **Processamento de Linguagem Natural (PLN)**: tradução automática, análise de sentimentos, chatbots.
* **Sistemas de Recomendação**: sugestão de produtos, filmes e músicas.
* **Jogos e Simulações**: agentes que aprendem a jogar, otimização de estratégias.
* **Finanças**: previsão de preços de ações, detecção de fraudes.

---

## 🔹 Características de Redes Neurais

### ✅ Capacidade de Aprendizado

Aprendem a partir de **dados rotulados** (supervisionado) ou **não rotulados** (não supervisionado).

### ✅ Generalização

Podem fazer previsões sobre **novos dados** nunca vistos durante o treinamento.

### ✅ Tolerância a Ruído

Robustas contra **dados imperfeitos** ou com **faltas de informação**.

### ✅ Escalabilidade

Podem crescer em **profundidade** (mais camadas) e **largura** (mais neurônios por camada) para captar padrões cada vez mais complexos.

---

## 🔹 Principais Arquiteturas de Redes Neurais

### 🧱 Perceptron Multicamadas (MLP)

* **Feedforward**: sinais fluem em uma única direção, da entrada até a saída.
* **Treinamento**: utiliza o algoritmo **Backpropagation** para ajustar pesos.

### 📷 Redes Convolucionais (CNN)

* **Filtros convolucionais** extraem características locais (bordas, texturas).
* **Pooling** reduz dimensionalidade, mantendo informação essencial.
* Muito usadas em **visão computacional**.

### 🔄 Redes Recorrentes (RNN, LSTM, GRU)

* **Laços internos** permitem processar sequências e capturar dependências temporais.
* **LSTM/GRU** resolvem o problema de desvanecimento de gradiente em sequências longas.
* Aplicações em **PLN** e **séries temporais**.

### 🌐 Redes Gerais e Transformers

* **Transformers** baseiam-se em mecanismos de **atenção** para modelar dependências globais nos dados.
* Pilares de grandes modelos de linguagem, como **BERT** e **GPT**.

---

## 🔹 Ciclo de Vida de um Projeto com Redes Neurais

1. **Coleta de Dados**: reunir e rotular exemplos relevantes.
2. **Pré-processamento**: limpeza, normalização e divisão em conjuntos de treino, validação e teste.
3. **Definição da Arquitetura**: escolher tipo de rede, número de camadas e neurônios.
4. **Treinamento**: otimização de pesos, ajustando hiperparâmetros (taxa de aprendizado, batch size).
5. **Avaliação**: medir métricas (acurácia, precisão, recall, F1-score).
6. **Ajustes e Validação**: refinar arquitetura e hiperparâmetros.
7. **Deploy**: disponibilizar o modelo em produção (APIs, dispositivos embarcados).
8. **Monitoramento**: acompanhar desempenho e retrain conforme necessário.

---

## 🔹 Ferramentas e Bibliotecas Populares

* **TensorFlow** e **Keras**
* **PyTorch**
* **scikit-learn** (para MLPs simples)
* **FastAI**
* **Hugging Face Transformers**
