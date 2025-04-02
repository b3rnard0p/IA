# Algoritmos Genéticos e Suas Aplicações

## 🔹 O que são Algoritmos Genéticos?  
Algoritmos Genéticos (AGs) são métodos de otimização e busca inspirados na teoria da evolução de Charles Darwin. Eles pertencem à classe dos **algoritmos evolutivos** e utilizam conceitos como **seleção natural, mutação e recombinação genética** para encontrar soluções aproximadas para problemas complexos.

## 🔹 Como Funcionam os Algoritmos Genéticos?  
1. **Inicialização**: Uma população inicial de soluções (candidatos) é gerada aleatoriamente.  
2. **Avaliação (Função de Aptidão)**: Cada solução recebe uma pontuação baseada em um critério de qualidade.  
3. **Seleção**: As melhores soluções são escolhidas para reprodução, simulando a sobrevivência dos mais aptos.  
4. **Crossover (Recombinação)**: Duas soluções "pais" trocam partes de seus dados para gerar novas soluções "filhas".  
5. **Mutação**: Pequenas alterações aleatórias são aplicadas às soluções para introduzir diversidade.  
6. **Nova Geração**: O processo se repete até que um critério de parada seja atingido (número de gerações ou uma solução satisfatória).

---

## 🔹 Onde Aplicar Algoritmos Genéticos?  
AGs são úteis quando o espaço de busca é **grande e complexo**, onde métodos tradicionais seriam ineficientes. Algumas aplicações incluem:

✔ **Otimização de Processos**  
   - Planejamento logístico (exemplo: roteamento de veículos)  
   - Alocação de recursos em fábricas ou empresas  

✔ **Inteligência Artificial e Machine Learning**  
   - Treinamento de redes neurais artificiais  
   - Ajuste de hiperparâmetros em modelos de aprendizado de máquina  

✔ **Jogos e Entretenimento**  
   - Desenvolvimento de NPCs adaptáveis  
   - Evolução de estratégias em jogos  

✔ **Bioinformática e Genética**  
   - Modelagem de DNA e proteínas  
   - Simulação de evolução e mutação genética  

✔ **Engenharia e Design**  
   - Otimização de estruturas mecânicas e arquitetônicas  
   - Desenvolvimento de circuitos eletrônicos eficientes  

✔ **Finanças e Economia**  
   - Otimização de carteiras de investimentos  
   - Previsão de tendências de mercado  

Em resumo, os Algoritmos Genéticos são uma abordagem poderosa para problemas onde **não há uma solução óbvia e exata**, sendo especialmente úteis para problemas de **otimização e busca heurística**. 🚀

# Exemplo de Modelagem

## 🔹 Atributos

- **estadoFinal/restricoes**: Condições que definem uma solução aceitável ou ótima para o problema.
- **populacao**: Lista de cromossomos (cada cromossomo possui uma palavra ou representação genética e um valor de aptidão).
- **novaPopulacao**: Lista de cromossomos que estão sendo selecionados, reproduzidos ou mutados para a próxima geração.
- **tamanhoPopulacao**: Número total de indivíduos na população.
- **taxaSelecao**: Percentual (geralmente 25% a 40%) dos cromossomos mais aptos selecionados para reprodução.
- **taxaReproducao**: Percentual (100% - taxaSelecao) de novos indivíduos produzidos a partir dos selecionados.
- **taxaMutacao**: Probabilidade de um cromossomo sofrer mutação.
- **qtdGeracoes**: Número máximo de gerações que o algoritmo irá executar.

## 🔹 Fluxo

### Primeira Geração (100% Aleatória)
1. **GerarPopulacao(populacao, tamanhoPopulacao, estadoFinal)**:  
   - Cria uma população inicial de cromossomos aleatórios, respeitando as restrições do problema.
2. **ordenarPopulacao(populacao)**:  
   - Ordena a população com base na aptidão de cada cromossomo (do mais apto ao menos apto).
3. **exibirPopulacao(populacao)**:  
   - Mostra os cromossomos e suas aptidões (opcional para acompanhamento).

### Demais Gerações
Repetir de **1** até **qtdGeracoes**:
1. **selecionar(populacao, novaPopulacao, taxaSelecao)** (Método: Torneio):  
   - Seleciona os melhores cromossomos (com base na taxa de seleção) para compor parte da nova população.
2. **reproduzir(populacao, novaPopulacao, taxaReproducao, estadoFinal)**:  
   - Combina cromossomos selecionados (crossover) para gerar novos indivíduos, completando a nova população.
3. **Verificar mutação (taxaMutacao)**:  
   - Se aplicável, realiza mutações aleatórias em alguns cromossomos da nova população.
     - **mutar(novaPopulacao, estadoFinal)**: Aplica pequenas alterações aleatórias em genes dos cromossomos.
4. **limpar(populacao)**:  
   - Remove todos os cromossomos da população atual (para preparar a substituição).
5. **copiar(novaPopulacao, populacao)**:  
   - Transfere os cromossomos da nova população para a população principal.
6. **limpar(novaPopulacao)**:  
   - Reseta a nova população para a próxima iteração.
7. **ordenarPopulacao(populacao)**:  
   - Reordena a população atualizada com base na aptidão.

---

Este fluxo ilustra o ciclo evolutivo típico de um Algoritmo Genético, onde a cada geração os indivíduos mais aptos têm maior chance de passar suas características adiante, enquanto operadores genéticos (crossover e mutação) introduzem diversidade para explorar o espaço de soluções. 🧬

