'''1 / 3 - Verificador de Planos de Internet
Desafio
Uma empresa de telecomunicações deseja criar uma solução algorítmica que ajude aos seus clientes 
a escolherem o plano de internet ideal com base em seu consumo mensal de dados. 
Para a resolução, você pode solicitar ao usuário que insira o seu consumo, sendo este um valor 'float'. 
Crie uma função chamada recomendar_plano para receber o consumo médio mensal de dados informado 
pelo cliente, além de utilizar estruturas condicionais para fazer a verificação e retornar 
o plano adequado.

Planos Oferecidos:

- Plano Essencial Fibra - 50Mbps: Recomendado para um consumo médio de até 10 GB.
- Plano Prata Fibra - 100Mbps: Recomendado para um consumo médio acima de 10 GB até 20 GB.
- Plano Premium Fibra - 300Mbps: Recomendado para um consumo médio acima de 20 GB.

Entrada
Como entrada solicite o consumo médio mensal de dados em GB (float).

Saída
Retorne o plano ideal para o cliente de acordo com o consumo informado na entrada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
10

Plano Essencial Fibra - 50Mbps

19

Plano Prata Fibra - 100Mbps
21

Plano Premium Fibra - 300Mbps

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))
'''

# Solução:

# Cria a função recomendar_plano para receber o consumo médio mensal de dados informado pelo cliente:
def recomendar_plano(consumo):
    # Utiliza estruturas condicionais para fazer a verificação e retornar o plano adequado:
    if consumo <= 10:
        return 'Plano Essencial Fibra - 50Mbps'
    elif consumo > 10 and consumo <= 20:
        return 'Plano Prata Fibra - 100Mbps'
    else:
        return 'Plano Premium Fibra - 300Mbps'

# Solicita ao usuário que insira o consumo médio mensal de dados:    
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))