'''
Desafios de Código Básicos - AWS Domínio 1
1 - Benefícios da Arquitetura em Nuvem

Descrição
Agora que exploramos os benefícios da arquitetura em nuvem, incluindo economia de custos, infraestrutura global, alta disponibilidade, elasticidade e agilidade, é hora de consolidar nosso entendimento através da prática.

Para fortalecer seus conhecimentos, complete o código deste desafio, associando os benefícios da nuvem AWS com suas respectivas definições. Não se preocupe com a linguagem de programação, com o tempo você vai perceber que ela é apenas um detalhe. Portanto, aproveite esse momento para sair da sua zona de conforto e conhecer uma das linguagens suportadas pela nuvem AWS.

Entrada
A entrada consistirá na vantagem da arquitetura em nuvem para a qual você deve retornar a descrição. Nesse contexto, as seguintes vantagens são consideradas válidas para este desafio de código:

"economia de custos"
"infraestrutura global"
"alta disponibilidade"
"elasticidade"
"agilidade"
Saída
A saída esperada é a descrição associada à vantagem fornecida como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"garantia de que os recursos estejam sempre disponiveis"
"capacidade de dimensionar recursos conforme a demanda"
"otimizacao de gastos por meio de modelos de precos flexiveis"
"capacidade de desenvolver, testar e implantar rapidamente"
"fornecer recursos eficientemente em qualquer lugar do mundo"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
alta disponibilidade

elasticidade

agilidade

Saída
garantia de que os recursos estejam sempre disponiveis

capacidade de dimensionar recursos conforme a demanda

capacidade de desenvolver, testar e implantar rapidamente
'''
# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "economia de custos":
        return "otimizacao de gastos por meio de modelos de precos flexiveis"
        
    # TODO: Preencha corretamente a descrição de cada vantagem, considerando as condições abaixo e Saídas possíveis:
    
    elif vantagem == "infraestrutura global":
        return "fornecer recursos eficientemente em qualquer lugar do mundo"
        
    elif vantagem == "alta disponibilidade":
        return "garantia de que os recursos estejam sempre disponiveis"
        
    elif vantagem == "elasticidade":
        return "capacidade de dimensionar recursos conforme a demanda"
        
    elif  vantagem == "agilidade":
        return "capacidade de desenvolver, testar e implantar rapidamente"
 
# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem".
print(descrever_vantagem(entrada))