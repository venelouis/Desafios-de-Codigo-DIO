'''
Descrição
O Armazenamento de Blobs do Azure é um serviço de armazenamento de objetos altamente escalável e seguro, oferecido pela Microsoft Azure. Ele é projetado para armazenar grandes quantidades de dados não estruturados, como documentos, imagens, vídeos e backups. Neste desafio, você irá associar os conceitos fundamentais do Armazenamento de Blobs do Azure com suas respectivas definições. 

Não se preocupe com a linguagem de programação, com o tempo você vai perceber que ela é apenas um detalhe.

Saiba mais em Microsoft Learn: Azure Blob Storage.

Entrada
A entrada consistirá no conceito de Armazenamento de Blobs do Azure para o qual você deve retornar a descrição. Nesse contexto, os seguintes conceitos são considerados válidos para este desafio de código:

"Container"
"Storage Account"
"Access Tier"
"Blob"
Saída
A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"Unidade de armazenamento de dados no Azure"
"Conta que gerencia os serviços de armazenamento"
"Nível de acesso que define a frequência de acesso aos dados"
"Agrupamento de Blobs"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada
Access Tier	
Container
Storage Account	

Saída
Nível de acesso que define a frequência de acesso aos dados
Agrupamento de Blobs
Conta que gerencia os serviços de armazenamento



# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Access Tier":
        return "Nível de acesso que define a frequência de acesso aos dados"

    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:             
    elif conceito == "escreva aqui o conceito correspondente":
        return "Agrupamento de Blobs"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "Conta que gerencia os serviços de armazenamento"
        
    elif conceito == "escreva aqui o conceito correspondente":
        return "Unidade de armazenamento de dados no Azure"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))

'''


# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "Access Tier":
        return "Nível de acesso que define a frequência de acesso aos dados"

    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:             
    elif conceito == "Container":
        return "Agrupamento de Blobs"
        
    elif conceito == "Storage Account":
        return "Conta que gerencia os serviços de armazenamento"
        
    elif conceito == "Blob":
        return "Unidade de armazenamento de dados no Azure"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito". 
print(descrever_conceito(entrada))