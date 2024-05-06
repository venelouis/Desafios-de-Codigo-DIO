// Desafios de Código Java Intermediários: Design Patterns

/* (comentário de várias linhas com a explicação do desafio):

Desafios de Código Java Intermediários: Design Patterns
1 / 5 - Padronizando um Sistema de Gerenciamento de Usuários

Descrição:
O Singleton é uma abordagem de design de software que visa assegurar a existência de 
apenas uma instância de uma classe e fornecer um ponto centralizado para acessá-la. 
Isso é especialmente benéfico em contextos nos quais é desejável manter uma única ocorrência 
de uma classe responsável pelo controle de um recurso compartilhado, como configurações, 
conexões de banco de dados ou caches.

Neste desafio, você deve criar um sistema de gerenciamento de usuários que 
permita adicionar e listar usuários. Você tem a opção de implementar o padrão Singleton para 
garantir que haja apenas uma instância do gerenciador de usuários em toda a aplicação. 
No entanto, a implementação do padrão Singleton é opcional 
e você pode optar por seguir uma abordagem diferente para resolver o desafio, se preferir.

Especificações do Desafio:

Crie uma classe User com os seguintes atributos: id (inteiro) e name (string).
Implemente uma classe UserManager que siga o padrão Singleton. 
Esta classe deve possuir as seguintes funcionalidades:
a. Adicionar um novo usuário ao sistema, recebendo o nome como entrada.
b. Listar todos os usuários cadastrados.
No programa principal (main), siga as etapas abaixo:
a. Solicite ao usuário a quantidade de usuários que deseja cadastrar.
b. Peça ao usuário para informar os nomes dos usuários, um por linha.
c. Após receber os nomes e cadastrar os usuários, liste os usuários cadastrados.

Entrada:
Um número inteiro representando a quantidade de usuários que o usuário deseja cadastrar.

Para cada usuário a ser cadastrado, uma string contendo o nome do usuário.

Saída:
Uma lista com os nomes dos usuários cadastrados.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
2
Ada
Linus	

Saída:
1 - Ada
2 - Linus

*/

// Solução:
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class User {
    private int id;
    private String name;

    public User(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}

class UserManager {
    private static UserManager instance;
    private List<User> users;

    private UserManager() {
        users = new ArrayList<>();
    }

    public static UserManager getInstance() {
        if (instance == null) {
            instance = new UserManager();
        }
        return instance;
    }

    public void addUser(String name) {
        int id = users.size() + 1;
        users.add(new User(id, name));
    }

    public void listUsers() {
        for (User user : users) {
            System.out.println(user.getId() + " - " + user.getName());
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numUsers = scanner.nextInt();
        scanner.nextLine(); // consume newline left-over
        UserManager userManager = UserManager.getInstance();
        for (int i = 0; i < numUsers; i++) {
            String name = scanner.nextLine();
            userManager.addUser(name);
        }
        userManager.listUsers();
    }
}

/*
Explicação do Código Java:

Este código implementa um sistema básico de gerenciamento de usuários. Vamos analisar cada parte:

1. Classe User:

    Define a estrutura de um usuário com atributos:
        id: Inteiro representando o identificador único do usuário (auto-incrementado).
        name: String contendo o nome do usuário.
    Possui construtor User(int id, String name) que inicializa os atributos.
    Possui métodos getId() e getName() para acessar os valores dos atributos.

2. Classe UserManager:

    Implementa o padrão Singleton para garantir que exista apenas uma instância do gerenciador de usuários.
        private static UserManager instance: Armazena a instância única do gerenciador.
        private List<User> users: Lista para armazenar os usuários cadastrados.
        Construtor privado UserManager(): Inicializa a lista users.
        public static UserManager getInstance(): Verifica se a instância já existe (null) e a cria caso contrário. Retorna a instância.
    Possui métodos para gerenciar usuários:
        public void addUser(String name): Adiciona um novo usuário à lista users. O ID é gerado automaticamente (tamanho da lista + 1).
        public void listUsers(): Percorre a lista users e imprime o ID e nome de cada usuário.

3. Classe Main:

    Ponto de entrada do programa.
    Utiliza um scanner para ler a entrada do usuário:
        Scanner scanner = new Scanner(System.in): Cria um objeto Scanner para ler a entrada.
        int numUsers = scanner.nextInt(): Lê o número de usuários a serem cadastrados como inteiro.
        scanner.nextLine(): Consome a quebra de linha deixada pelo nextInt().
    Obtém a instância do UserManager usando UserManager.getInstance().
    Realiza um loop para cadastrar cada usuário:
        Lê o nome do usuário usando scanner.nextLine().
        Chama userManager.addUser(name) para adicionar o usuário à lista.
    Chama userManager.listUsers() para listar todos os usuários cadastrados.

Resumo:

Este código demonstra como criar um sistema de gerenciamento de usuários simples em Java. 
Ele utiliza o padrão Singleton para garantir que haja apenas uma instância do gerenciador 
e implementa funcionalidades básicas para adicionar e listar usuários.
 */
