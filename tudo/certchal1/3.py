'''
Descrição
Neste desafio, seu objetivo é associar corretamente os serviços de Inteligência Artificial do Azure com suas descrições específicas. Cada serviço oferece uma funcionalidade distinta, e sua tarefa será identificar o serviço correspondente à descrição fornecida na entrada. Este desafio foi criado para aprimorar seus conhecimentos sobre os recursos de IA do Azure, sem focar em uma linguagem de programação específica.

Saiba mais em: Serviços de IA do Azure

Entrada
A entrada consistirá no serviço de IA no Azure para o qual você deve retornar a descrição. Nesse contexto, os seguintes serviços são considerados válidos para este desafio de código:

"Azure Machine Learning"
"Azure OpenAI Service"
"Azure AI Vision"
"Azure Bot Services"
Saída
A saída esperada é a descrição associada ao serviço fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"análise e interpretação de imagens e vídeos"
"criação e gerenciamento de bots inteligentes"
"plataforma para construir, treinar e implantar modelos de ml"
"integração de modelos avançados de linguagem da OpenAI"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
Azure Machine Learning
Azure Bot Services
Azure OpenAI Service

Saída
plataforma para construir, treinar e implantar modelos de ml
criação e gerenciamento de bots inteligentes
integração de modelos avançados de linguagem da OpenAI

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.
'''

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um serviço e retornar sua respectiva descrição.
def descrever_servico(servico):
    if servico == "Azure Cognitive Services":
        return "serviços pré-construídos para visão, fala, linguagem e tomada de decisão"
        
    # COMPLETE AQUI: Preencha corretamente cada serviço, considerando as descrições abaixo:                        
    elif servico == "Azure Machine Learning":
        return "plataforma para construir, treinar e implantar modelos de ml"
        
    elif servico == "Azure Bot Services":
        return "criação e gerenciamento de bots inteligentes"
        
    elif servico == "Azure OpenAI Service":
        return "integração de modelos avançados de linguagem da OpenAI"
        
    elif  servico == "Azure AI Vision":
        return "análise e interpretação de imagens e vídeos"
        
# Imprime a descrição do serviço recebido na "entrada" através da função "descrever_servico". 
print(descrever_servico(entrada))