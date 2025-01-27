'''
3 / 3 - Explorando o Azure Cosmos DB
Descrição
O Azure Cosmos DB é um serviço de banco de dados NoSQL distribuído globalmente, oferecido pela Microsoft Azure. Ele é projetado para fornecer alta disponibilidade, baixa latência e escalabilidade automática para aplicativos modernos. Neste desafio, você irá associar os conceitos fundamentais do Azure Cosmos DB com suas respectivas definições. 

Não se preocupe com a linguagem de programação, com o tempo você vai perceber que ela é apenas um detalhe.

Saiba mais em Microsoft Learn: Azure Cosmos DB.

Entrada
A entrada consistirá no conceito de Azure Cosmos DB para o qual você deve retornar a descrição. Nesse contexto, os seguintes conceitos são considerados válidos para este desafio de código:

"Throughput"
"Database"
"Partition Key"
"Container"
Saída
A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"Unidade de armazenamento e execução de consultas no Cosmos DB"
"Chave usada para distribuir dados entre partições"
"Agrupa contêineres com throughput compartilhado ou dedicado"
"Mede a capacidade de processamento em RUs"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
Throughput	
Database
Partition Key

Saída
Mede a capacidade de processamento em RUs
Agrupa contêineres com throughput compartilhado ou dedicado
Chave usada para distribuir dados entre partições

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Throughput":
        return "Mede a capacidade de processamento em RUs"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:               
    elif conceito == "escreva aqui o conceito correspondente":
        return "Agrupa contêineres com throughput compartilhado ou dedicado"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "Chave usada para distribuir dados entre partições"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "Unidade de armazenamento e execução de consultas no Cosmos DB"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))

'''

# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Throughput":
        return "Mede a capacidade de processamento em RUs"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:               
    elif conceito == "Database":
        return "Agrupa contêineres com throughput compartilhado ou dedicado"
        
    elif conceito == "Partition Key":
        return "Chave usada para distribuir dados entre partições"
        
    elif conceito == "Container":
        return "Unidade de armazenamento e execução de consultas no Cosmos DB"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))