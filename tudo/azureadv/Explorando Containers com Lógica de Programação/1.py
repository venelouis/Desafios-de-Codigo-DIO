'''
Descrição
Você foi encarregado de criar uma ferramenta automatizada para gerenciar volumes em Docker. A ferramenta deve interpretar comandos relacionados a volumes e gerar os comandos Docker correspondentes para criar, inspecionar e remover volumes. Por exemplo, se o comando for "criar" seguido do nome do volume, como my-vol, o programa deverá gerar o comando docker volume create my-vol.

Os comandos que você deve implementar são:

criar: para criar um novo volume Docker.
inspecionar: para inspecionar um volume existente.
remover: para remover um volume existente.
Sua missão é desenvolver um programa que leia a ação e o nome do volume como entrada e retorne o comando Docker apropriado.

Entrada
A entrada será uma string com dois valores separados por vírgula. O primeiro valor é o comando de ação, e o segundo valor é o nome do volume Docker.

Saída
O programa deve retornar o comando Docker correspondente à ação informada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
criar, my-vol	
remover, my-vol	
criar, data-volume

Saída
docker volume create my-vol
docker volume rm my-vol
docker volume create data-volume

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

'''

# Recebe a entrada do usuário
input_string = input()

def docker_command(input_string):
    # Separa a entrada em ação e nome do volume
    action, volume_name = input_string.split(", ")
    
    # COMPLETE AQUI: Mapeie as ações para comandos Docker correspondentes
    actions_to_commands = {
        "criar": "docker volume create",
        "inspecionar": "docker volume inspect",
        "remover": "docker volume rm"
    }
    
    # Verifica se a ação está mapeada e retorna o comando correspondente
    if action in actions_to_commands:
        return f"{actions_to_commands[action]} {volume_name}"

# Gera e exibe o comando Docker correspondente
print(docker_command(input_string))