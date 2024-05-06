/*
Desafios de Código Java Intermediários: S.O.L.I.D
2 / 5 - Sistema de Notificações

Descrição:
Desenvolva uma simulação de um sistema de notificações que utilize o Princípio de Segregação de Interface 
(ISP) em seu desenvolvimento, criando interfaces separadas para diferentes tipos de notificações, 
como EmailNotification e SMSNotification.

Entrada:
O programa receberá dois parâmetros de entrada: o tipo de notificação (string) - email ou sms, 
e a mensagem (string) a ser enviada.

Saída:
O programa deve imprimir uma confirmação da notificação enviada (string): {tipo} enviado: {mensagem}.

Se o tipo de notificação não for válido, a mensagem de retorno deve ser: Tipo de notificação inválido.

Exemplos:
Entrada:
email, Ola Mundo!
sms, Bem-Vindo.
fax, Rua Dominick

Saída:
Email enviado: Ola Mundo!
SMS enviado: Bem-Vindo.
Tipo de notificação inválido.

5. Observações:
Aplique o Princípio de Segregação de Interface (ISP) criando interfaces específicas para 
cada tipo de notificação.
Considere a possibilidade de criar exceções ou tratamentos adequados para casos em que 
ocorram tipos de notificação inválidos.
 */

 import java.util.Scanner;

interface Notificacao {
  void enviar(String mensagem);
}

class NotificacaoEmailImpl implements Notificacao {
  @Override
  public void enviar(String mensagem) {
    System.out.println("Email enviado: %s".formatted(mensagem));
  }
}

class NotificacaoSMSImpl implements Notificacao {
  @Override
  public void enviar(String mensagem) {
    System.out.println("SMS enviado: %s".formatted(mensagem));
  }
}

public class Principal {
  public static void main(String[] args) {
    try(Scanner scanner = new Scanner(System.in)) {
      String[] entradas = scanner.nextLine().split(", ");
  
      String tipoNotificacao = entradas[0];
      String mensagem = entradas[1];
  
      Notificacao notificacao;
      switch (tipoNotificacao) {
        case "email":
          notificacao = new NotificacaoEmailImpl();
          break;
        case "sms":
          notificacao = new NotificacaoSMSImpl();
          break;
        default:
          System.out.println("Tipo de notificacao invalido.");
          return;
      }
      notificacao.enviar(mensagem);
    }
  }
}