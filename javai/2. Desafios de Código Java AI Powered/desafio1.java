/*
Descrição
Implemente um sistema de registro de alunos que aplique o Princípio da Responsabilidade Única (SRP) 
do S.O.L.I.D. Neste contexto, você deve criar duas classes: Student e StudentRegistry. 
A classe Student será responsável apenas por armazenar informações relacionadas ao aluno (nome e ID), 
enquanto a classe StudentRegistry terá a única responsabilidade de gerenciar operações de registro, 
como adicionar e remover alunos.

Entrada
O programa deve receber a entrada do usuário contendo o nome e o ID do aluno, separados por vírgula.

Saída
O programa deve imprimir mensagens de sucesso ou erro, de acordo com as operações realizadas. 
Se um aluno for adicionado com sucesso, exiba a mensagem no formato: {student.name} added. 
Se o aluno já estiver registrado, a mensagem deve ser: Student already registered.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
Carlo, 931
Mariana, 456
Joao, 123

Saída:
Carlo adicionado.
Mariana adicionado.
Aluno ja registrado.
 */

// Solução:

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Aluno {
    private String nome;
    private String id;

    public Aluno(String nome, String id) {
        this.nome = nome;
        this.id = id;
    }

    public String getNome() {
        return nome;
    }

    public String getId() {
        return id;
    }
}

class RegistroAluno {
    private List<Aluno> alunosRegistrados;

    public RegistroAluno() {
        this.alunosRegistrados = new ArrayList<>();
        this.alunosRegistrados.add(new Aluno("João", "123"));
    }

    public String adicionarAluno(Aluno aluno) {
        if (alunoJaRegistrado(aluno)) {
            return "Aluno ja registrado.";
        } else {
            this.alunosRegistrados.add(aluno);
            return aluno.getNome() + " adicionado.";
        }
    }

    private boolean alunoJaRegistrado(Aluno aluno) {
        return alunosRegistrados.stream().anyMatch(a -> a.getId().equals(aluno.getId()));
    }
}

class MensagemHandler {
    public static void exibirMensagem(String mensagem) {
        System.out.println(mensagem);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        RegistroAluno registroAluno = new RegistroAluno();

        String input = scanner.nextLine();
        String[] dadosAluno = input.split(", ");
        Aluno aluno = new Aluno(dadosAluno[0], dadosAluno[1]);

        String mensagem = registroAluno.adicionarAluno(aluno);
        MensagemHandler.exibirMensagem(mensagem);

        scanner.close();
    }
}