'''
Descrição
Neste desafio, você deve associar as vantagens da Inteligência Artificial no Azure com suas respectivas definições. Cada vantagem possui uma descrição específica que você precisará identificar e retornar de acordo com a entrada fornecida. O objetivo é reforçar sua familiaridade com os principais benefícios da IA no Azure, independentemente da linguagem de programação escolhida.

Entrada
A entrada consistirá na vantagem da IA no Azure para a qual você deve retornar a descrição. Nesse contexto, as seguintes vantagens são consideradas válidas para este desafio de código:

"análise preditiva"
"processamento de linguagem natural"
"automação"
"personalização"
Saída
A saída esperada é a descrição associada à vantagem fornecida como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"automatização de tarefas repetitivas e processos"
"oferecer experiências personalizadas aos usuários"
"habilidade de entender e gerar linguagem humana"
"capacidade de prever tendências e comportamentos futuros"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
análise preditiva	
processamento de linguagem natural	
automação

Saída
capacidade de prever tendências e comportamentos futuros
habilidade de entender e gerar linguagem humana
automatização de tarefas repetitivas e processos
Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

'''

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "análise preditiva":
        return "capacidade de prever tendências e comportamentos futuros"
        
    # COMPLETE AQUI: Preencha corretamente cada vantagem, considerando as descrições abaixo:                
    elif vantagem == "processamento de linguagem natural":
        return "habilidade de entender e gerar linguagem humana"
        
    elif vantagem == "automação":
        return "automatização de tarefas repetitivas e processos"
        
    elif  vantagem == "personalização":
        return "oferecer experiências personalizadas aos usuários"

# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem". 
print(descrever_vantagem(entrada))