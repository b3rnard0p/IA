# 🔹 O que são Sistemas Multiagentes?

Um **Sistema Multiagente (SMA)** é um sistema composto por vários "agentes" autônomos que trabalham juntos para resolver um problema complexo, dividido em partes menores — por isso, o princípio do **"dividir para conquistar"**.

---

## 🔹 Ligação com Inteligência Artificial Distribuída

Sistemas Multiagentes fazem parte de uma subárea da Inteligência Artificial chamada **IA Distribuída**, inspirada em organizações da natureza, como colônias de formigas, abelhas, ou enxames.

- **Exemplo natural**: formigas encontram o caminho mais curto até o alimento trabalhando juntas.
- **Na computação**: vários programas (ou máquinas) trabalham em conjunto, cada um com uma parte do problema, e se comunicam para alcançar um objetivo comum.

---

## 🔹 O que é um Agente?

Na computação, um agente pode ser:

- Uma **entidade de software**, como um programa que toma decisões sozinho.
- Uma **entidade de hardware**, como um robô autônomo.

Pode estar em diferentes lugares (**distribuído geograficamente**) e se comunicar com outros via redes, **sockets**, **multicast**, etc.

---

## 🔹 Aplicações de Sistemas Multiagentes

Podem ser vistos como **equipes ou times**, cada agente com uma função diferente:

### Exemplos:

- **Automação residencial**: luzes, trancas, sensores e câmeras trabalhando juntos para manter a casa segura.
- **Automação industrial**: máquinas que se comunicam para ajustar produção em tempo real.

---

## 🔹 Características de Agentes Inteligentes

### ✅ Autonomia
O agente **toma decisões sozinho**, sem ser comandado o tempo todo.  
> *Exemplo: uso de **threads** (execução independente de tarefas).*

### ✅ Proatividade
Vai atrás de seus objetivos, **não só reage**.  
> *Exemplo: combina **threads** com estruturas **if** para agir conforme condições.*

### ✅ Adaptação / Flexibilidade
Se ajusta a mudanças.  
> *Exemplo: uso de **try-catch** para lidar com erros, e sobrecarga de predicados para comportamentos alternativos.*

### ✅ Habilidade social (comunicação entre agentes)
Agentes trocam mensagens:
- Comando/ordem
- Pergunta
- Plantio de crença (fazer outro agente acreditar em algo)

**Ferramentas usadas**:
- `sockets`
- `.broadcast`
- `.tell`
- `.send`

---

## 🔹 Arquiteturas de Agentes

### 🧱 Imperativa
- Usa programação **procedural** ou **orientada a objetos (OO)**.
- **Exemplos**: Java, C++, Python com threads e sockets.

### 🧠 BDI (Belief-Desire-Intention)
- **Beliefs (Crenças)**: informações que o agente considera verdadeiras (fatos).
- **Desires (Desejos)**: metas ou objetivos que ele gostaria de atingir.
- **Intentions (Intenções)**: metas que ele está realmente tentando atingir agora.

Essa arquitetura é muito usada em agentes "inteligentes" com capacidade de **raciocínio**.

---

