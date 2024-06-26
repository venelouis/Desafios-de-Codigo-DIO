/*
Desafios de Código Java Intermediários: S.O.L.I.D
3 / 5 - Calculando Desconto

Descrição:
O Princípio Aberto/Fechado (Open/Closed Principle - OCP), 
juntamente com o Princípio da Responsabilidade Única (Single Responsibility Principle - SRP), 
faz parte dos fundamentos do design de software que visam promover a flexibilidade e extensibilidade 
dos sistemas. Esse princípio enfatiza que uma classe ou módulo deve ser aberto para extensões, 
permitindo a adição de novas funcionalidades, mas fechado para modificações, evitando alterações 
frequentes em seu código existente.

Seguindo o Princípio Aberto/Fechado, neste desafio você deve criar uma classe base Discount 
e classes derivadas para diferentes tipos de descontos, como StudentDiscount e MembershipDiscount. 
Os estudantes recebem um desconto de 10% e os afiliados recebem um desconto de 15%. Ao seguirmos o OCP, 
criamos sistemas mais fáceis de estender sem comprometer a estabilidade das partes já implementadas, 
resultando em códigos mais robustos, coesos e adaptáveis, características essenciais para 
o desenvolvimento de software escalável e de alta qualidade.

Entrada:
A entrada é composta pelo tipo de desconto (estudante ou afiliado) e o valor original exibidos em 
uma linha separada.

Saída:
A saída esperada é o valor com desconto aplicado (double).

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
    student
    100

    membership
    100

    membership
    245

Saída:
    90.0
    85.0
    208.25
 */

// Solução:

import java.util.Scanner;

/** Classe base para descontos (aberto para extensões) */
class Discount {
  public double calculateDiscount(double originalValue) {
    return originalValue; // No default discount
  }
}

/** Classe derivada para desconto de estudante (10%). */
final class StudentDiscount extends Discount {
  @Override
  public double calculateDiscount(double originalValue) {
    return originalValue * 0.90; // 10% de desconto
  }
}

/** Classe derivada para desconto de afiliado (15%). */
final class MembershipDiscount extends Discount {
  @Override
  public double calculateDiscount(double originalValue) {
    return originalValue * 0.85; // 15% de desconto
  }
}

public class Main {
  public static void main(String[] args) {
    try(Scanner scanner = new Scanner(System.in)) {
      String discountType = scanner.next();
      double originalValue = scanner.nextDouble();
  
      // Aplicação OCP: Criando uma instância com base no tipo de desconto fornecido
      Discount discount;
      if ("student".equals(discountType)) {
          discount = new StudentDiscount();
      } else if ("membership".equals(discountType)) {
          discount = new MembershipDiscount();
      } else {
          discount = new Discount();
      }
  
      double discountValue = discount.calculateDiscount(originalValue);
      System.out.printf("%.2f", discountValue);
    }
  }
}