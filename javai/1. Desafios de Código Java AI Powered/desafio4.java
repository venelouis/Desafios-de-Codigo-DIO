/*
Desafios de Código Java Intermediários: Design Patterns
4 / 5 - Implementando um Carrinho de Compras com Padrão Strategy

Descrição:
Você está desenvolvendo um sistema simples de carrinho de compras. 
O desafio é implementar a funcionalidade de calcular o total da compra, 
permitindo que o usuário escolha entre diferentes estratégias de desconto, 
utilizando o padrão de projeto Strategy.

Entrada:
O programa deve permitir que o usuário adicione produtos ao carrinho, 
informando o nome e o preço de cada produto. 
Em seguida, o usuário deve escolher a estratégia de desconto desejada entre duas opções: 
10% de desconto ou frete grátis.

Saída:
O programa deve calcular e exibir o total da compra com base na estratégia de desconto escolhida.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
Livro
45
1	

Saída:
Total da compra: R$40.5

 */

// Solução:
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

interface DiscountStrategy {
    double applyDiscount(double total);
}

class TenPercentDiscount implements DiscountStrategy {
    @Override
    public double applyDiscount(double total) {
        return total * 0.9;
    }
}

class FreeShipping implements DiscountStrategy {
    @Override
    public double applyDiscount(double total) {
        System.out.println("Frete gratis aplicado");
        return total;
    }
}

class ShoppingCart {
    private List<Double> products = new ArrayList<>();
    private DiscountStrategy discountStrategy;

    public void addProduct(double price) {
        products.add(price);
    }

    public void setDiscountStrategy(DiscountStrategy discountStrategy) {
        this.discountStrategy = discountStrategy;
    }

    public double calculateTotal() {
        double total = 0.0;
        for (Double price : products) {
            total += price;
        }
        return discountStrategy.applyDiscount(total);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        DiscountStrategy tenPercentDiscount = new TenPercentDiscount();
        DiscountStrategy freeShipping = new FreeShipping();

        ShoppingCart cart = new ShoppingCart();

        String productName = scanner.nextLine();
        double productPrice = scanner.nextDouble();
        cart.addProduct(productPrice);

        int strategyChoice = scanner.nextInt();
        switch (strategyChoice) {
            case 1:
                cart.setDiscountStrategy(tenPercentDiscount);
                break;
            case 2:
                cart.setDiscountStrategy(freeShipping);
                break;
            default:
                System.out.println("Escolha invalida. Nenhum desconto aplicado.");
        }

        double total = cart.calculateTotal();
        System.out.println("Total da compra: R$" + total);
    }
}

/*
O código é uma implementação do padrão de projeto Strategy em Java.
Este padrão é usado quando queremos escolher o algoritmo a ser usado em tempo de execução. 
Neste caso, o algoritmo é a estratégia de desconto a ser aplicada em um carrinho de compras.

Aqui está uma breve explicação das classes e métodos:

1. `DiscountStrategy`: Esta é uma interface que define o método `applyDiscount`. 
Qualquer classe que implemente esta interface terá que fornecer uma implementação para este método.

2. `TenPercentDiscount` e `FreeShipping`: Estas classes implementam a interface `DiscountStrategy`. 
Elas fornecem implementações diferentes para o método `applyDiscount`.

3. `ShoppingCart`: Esta classe representa um carrinho de compras. 
Ela mantém uma lista de preços de produtos e uma estratégia de desconto. 
O método `calculateTotal` calcula o total do carrinho aplicando a estratégia de desconto.

4. `Main`: Esta é a classe principal onde a execução do programa começa. 
Ela cria um `ShoppingCart` e duas estratégias de desconto. 
Em seguida, lê o nome e o preço de um produto do usuário, adiciona o produto ao carrinho, 
lê a escolha da estratégia de desconto do usuário e aplica a estratégia escolhida ao carrinho.

Na linha 78, o código está lendo a escolha da estratégia de desconto do usuário. 
Se o usuário digitar `1`, a estratégia de desconto de dez por cento será aplicada ao carrinho. 
Se o usuário digitar qualquer outro número, nenhuma estratégia de desconto será aplicada.
 */