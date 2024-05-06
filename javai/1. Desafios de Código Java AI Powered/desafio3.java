/*
Desafios de Código Java Intermediários: Design Patterns
3 / 5 - Implementando um Catálogo de Produtos com Padrão Observer

Descrição:
Você deve aprimorar o sistema de monitoramento de produtos, 
adicionando a capacidade de exibir uma mensagem específica para cada usuário 
quando um novo produto é adicionado ao catálogo. 
Além disso, implemente a funcionalidade de permitir que 
os usuários cancelem sua assinatura para deixar de receber notificações sobre novos produtos.

Entrada:
O programa deve solicitar ao usuário que insira o nome do usuário para realizar a ação desejada.
Se o usuário deseja cancelar a assinatura, ele deve digitar "cancelar". 
Se desejar receber notificações, deve digitar qualquer outro valor.
Se o usuário optar por adicionar um novo produto, será solicitado o nome do produto a ser adicionado.

Saída:
Após cada ação, o programa deve exibir mensagens informativas 
para indicar se a assinatura foi cancelada com sucesso, 
se o usuário ainda está assinando notificações ou se o produto foi adicionado ao catálogo.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
TV
Smart
999
S	

Saída:
Notificacao recebida: Novo produto adicionado - TV

 */

// Solução:
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner; // Importando a classe Scanner

// Interface Observer
interface Observer {
    void update(String productName);
}

// Classe concreta Observer
class User implements Observer {
    private String name;
    private boolean isSubscribed;

    public User(String name) {
        this.name = name;
        this.isSubscribed = true;
    }

    public void setSubscription(boolean isSubscribed) {
        this.isSubscribed = isSubscribed;
    }

    @Override
    public void update(String productName) {
        if (isSubscribed) {
            System.out.println("Notificacao recebida: Novo produto adicionado - " + productName);
        }
    }
}

// Interface Observable
interface CatalogObservable {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers(String productName);
}

// Classe concreta Observable
class Catalog implements CatalogObservable {
    private List<Observer> observers = new ArrayList<>();

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(String productName) {
        for (Observer observer : observers) {
            observer.update(productName);
        }
    }

    public void addProduct(String name, String description, double price) {
        notifyObservers(name);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Criando catálogo e usuário
        Catalog catalog = new Catalog();
        User user = new User("Usuário 1");

        // Inscricao do usuário no catálogo
        catalog.addObserver(user);

        while (scanner.hasNext()) {
            // Adicionando novo produto
            String name = scanner.nextLine();
            String description = scanner.nextLine();
            double price = scanner.nextDouble();

            scanner.nextLine(); // Consumir a quebra de linha após nextDouble
            String subscribeChoice = scanner.nextLine();

            // Verifique qual foi a escolha de notificação (S ou N) do usuário
            if (subscribeChoice.equalsIgnoreCase("N")) {
                user.setSubscription(false);
                System.out.println("Programa Encerrado."); // Adicionando a mensagem de saída
                break;
            }

            // Adicionando produto ao catálogo
            catalog.addProduct(name, description, price);
        }

        scanner.close();
    }
}
/*
O código é uma implementação do padrão de projeto Observer em Java. 
Este padrão é usado quando uma mudança em um objeto (o Subject) 
deve ser refletida em outros objetos (os Observers) sem manter os objetos fortemente acoplados.

Aqui está uma breve explicação das classes e interfaces:

1. `Observer`: Esta é uma interface que define o método `update`. 
Qualquer classe que implemente esta interface terá que fornecer uma implementação para este método.

2. `User`: Esta classe implementa a interface `Observer`. 
Ela tem os atributos `name` e `isSubscribed`. 
O método `update` é implementado de tal forma que 
uma notificação é impressa apenas se `isSubscribed` for verdadeiro.

3. `CatalogObservable`: Esta é uma interface que define métodos para adicionar, 
remover e notificar observadores.

4. `Catalog`: Esta classe implementa a interface `CatalogObservable`. 
Ela mantém uma lista de observadores e fornece métodos para adicionar, remover e notificá-los.

5. `Main`: Esta é a classe principal onde a execução do programa começa. 
Ela cria um `Catalog` e um `User`, inscreve o usuário no catálogo, 
e então entra em um loop onde continua adicionando produtos ao catálogo e notificando o usuário.

Em relação aos comentários:

- O campo `User.name` é de fato declarado e inicializado, mas nunca usado. 
Se não houver necessidade de usar este campo no futuro, 
você poderia removê-lo para tornar o código mais limpo.

- Em Java, cada classe ou interface pública deve ser declarada em seu próprio arquivo. 
No entanto, esta regra é frequentemente relaxada em ambientes educacionais ou para pequenos programas. 
Se você quiser aderir estritamente a esta regra, você deveria mover a classe `Main` 
para seu próprio arquivo chamado `Main.java`.

Aqui está o método `setSubscription`:

```java
public void setSubscription(boolean isSubscribed) {
    this.isSubscribed = isSubscribed;
}
```

Este método é um setter para o campo `isSubscribed`. 
Ele permite que o código externo mude o status de inscrição de um objeto `User`. 
Se `isSubscribed` for definido como `false`, o usuário deixará de receber notificações.
 */