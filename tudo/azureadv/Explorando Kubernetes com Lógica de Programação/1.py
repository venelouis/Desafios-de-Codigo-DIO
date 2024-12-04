'''
Descrição
Você foi encarregado de desenvolver uma ferramenta automatizada que recebe comandos de ação e nomes de Pods Kubernetes. Seu objetivo é interpretar esses comandos e gerar o comando kubectl correspondente. Por exemplo, se o comando for "listar", o programa deverá gerar o comando kubectl get pods.

O sistema deve interpretar as seguintes ações:

descrever: para descrever todos os Pods.
deletar: para deletar todos os Pods.
explicar: para obter a documentação de um recurso e seus campos.
listar: para listar todos os Pods em formato de saída ps.
Sua missão é desenvolver um programa que leia a ação como entrada e retorne o comando kubectl apropriado.

Saiba mais em: kubectl reference

Entrada
A entrada será uma string contendo apenas o comando de ação.

Saída
O programa deve retornar o comando kubectl correspondente à ação informada. Por exemplo, se o comando for "listar", o comando gerado será kubectl get pods.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
descrever
deletar
explicar

Saída
kubectl describe pods
kubectl delete pods --all
kubectl explain pods

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

'''

# Recebe a entrada do usuário
input_string = input()

def kubectl_command(input_string):
    # COMPLETE AQUI: Mapeie ações para comandos kubectl correspondentes
    actions_to_commands = {
        "descrever": "kubectl describe pods",
        "deletar": "kubectl delete pods --all",
        "explicar": "kubectl explain pods",
        "listar": "kubectl get pods"
    }
    
    # Verifica se a ação está mapeada e retorna o comando correspondente
    if input_string in actions_to_commands:
        return actions_to_commands[input_string]

# Gera e exibe o comando kubectl correspondente
print(kubectl_command(input_string))