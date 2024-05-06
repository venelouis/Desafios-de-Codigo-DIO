'''2 / 3 - Criando uma Lista de Equipamentos
Desafio:
Você foi designado para desenvolver um programa para gerenciar os equipamentos de uma empresa. 
O objetivo é criar um solução que permita aos usuários inserir informações sobre os equipamentos 
que serão cadastrados na rede, em seguida, exibir essa lista de equipamentos. 
Crie uma Lista para armazenar esses equipamentos e depois um loop para solicitar ao usuário 
inserir até três equipamentos.

Entrada:
O programa solicitará ao usuário que insira uma lista com três equipamentos para adicionar a rede.

Saída
Após a entrada dos itens, o programa exibirá a lista de equipamentos inseridos pelo usuário. 
Cada equipamento será listado com um prefixo ( - ) de marcação para melhor organização.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
Antena
Roteador
Switch

Saída:
Lista de Equipamentos:
- Antena
- Roteador
- Switch

Entrada:
Servidor
Cabinet Rack
Access Point

Saída:
Lista de Equipamentos:
- Servidor
- Cabinet Rack
- Access Point

Entrada:
Edge Routers
Patch Cord
UPS

Saída:
Lista de Equipamentos:
- Edge Routers
- Patch Cord
- UPS

# Providenciado pela DIO:
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:


# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")

'''

# Solução:

# Cria uma Lista 'itens' para armazenar os equipamentos:
itens = []

# Cria um loop para solicitar os itens ao usuário:
for i in range(3):
    # Solicita o item e armazena na variável "item":
    item = input()
    # Adiciona o item à lista "itens":
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")