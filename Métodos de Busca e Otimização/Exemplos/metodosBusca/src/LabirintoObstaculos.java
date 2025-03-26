import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import busca.BuscaLargura;
import busca.BuscaProfundidade;
import busca.Estado;
import busca.MostraStatusConsole;
import busca.Nodo;
import javax.swing.JOptionPane;

public class LabirintoObstaculos implements Estado{
    final char matriz[][];
    int linhaEntrada1, colunaEntrada1;
    int linhaEntrada2, colunaEntrada2;
    int linhaSaida, colunaSaida;
    final String op;
    final int entradaAlvo;

    public LabirintoObstaculos(char m[][], int linhaEntrada1, int colunaEntrada1, 
                              int linhaEntrada2, int colunaEntrada2, 
                              int linhaSaida, int colunaSaida, 
                              String o, int entradaAlvo) {
        this.matriz = clonar(m);
        this.linhaEntrada1 = linhaEntrada1;
        this.colunaEntrada1 = colunaEntrada1;
        this.linhaEntrada2 = linhaEntrada2;
        this.colunaEntrada2 = colunaEntrada2;
        this.linhaSaida = linhaSaida;
        this.colunaSaida = colunaSaida;
        this.op = o;
        this.entradaAlvo = entradaAlvo;
    }

    public LabirintoObstaculos(int dimensao, String o, int porcentagemObstaculos) {
        this.matriz = new char[dimensao][dimensao];
        this.op = o;
        this.entradaAlvo = 0;
        
        Random gerador = new Random();
        int quantidadeObstaculos = (dimensao*dimensao)*porcentagemObstaculos/100;

        int entrada1 = gerador.nextInt(dimensao * dimensao);
        int entrada2;
        do {
            entrada2 = gerador.nextInt(dimensao * dimensao);
        } while (entrada1 == entrada2);
        
        int saida;
        do {
            saida = gerador.nextInt(dimensao * dimensao);
        } while (entrada1 == saida || entrada2 == saida);

        int pos = 0;
        for (int i = 0; i < dimensao; i++) {
            for (int j = 0; j < dimensao; j++) {
                if (pos == entrada1) {
                    matriz[i][j] = 'E';
                    linhaEntrada1 = i;
                    colunaEntrada1 = j;
                } else if (pos == entrada2) {
                    matriz[i][j] = 'E';
                    linhaEntrada2 = i;
                    colunaEntrada2 = j;
                } else if (pos == saida) {
                    matriz[i][j] = 'S';
                    linhaSaida = i;
                    colunaSaida = j;
                } else if (quantidadeObstaculos > 0 && gerador.nextInt(3) == 1) {
                    quantidadeObstaculos--;
                    matriz[i][j] = '@';
                } else {
                    matriz[i][j] = 'O';
                }
                pos++;
            }
        }
    }

    private char[][] clonar(char[][] origem) {
        char[][] destino = new char[origem.length][origem.length];
        for (int i = 0; i < origem.length; i++) {
            System.arraycopy(origem[i], 0, destino[i], 0, origem.length);
        }
        return destino;
    }

    @Override
    public boolean ehMeta() {
        if (entradaAlvo == 1) {
            return linhaEntrada1 == linhaSaida && colunaEntrada1 == colunaSaida;
        } else if (entradaAlvo == 2) {
            return linhaEntrada2 == linhaSaida && colunaEntrada2 == colunaSaida;
        }
        return false;
    }

    @Override
    public int custo() {
        return 1;
    }
    
    @Override
    public List<Estado> sucessores() {
        List<Estado> visitados = new LinkedList<>();
        
        if (entradaAlvo == 1 || entradaAlvo == 0) {
            gerarMovimentos(visitados, 1);
        }
        if (entradaAlvo == 2 || entradaAlvo == 0) {
            gerarMovimentos(visitados, 2);
        }
        
        return visitados;
    }

    private void gerarMovimentos(List<Estado> visitados, int entrada) {
        int linhaAtual = (entrada == 1) ? linhaEntrada1 : linhaEntrada2;
        int colunaAtual = (entrada == 1) ? colunaEntrada1 : colunaEntrada2;

        if (linhaAtual > 0 && matriz[linhaAtual-1][colunaAtual] != '@') {
            adicionarSucessor(visitados, entrada, linhaAtual-1, colunaAtual, "cima");
        }
        if (linhaAtual < matriz.length-1 && matriz[linhaAtual+1][colunaAtual] != '@') {
            adicionarSucessor(visitados, entrada, linhaAtual+1, colunaAtual, "baixo");
        }
        if (colunaAtual > 0 && matriz[linhaAtual][colunaAtual-1] != '@') {
            adicionarSucessor(visitados, entrada, linhaAtual, colunaAtual-1, "esquerda");
        }
        if (colunaAtual < matriz.length-1 && matriz[linhaAtual][colunaAtual+1] != '@') {
            adicionarSucessor(visitados, entrada, linhaAtual, colunaAtual+1, "direita");
        }
    }

