'''
Descrição
Você foi encarregado de desenvolver uma ferramenta automatizada que recebe comandos de ação e nomes de imagens ou containers Docker. Seu objetivo é interpretar esses comandos e gerar o comando Docker correspondente. Por exemplo, se o comando for "baixar" seguido de um nome de imagem, como ubuntu, o programa deverá gerar o comando docker pull ubuntu.

O sistema deve interpretar mais ações, como:

baixar: para baixar uma imagem Docker.
executar: para executar uma imagem Docker.
parar: para interromper um container em execução.
remover: para remover um container existente.
Sua missão é desenvolver um programa que leia a ação e o nome da imagem/container como entrada e retorne o comando Docker apropriado.

Entrada
A entrada será uma string com dois valores separados por vírgula. O primeiro valor é o comando de ação, e o segundo valor é o nome da imagem ou container Docker.

Saída
O programa deve retornar o comando Docker correspondente à ação informada. Por exemplo, se o comando for "executar", seguido da imagem ubuntu, o comando gerado será docker run ubuntu.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
baixar, ubuntu	
executar, nginx	
parar, my_container	

Saída
docker pull ubuntu
docker run nginx
docker stop my_container

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

'''

# Recebe a entrada do usuário
input_string = input()

def docker_command(input_string):
    # Separa a entrada em ação e nome da imagem/container
    action, name = input_string.split(", ")
    
    # COMPLETE AQUI: Mapeie ações para comandos Docker correspondentes
    actions_to_commands = {
        "baixar": "docker pull",
        "executar": "docker run",
        "parar": "docker stop",
        "remover": "docker rm"
    }
    
    # Verifica se a ação está mapeada e retornar o comando correspondente
    if action in actions_to_commands:
        return f"{actions_to_commands[action]} {name}"

# Gera e exibir o comando Docker correspondente
print(docker_command(input_string))