import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Perceptron {
    private List<Ponto> amostras;
    private List<Integer> saidas;
    private double taxaAprendizado;
    private int geracoes;
    private int limiar;
    private double[] pesos;

    public Perceptron(List<Ponto> amostras, List<Integer> saidas,
                      double taxaAprendizado, int geracoes, int limiar) {
        this.amostras = amostras;
        this.saidas = saidas;
        this.taxaAprendizado = taxaAprendizado;
        this.geracoes = geracoes;
        this.limiar = limiar;
        this.pesos = new double[3]; // limiar + dois atributos
    }

    private int funcaoAtivacao(double soma) {
        return soma >= 0 ? 1 : -1;
    }

    public void treinar() {
        // Atribui limiar a cada ponto
        for (Ponto p : amostras) {
            p.limiar = this.limiar;
        }

        // Inicializa pesos
        Random gerador = new Random();
        pesos[0] = limiar;
        pesos[1] = gerador.nextDouble() - 0.5;  // pequenos valores centrais em 0
        pesos[2] = gerador.nextDouble() - 0.5;

        int epocaUsada = 0;

        for (int epoca = 1; epoca <= geracoes; epoca++) {
            int erros = 0;

            // Opcional: embaralha amostras para melhor convergência
            List<Ponto> copiaAmostras = new java.util.ArrayList<>(amostras);
            List<Integer> copiaSaidas = new java.util.ArrayList<>(saidas);
            Collections.shuffle(copiaAmostras, gerador);
            Collections.shuffle(copiaSaidas, gerador);

            for (int i = 0; i < copiaAmostras.size(); i++) {
                Ponto ponto = copiaAmostras.get(i);
                int saidaDesejada = copiaSaidas.get(i);

                // calcula soma de ativação para esta amostra
                double soma = ponto.limiar * pesos[0]
                        + ponto.x      * pesos[1]
                        + ponto.y      * pesos[2];

                int saidaGerada = funcaoAtivacao(soma);
                if (saidaGerada != saidaDesejada) {
                    erros++;
                    // atualiza pesos
                    int erro = saidaDesejada - saidaGerada;
                    pesos[0] += taxaAprendizado * erro * ponto.limiar;
                    pesos[1] += taxaAprendizado * erro * ponto.x;
                    pesos[2] += taxaAprendizado * erro * ponto.y;
                }
            }

            if (erros == 0) {
                epocaUsada = epoca;
                break;
            }
            epocaUsada = epoca;
        }

        System.out.println("Convergiu em " + epocaUsada + " épocas (máx " + geracoes + ")");
        System.out.printf("Pesos finais: [%.4f, %.4f, %.4f]%n", pesos[0], pesos[1], pesos[2]);
    }

    public void testar(Ponto amostra) {
        amostra.limiar = this.limiar;
        double soma = amostra.limiar * pesos[0]
                + amostra.x      * pesos[1]
                + amostra.y      * pesos[2];
        int saidaGerada = funcaoAtivacao(soma);
        String classe = (saidaGerada == 1) ? "Time Azul" : "Time Vermelho";
        System.out.println("Classe: " + saidaGerada + " (" + classe + ")");
    }
}
