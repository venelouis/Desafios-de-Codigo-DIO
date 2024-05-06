/*
Desafios de Código Java Intermediários: S.O.L.I.D
5 / 5 - Gerenciamento de Colaboradores

Descrição:
Desenvolva um programa para gerenciar colaboradores sob dois regimes de contratação distintos: 
Pessoa Jurídica (PJ) e Consolidação das Leis do Trabalho (CLT). 
O programa deve calcular os salários de acordo com o tipo de contrato fornecido pelo usuário e aplicar 
a lógica adequada para cada caso. Este desafio visa aplicar os princípios SOLID, 
como Single Responsibility, Open/Closed, Liskov Substitution e Interface Segregation na implementação 
do sistema, garantindo uma arquitetura flexível e fácil de manter.

Entrada:
O programa deve receber como entrada o tipo de contrato (PJ ou CLT) seguido dos valores necessários 
para o cálculo do salário, conforme o seguinte formato:

Para PJ: o número de horas trabalhadas e o valor da hora, separados por vírgula.
Para CLT: o salário base e o valor das comissões, separados por vírgula.

Saída:
A saída deve ser o valor do salário calculado de acordo com o tipo de contrato e os dados fornecidos. 
Por exemplo: CLT: 5462.0.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
    PJ
    40,160

    CLT
    4942,520

    CLT
    2824.54,300

Saída:
    6400.0

    5462.0

    3124.54
 */

// Solução:
import java.util.Scanner;

interface Employee {
    double calculateSalary();
}

interface ContractType {
    double getSalary();
}

class CLTEmployee implements Employee {
    private final ContractType contractType;
    public CLTEmployee(ContractType contractType) {
        this.contractType = contractType;
    }
    @Override
    public double calculateSalary() {
        return contractType.getSalary();
    }
}

class PJEmployee implements Employee {
    private final ContractType contractType;
    public PJEmployee(ContractType contractType) {
        this.contractType = contractType;
    }
    @Override
    public double calculateSalary() {
        return contractType.getSalary();
    }
}

class CLT implements ContractType {
    private final double baseSalary;
    private final double commissions;
    public CLT(double baseSalary, double commissions) {
        this.baseSalary = baseSalary;
        this.commissions = commissions;
    }
    @Override
    public double getSalary() {
        return baseSalary + commissions;
    }
}

class PJ implements ContractType {
    private final double hoursWorked;
    private final double hourlyRate;
    public PJ(double hoursWorked, double hourlyRate) {
        this.hoursWorked = hoursWorked;
        this.hourlyRate = hourlyRate;
    }
    @Override
    public double getSalary() {
        return hoursWorked * hourlyRate;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String contractType = scanner.nextLine();
        if (contractType.equalsIgnoreCase("CLT")) {
            String[] input = scanner.nextLine().split(",");
            double baseSalary = Double.parseDouble(input[0]);
            double commissions = Double.parseDouble(input[1]);
            ContractType cltContract = new CLT(baseSalary, commissions);
            Employee cltEmployee = new CLTEmployee(cltContract);
            System.out.println("CLT: " + cltEmployee.calculateSalary());
        } else if (contractType.equalsIgnoreCase("PJ")) {
            String[] input = scanner.nextLine().split(",");
            double hoursWorked = Double.parseDouble(input[0]);
            double hourlyRate = Double.parseDouble(input[1]);
            ContractType pjContract = new PJ(hoursWorked, hourlyRate);
            Employee pjEmployee = new PJEmployee(pjContract);
            System.out.println("PJ: " + pjEmployee.calculateSalary());
        }
        scanner.close();
    }
}
