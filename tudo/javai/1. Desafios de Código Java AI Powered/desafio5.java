/*
Desafios de Código Java Intermediários: Design Patterns
5 / 5 - Implementando um Adaptador para Conversão de Moedas

Descrição
O padrão de projeto Adapter é um padrão de projeto estrutural 
que permite que objetos com interfaces incompatíveis trabalhem juntos. 
Ele atua como um intermediário, adaptando a interface de uma classe para 
outra interface esperada pelo cliente.

Neste desafio, você deverá implementar um conversor de moedas que 
permitirá que valores monetários sejam convertidos de dólares americanos (USD) para euros (EUR). 
Embora exista uma taxa de conversão direta de 1 USD = 0.85 EUR, 
o nosso sistema inicialmente só suportava a conversão de USD para libras esterlinas (GBP). 
Utilizando o padrão Adapter, você deve adaptar esse sistema antigo para fornecer 
a nova funcionalidade de conversão direta para EUR, usando a conversão intermediária para GBP.

Entrada:
Um valor em dólares americanos USD (Double).

Saída:
O valor convertido para euros EUR (Double) usando o adaptador.

Taxa de conversão direta (para referência):
1 USD = 0.85 EUR

Taxas de conversão para a adaptação:
1 USD para GBP = 0.80
1 GBP para EUR = 1.0625

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
200

Saída:
USD: 200.0
EUR: 170.0


Nota:
O padrão Adapter é uma ferramenta valiosa para lidar com incompatibilidades de interface 
e integrar componentes heterogêneos. No entanto, é importante avaliar cuidadosamente sua utilização 
para garantir que os benefícios superem os possíveis custos em termos de complexidade e desempenho.

Caso queira saber mais sobre o Design Pattern Adapter:
https://refactoring.guru/pt-br/design-patterns/adapter
 */

// Solução:
import java.util.Scanner;

// Antiga classe de conversão que só suporta a conversão de USD para GBP
class OldCurrencyConverter {
    public double convertUSDtoGBP(double amount) {
        return amount * 0.80; // 80% do valor em USD
    }
}

// Classe adicional para converter GBP para EUR
class GBPToEURConverter {
    public double convertGBPToEUR(double amount) {
        return amount * 1.0625; // 106.25% do valor em GBP
    }
}

// Novo adaptador que usa a antiga conversão e aplica a taxa adicional de GBP para EUR
class CurrencyAdapter {
    private final OldCurrencyConverter oldConverter;
    private final GBPToEURConverter newConverter;

    public CurrencyAdapter(OldCurrencyConverter oldConverter, GBPToEURConverter newConverter) {
        this.oldConverter = oldConverter;
        this.newConverter = newConverter;
    }

    public double convertUSDtoEUR(double amount) {
        double gbp = oldConverter.convertUSDtoGBP(amount);
        return newConverter.convertGBPToEUR(gbp);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double input = Double.parseDouble(scanner.nextLine());

        OldCurrencyConverter oldConverter = new OldCurrencyConverter();
        GBPToEURConverter newConverter = new GBPToEURConverter();
        CurrencyAdapter adapter = new CurrencyAdapter(oldConverter, newConverter);

        double eur = adapter.convertUSDtoEUR(input);

        System.out.println("USD: " + input);
        System.out.println("EUR: " + eur);
    }
}

/*
O código é uma implementação do padrão de projeto Adapter em Java. 
Este padrão é usado quando queremos fazer duas interfaces incompatíveis trabalharem juntas.

Aqui está uma breve explicação das classes e métodos:

1. `OldCurrencyConverter`: Esta é uma classe que representa um conversor de moedas antigo. 
Presumivelmente, ela tem um método para converter USD para EUR.

2. `GBPToEURConverter`: Esta é uma classe que representa um novo conversor de moedas. 
Presumivelmente, ela tem um método para converter GBP para EUR.

3. `CurrencyAdapter`: Esta é a classe do adaptador. 
Ela tem uma instância de `OldCurrencyConverter` e `GBPToEURConverter`. 
Ela usa o `OldCurrencyConverter` para converter USD para GBP, 
e então usa o `GBPToEURConverter` para converter GBP para EUR.

4. `main`: Este é o método principal onde a execução do programa começa. 
Ele lê um valor em USD do usuário, usa o `CurrencyAdapter` para converter esse valor para EUR, 
e então imprime ambos os valores.

 */