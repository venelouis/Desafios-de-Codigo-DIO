'''
Desafios de Código Básicos - AWS Domínio 2
1 / 3 - Indicando a Categoria de Serviço em Nuvem

Descrição
Os serviços em nuvem são divididos em três categorias principais: Infraestrutura como Serviço (IaaS), Plataforma como Serviço (PaaS) e Software como Serviço (SaaS). Cada uma dessas categorias representa um nível diferente de abstração e controle sobre os recursos da nuvem.

Neste desafio, você será apresentado a uma série de afirmações e deverá escolher a categoria de serviço em nuvem mais apropriada para cada uma deles. Para isso, você deve complementar o código, inserindo como retorno o nome da categoria de serviço cuja afirmação está se referindo.

Entrada
A entrada consistirá em uma afirmação acerca de uma categoria de serviço em nuvem. Nesse contexto, as seguintes afirmações são consideradas válidas para este desafio de código:

"e o nivel mais baixo de abstracao"
"e o nivel intermediario de abstracao"
"e o nivel mais alto de abstracao"
"o cliente tem acesso direto aos recursos de computacao"
Saída
A saída esperada é a categoria de serviço em nuvem à qual se refere a afirmação fornecida como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"paas"
"saas"
"iaas"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
e o nivel mais baixo de abstracao	

Saída
iaas
'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber uma afirmação e retornar a categoria do serviço à qual se refere.
def escolher_categoria(afirmacao):
    if "nivel mais baixo de abstracao" in afirmacao:
        return "iaas"
        
    # TODO: Preencha corretamente a categoria de serviço indicada para cada afirmação, considerando as condições abaixo e Saídas possíveis:


    elif "nivel intermediario de abstracao" in afirmacao:
        return "paas"
        
    elif "nivel mais alto de abstracao" in afirmacao:
        return "saas"
        
    elif "acesso direto aos recursos de computacao" in afirmacao:
        return "iaas"
        
# Imprime a categoria do serviço referenciada na afirmação recebida na "entrada" através da função "escolher_categoria".
print(escolher_categoria(entrada))