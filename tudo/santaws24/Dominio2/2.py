'''
Desafios de Código Básicos - AWS Domínio 2
2 / 3 - Identificando Responsabilidades: AWS e Cliente na Segurança da Nuvem

Descrição
A segurança é um aspecto crucial ao lidar com serviços em nuvem, e entender a diferença entre Segurança da Nuvem e Segurança na Nuvem é fundamental para garantir uma estratégia eficaz de proteção de dados e recursos.

Neste desafio, você receberá uma lista de responsabilidades e deverá determinar se são atribuídas à AWS ou ao cliente. Para isso, é necessário completar o código, indicando de quem é a responsabilidade correspondente.

Entrada
As entradas para este desafio serão responsabilidades relacionadas à segurança. As seguintes descrições são consideradas válidas para este desafio de código:

"seguranca da nuvem"
"seguranca na nuvem"
"garantir que os dados estejam em conformidade com as leis"
"proteger a infraestrutura que executa todos os servicos;
Saída
A saída esperada é a distinção entre segurança da nuvem e segurança na nuvem para cada descrição fornecida como entrada. Seguem as saídas possíveis, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"AWS"
"cliente"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
seguranca da nuvem	

Saída
AWS

'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função encarregada de receber uma responsabilidade e retornar o responsável por ela.
def indicar_responsavel(responsabilidade):
    if "seguranca da nuvem" in responsabilidade:
        return "AWS"
    elif "seguranca na nuvem" in responsabilidade:
        return "cliente"
        
    elif "garantir que os dados estejam em conformidade com as leis" in responsabilidade:
        return "cliente"
        
    elif "proteger a infraestrutura que executa todos os servicos" in responsabilidade:
        return "AWS"
        
# Imprime o responsável pela responsabilidade recebida na "entrada" através da função "indicar_responsavel".
print(indicar_responsavel(entrada))