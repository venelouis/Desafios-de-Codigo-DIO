'''Associando Conceitos de IA com Lógica de Programação
1 / 3 - Associando os Conceitos de IA
XP 50258/53270
NÍVEL 22
5/5
 Básico
 Princípios Básicos
Descrição
Para fortalecer seus conhecimentos, complete o código deste desafio, associando os conceitos de IA com suas respectivas definições. Não se preocupe com a linguagem de programação, com o tempo você vai perceber que ela é apenas um detalhe. Portanto, aproveite esse momento para sair da sua zona de conforto e conhecer uma das linguagens suportadas pela IA.

Entrada
A entrada consistirá no conceito de IA para o qual você deve retornar a descrição. Nesse contexto, os seguintes conceitos são considerados válidos para este desafio de código:

"aprendizado supervisionado"
"aprendizado não supervisionado"
"redes neurais"
"processamento de linguagem natural"
Saída
A saída esperada é a descrição associada ao conceito fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"análise e geração de linguagem humana"
"sistemas inspirados no cérebro humano para processamento de dados"
"descoberta de padrões em dados não rotulados"
"treinamento de modelos com dados rotulados"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
aprendizado supervisionado	
aprendizado não supervisionado
redes neurais

Saída
treinamento de modelos com dados rotulados
descoberta de padrões em dados não rotulados
sistemas inspirados no cérebro humano para processamento de dados

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

'''

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "aprendizado supervisionado":
        return "treinamento de modelos com dados rotulados"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:        
    elif conceito == "aprendizado não supervisionado":
        return "descoberta de padrões em dados não rotulados"
        
    elif conceito == "redes neurais":
        return "sistemas inspirados no cérebro humano para processamento de dados"
        
    elif conceito == "processamento de linguagem natural":
        return "análise e geração de linguagem humana"
 
# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".
print(descrever_conceito(entrada))