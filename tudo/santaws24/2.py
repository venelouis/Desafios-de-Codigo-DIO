'''
Desafios de Código Básicos - AWS Domínio 1
2 / 3 - Os Pilares do AWS Well-Architected Framework

Descrição
Agora que você já conhece os seis pilares do AWS Well-Architected Framework, sendo eles: Excelência operacional, Segurança, Confiabilidade, Eficiência de performance, Otimização de custos e Sustentabilidade, chegou a hora de colocar em prática os conceitos aprendidos.

Para reforçar os seus conhecimentos, complete o código deste desafio, associando o pilar do AWS Well-Architected Framework com suas respectivas descrições. Não se preocupe com a linguagem de programação, com o tempo você vai perceber que ela é apenas um detalhe. Então, aproveite para sair da sua zona de conforto e experimentar uma das linguagens suportadas pela AWS na nuvem.

Entrada
A entrada consistirá no pilar do AWS Well-Architected Framework para o qual você deve retornar a descrição. Nesse contexto, os seguintes pilares são considerados válidos para este desafio de código:

"excelencia operacional"
"seguranca"
"confiabilidade"
"eficiencia de performance"
"otimizacao de custos"
"sustentabilidade"
Saída
A saída esperada é a descrição associada ao pilar fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"capacidade dos sistemas de executar as funcoes pretendidas"
"execucao e monitoramento de sistemas e melhoria continua"
"reducao do impacto ambiental dos sistemas na nuvem"
"protecao de informacoes e sistemas"
"alocacao eficaz e otimizada de recursos de TI e computacao"
"obtencao do melhor retorno sobre o investimento em recursos"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada
seguranca

confiabilidade

excelencia operacional

Saída
protecao de informacoes e sistemas

capacidade dos sistemas de executar as funcoes pretendidas

execucao e monitoramento de sistemas e melhoria continua
'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um pilar e retornar sua respectiva descrição.
def descrever_pilar(pilar):
    if pilar == "excelencia operacional":
        return "execucao e monitoramento de sistemas e melhoria continua"
        
    # TODO: Preencha corretamente a descrição de cada pilar, considerando as condições abaixo e Saídas possíveis:
    
    elif pilar == "seguranca":
        return "protecao de informacoes e sistemas"
        
    elif pilar == "confiabilidade":
        return "capacidade dos sistemas de executar as funcoes pretendidas"
        
    elif pilar == "eficiencia de performance":
        return "alocacao eficaz e otimizada de recursos de TI e computacao"
        
    elif pilar == "otimizacao de custos":
        return "obtencao do melhor retorno sobre o investimento em recursos"
        
    elif pilar == "sustentabilidade":
        return "reducao do impacto ambiental dos sistemas na nuvem"
 
# Imprime a descrição do pilar recebido na "entrada" através da função "descrever_pilar".
print(descrever_pilar(entrada))