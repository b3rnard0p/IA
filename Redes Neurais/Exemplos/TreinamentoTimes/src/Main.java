import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("Exemplo de RNA Perceptron para classificação de equipes");

        List<Ponto> amostras = new ArrayList<>();
        List<Integer> saidas = new ArrayList<>();

        // ✅ Lê dados de um CSV
        String caminhoCSV = "dados.csv"; // <-- coloque aqui o caminho correto
        lerCSV(caminhoCSV, amostras, saidas);

        double taxaAprendizado = 0.1;
        int geracoes = 1000;
        int limiar = 1;

        Perceptron p = new Perceptron(amostras, saidas, taxaAprendizado, geracoes, limiar);
        p.treinar();

        Scanner scanner = new Scanner(System.in);
        String op;
        do {
            System.out.print("\n\nInforme valor para x (-1 a 1): ");
            double x = scanner.nextDouble();
            System.out.print("Informe valor para y (-1 a 1): ");
            double y = scanner.nextDouble();

            p.testar(new Ponto(x, y));
            System.out.print("Digite '1' para sair ou qualquer outra tecla para testar novamente: ");
            op = scanner.next();
        } while (!"1".equals(op));

        scanner.close();
    }

    private static void lerCSV(String caminho, List<Ponto> amostras, List<Integer> saidas) {
        try (BufferedReader br = new BufferedReader(new FileReader(caminho))) {
            String linha;
            boolean cabecalho = true;
            while ((linha = br.readLine()) != null) {
                if (cabecalho) { // pula a primeira linha (cabeçalho)
                    cabecalho = false;
                    continue;
                }
                String[] partes = linha.split(",");
                if (partes.length != 3) continue;

                double x = Double.parseDouble(partes[0].trim());
                double y = Double.parseDouble(partes[1].trim());
                int saida = Integer.parseInt(partes[2].trim());

                amostras.add(new Ponto(x, y));
                saidas.add(saida);
            }
        } catch (IOException e) {
            System.err.println("Erro ao ler arquivo CSV: " + e.getMessage());
        }
    }
}
