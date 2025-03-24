import java.util.LinkedList;
import java.util.List;
import java.util.Random;
import busca.Heuristica;
import busca.BuscaLargura;
import busca.BuscaProfundidade;
import busca.Estado;
import busca.MostraStatusConsole;
import busca.Nodo;
import javax.swing.JOptionPane;

public class LabirintoObstaculos implements Estado, Heuristica {
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
    public int h() {
        if (entradaAlvo == 1) {
            return Math.abs(linhaEntrada1 - linhaSaida) + Math.abs(colunaEntrada1 - colunaSaida);
        } else if (entradaAlvo == 2) {
            return Math.abs(linhaEntrada2 - linhaSaida) + Math.abs(colunaEntrada2 - colunaSaida);
        }
        return 0;
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