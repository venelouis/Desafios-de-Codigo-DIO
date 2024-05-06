/*
Desafios de Código Java Intermediários: Design Patterns
2 / 5 - Implementando uma Calculadora Simples com Padrão Strategy

Descrição:
Você foi designado para criar uma calculadora simples em Java, 
aplicando o padrão de projeto Strategy para representar as operações matemáticas.

Entrada:
O programa deve solicitar ao usuário dois números e a operação desejada. 
As operações podem ser especificadas pelos seguintes sinais: 
+ para soma, - para subtração, * para multiplicação e / para divisão. 
O usuário deve inserir o sinal correspondente à operação desejada.

Saída:
A calculadora deve utilizar o padrão Strategy para realizar a operação escolhida e exibir o resultado.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
100
10
/	

Saída:
10.0

*/

// Solução:

import java.util.Scanner;

// Interface Strategy
interface Operation {
    double execute(double num1, double num2);
}

// Implementações concretas do Strategy
class AddOperation implements Operation {
    @Override
    public double execute(double num1, double num2) {
        return num1 + num2;
    }
}

class SubtractOperation implements Operation {
    @Override
    public double execute(double num1, double num2) {
        return num1 - num2;
    }
}

class MultiplyOperation implements Operation {
    @Override
    public double execute(double num1, double num2) {
        return num1 * num2;
    }
}

// Implementação da estratégia de divisão
class DivideOperation implements Operation {
    @Override
    public double execute(double num1, double num2) {
        return num1 / num2;
    }
}

// Contexto que utiliza a estratégia
class Calculator {
    private Operation operation;

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

    public double performOperation(double num1, double num2) {
        return operation.execute(num1, num2);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Operation addOperation = new AddOperation();
        Operation subtractOperation = new SubtractOperation();
        Operation multiplyOperation = new MultiplyOperation();
        Operation divideOperation = new DivideOperation();

        // Criando a calculadora
        Calculator calculator = new Calculator();

        // Obtendo os números do usuário
        double num1 = scanner.nextDouble();
        double num2 = scanner.nextDouble();

        // Obtendo a operação desejada
        String operationChoice = scanner.next();

        // Configurando a operação na calculadora
        switch (operationChoice) {
            case "+":
                calculator.setOperation(addOperation);
                break;
            case "-":
                calculator.setOperation(subtractOperation);
                break;
            case "*":
                calculator.setOperation(multiplyOperation);
                break;
            case "/":
                calculator.setOperation(divideOperation);
                break;
            default:
                System.out.println("Operação inválida.");
                return;
        }

        // Realizando a operação e exibindo o resultado
        double result = calculator.performOperation(num1, num2);
        System.out.println(result);
    }
}

/* Explicação:

1. Padrão de Projeto Strategy:

- O código implementa o padrão de projeto Strategy 
para encapsular diferentes algoritmos de cálculo em classes separadas 
e permitir a troca dinâmica de algoritmos em tempo de execução. 

2. Partes do código:

- Interface `Operation`:** Define a interface que todas as estratégias de cálculo devem implementar. 
Possui um único método `execute(double num1, double num2)` para realizar o cálculo.

- Classes de estratégias concretas:
 `AddOperation`, `SubtractOperation`, `MultiplyOperation`, `DivideOperation`: 
Implementam a interface `Operation`, cada uma definindo o cálculo específico 
para adição, subtração, multiplicação e divisão, respectivamente.

- Classe `Calculator`: Contexto que utiliza a estratégia. 
Possui um atributo `operation` para armazenar a estratégia atual. 
Os métodos `setOperation(Operation operation)` 
e `performOperation(double num1, double num2)` permitem definir a estratégia 
e realizar a operação, respectivamente.

- Classe `Main`: Ponto de entrada do programa. 
Cria instâncias das estratégias, obtem os números e a operação desejada do usuário, 
configura a estratégia apropriada na calculadora e executa a operação.

3. Funcionamento:

1. O código lê dois números e a operação desejada pelo usuário.
2. De acordo com a operação escolhida, uma estratégia de cálculo específica é configurada na calculadora.
3. A calculadora utiliza o método `execute` da estratégia configurada para realizar o cálculo e obter o resultado.
4. O resultado é impresso para o usuário.

**Benefícios do padrão Strategy:**

- **Flexibilidade:** Permite alterar o comportamento da calculadora sem modificar o código principal, 
apenas trocando a estratégia.
- **Testabilidade:** Cada estratégia pode ser testada de forma independente.
- **Coesão:** Separa as preocupações da lógica de cálculo da classe Calculator, 
melhorando a organização do código.

 */
