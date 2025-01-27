'''
Associando Conceitos de Armazenamento e Banco de Dados no Azure
1 / 3 - Explorando Armazenamento e Banco de Dados no Azure

Descrição
O Azure oferece uma variedade de serviços de armazenamento e banco de dados para atender às necessidades de diferentes tipos de aplicações. Esses serviços são projetados para fornecer alta disponibilidade, escalabilidade e segurança. Neste desafio, você irá associar os conceitos fundamentais de Armazenamento e Banco de Dados no Azure com suas respectivas definições.

Não se preocupe com a linguagem de programação, com o tempo você vai perceber que ela é apenas um detalhe.

Saiba mais em Microsoft Learn: Azure Blob Storage, Azure SQL Database, Azure Table Storage, Azure Cosmos DB.

Entrada
A entrada consistirá no conceito de Armazenamento e Banco de Dados no Azure para o qual você deve retornar a descrição. Nesse contexto, os seguintes conceitos são considerados válidos para este desafio de código:

"Azure Blob Storage"
"Azure SQL Database"
"Azure Table Storage"
"Azure Cosmos DB"
Saída
A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"Serviço de armazenamento de dados NoSQL baseado em tabelas"
"Banco de dados NoSQL distribuído globalmente"
"Banco de dados relacional gerenciado"
"Serviço de armazenamento de objetos para dados não estruturados"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada
Azure Blob Storage	

Azure SQL Database	

Azure Table Storage	

Saída
Serviço de armazenamento de objetos para dados não estruturados

Banco de dados relacional gerenciado

Serviço de armazenamento de dados NoSQL baseado em tabelas


Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
  if conceito == "Azure Blob Storage":
    return "Serviço de armazenamento de objetos para dados não estruturados"

# COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo: 
  elif conceito == "escreva aqui o conceito correspondente":
    return "Banco de dados NoSQL distribuído globalmente"

  elif conceito == "escreva aqui o conceito correspondente":
    return "Serviço de armazenamento de dados NoSQL baseado em tabelas"

  elif conceito == "escreva aqui o conceito correspondente":
    return "Banco de dados relacional gerenciado"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))

'''

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
  if conceito == "Azure Blob Storage":
    return "Serviço de armazenamento de objetos para dados não estruturados"

# COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo: 
  elif conceito == "Azure Cosmos DB":
    return "Banco de dados NoSQL distribuído globalmente"

  elif conceito == "Azure Table Storage":
    return "Serviço de armazenamento de dados NoSQL baseado em tabelas"

  elif conceito == "Azure SQL Database":
    return "Banco de dados relacional gerenciado"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))