    private void adicionarSucessor(List<Estado> visitados, int entrada, 
                                  int novaLinha, int novaColuna, String direcao) {
        char[][] mTemp = clonar(matriz);
        mTemp[(entrada == 1) ? linhaEntrada1 : linhaEntrada2]
             [(entrada == 1) ? colunaEntrada1 : colunaEntrada2] = 'O';
        mTemp[novaLinha][novaColuna] = 'E';

        LabirintoObstaculos novo = new LabirintoObstaculos(
            mTemp,
            (entrada == 1) ? novaLinha : linhaEntrada1,
            (entrada == 1) ? novaColuna : colunaEntrada1,
            (entrada == 2) ? novaLinha : linhaEntrada2,
            (entrada == 2) ? novaColuna : colunaEntrada2,
            linhaSaida, colunaSaida,
            "Movendo para " + direcao + " (Entrada " + entrada + ")",
            entradaAlvo == 0 ? entrada : entradaAlvo
        );
        
        if (!visitados.contains(novo)) {
            visitados.add(novo);
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof LabirintoObstaculos)) return false;
        LabirintoObstaculos e = (LabirintoObstaculos) o;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz.length; j++) {
                if (e.matriz[i][j] != matriz[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    @Override
    public int hashCode() {
        StringBuilder estado = new StringBuilder();
        for (char[] linha : matriz) {
            estado.append(linha);
        }
        return estado.toString().hashCode();
    }

    @Override
    public String toString() {
        StringBuilder resultado = new StringBuilder();
        for (char[] linha : matriz) {
            for (char c : linha) {
                resultado.append(c).append("\t");
            }
            resultado.append("\n");
        }
        resultado.append("Entrada 1: (").append(linhaEntrada1).append(",").append(colunaEntrada1).append(")\n");
        resultado.append("Entrada 2: (").append(linhaEntrada2).append(",").append(colunaEntrada2).append(")\n");
        resultado.append("Saída: (").append(linhaSaida).append(",").append(colunaSaida).append(")\n");
        return "\n" + op + "\n" + resultado + "\n";
    }

    public static void main(String[] a) {
        try {
            int dimensao = Integer.parseInt(JOptionPane.showInputDialog("Dimensão do labirinto:"));
            int porcentagem = Integer.parseInt(JOptionPane.showInputDialog("Porcentagem de obstáculos:"));
            int metodo1 = Integer.parseInt(JOptionPane.showInputDialog("1-Profundidade\n2-Largura\nEntrada 1:"));
            int metodo2 = Integer.parseInt(JOptionPane.showInputDialog("1-Profundidade\n2-Largura\nEntrada 2:"));

            LabirintoObstaculos inicial = new LabirintoObstaculos(dimensao, "Estado Inicial", porcentagem);
            LabirintoObstaculos paraEntrada1 = new LabirintoObstaculos(
                inicial.matriz, 
                inicial.linhaEntrada1, inicial.colunaEntrada1,
                inicial.linhaEntrada2, inicial.colunaEntrada2,
                inicial.linhaSaida, inicial.colunaSaida,
                "Resolvendo Entrada 1", 1);
            
            LabirintoObstaculos paraEntrada2 = new LabirintoObstaculos(
                inicial.matriz, 
                inicial.linhaEntrada1, inicial.colunaEntrada1,
                inicial.linhaEntrada2, inicial.colunaEntrada2,
                inicial.linhaSaida, inicial.colunaSaida,
                "Resolvendo Entrada 2", 2);

            System.out.println("=== SOLUÇÃO PARA ENTRADA 1 ===");
            Nodo solucao1 = (metodo1 == 1) ? 
                new BuscaProfundidade(new MostraStatusConsole()).busca(paraEntrada1) :
                new BuscaLargura(new MostraStatusConsole()).busca(paraEntrada1);
            
            if (solucao1 != null) {
                System.out.println(solucao1.montaCaminho());
            } else {
                System.out.println("Sem solução para Entrada 1");
            }

            System.out.println("\n=== SOLUÇÃO PARA ENTRADA 2 ===");
            Nodo solucao2 = (metodo2 == 1) ? 
                new BuscaProfundidade(new MostraStatusConsole()).busca(paraEntrada2) :
                new BuscaLargura(new MostraStatusConsole()).busca(paraEntrada2);
            
            if (solucao2 != null) {
                System.out.println(solucao2.montaCaminho());
            } else {
                System.out.println("Sem solução para Entrada 2");
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Erro: " + e.getMessage());
        }
    }

    @Override
    public String getDescricao() {
        return "Labirinto com duas entradas (E) e uma saída (S). Obstáculos (@).";
    }
}

/**
Classe LabirintoObstaculos:
* 
A classe LabirintoObstaculos é uma implementação de um labirinto com dois pontos de entrada, um ponto de saída e obstáculos. 
* Ela implementa a interface Estado e a interface Heuristica, sendo utilizada para representar estados no contexto de um algoritmo de busca.
* 
Construtores:
* 
LabirintoObstaculos(char m[][], int linhaEntrada1, int colunaEntrada1, int linhaEntrada2, int colunaEntrada2, int linhaSaida, int colunaSaida, String o, int entradaAlvo):
Este é o construtor principal da classe. Ele recebe uma matriz representando o labirinto (m), as coordenadas 
* das duas entradas e da saída, uma string de descrição do estado e o índice da entrada alvo (1 ou 2).

LabirintoObstaculos(int dimensao, String o, int porcentagemObstaculos):
Este é o segundo construtor que cria um labirinto aleatório. Ele recebe a dimensão do labirinto, uma descrição do 
* estado e a porcentagem de obstáculos. O método gera aleatoriamente as posições das entradas e saída, além de preencher o labirinto com obstáculos.

Métodos:
* 
private char[][] clonar(char[][] origem):
Este método cria uma cópia (clone) da matriz do labirinto. Ele é usado para gerar novos estados do labirinto sem modificar o estado original.

@Override public boolean ehMeta():
Este método verifica se o estado atual é uma solução (meta). Ele compara a posição de uma das entradas 
* com a posição da saída, retornando true se as posições coincidirem, dependendo da entrada alvo (1 ou 2).

@Override public int custo():
Este método retorna o custo de mover-se de um estado para outro. No caso deste labirinto, o custo é sempre 1, 
* pois cada movimento (independente da direção) tem o mesmo custo.

@Override public int h():
Este método calcula a heurística (estimativa de custo) para alcançar a saída a partir do estado atual. 
* Ele usa a distância de Manhattan entre a entrada e a saída, dependendo de qual entrada é a "alvo" (entrada 1 ou entrada 2).

@Override public List<Estado> sucessores():
Este método gera uma lista de sucessores (novos estados) a partir do estado atual. Ele verifica se os movimentos possíveis 
* (para cima, baixo, esquerda, direita) não resultam em colidir com um obstáculo, e, caso contrário, adiciona o novo estado à lista de sucessores.

private void gerarMovimentos(List<Estado> visitados, int entrada):
Este método ajuda a gerar os movimentos possíveis a partir de um estado específico. Ele verifica os quatro 
* sentidos (cima, baixo, esquerda, direita) e adiciona sucessores válidos à lista de visitados. O movimento é restrito por obstáculos ('@').

private void adicionarSucessor(List<Estado> visitados, int entrada, int novaLinha, int novaColuna, String direcao):
Este método cria um novo estado, movendo a entrada atual para a nova posição (linha e coluna). O novo estado é adicionado 
* à lista de sucessores, desde que ainda não tenha sido visitado.

@Override public boolean equals(Object o):
Este método compara o estado atual com outro objeto. Ele verifica se a matriz de labirinto é idêntica à de outro 
* estado, realizando a comparação posição por posição.

@Override public int hashCode():
Este método gera um código de hash para o estado atual. Ele cria um código baseado na matriz do labirinto, permitindo a comparação eficiente entre estados.

@Override public String toString():
Este método retorna uma representação em string do labirinto, com as coordenadas das entradas e da saída. Ele formata a matriz do labirinto em uma string legível.

public static void main(String[] a):
Este é o método principal, que executa o programa. Ele solicita ao usuário a dimensão do labirinto, a porcentagem de 
* obstáculos e os métodos de busca (profundidade ou largura) a serem utilizados para cada entrada. Em seguida, ele resolve 
* o labirinto para as duas entradas, imprimindo o caminho encontrado ou uma mensagem indicando que não há solução.

@Override public String getDescricao():
Este método retorna uma descrição do labirinto, informando que ele contém duas entradas (representadas por 'E'), uma saída ('S') e obstáculos ('@').
* */
