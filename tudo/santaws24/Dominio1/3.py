'''
Desafios de Código Básicos - AWS Domínio 1
3 / 3 - Escolhendo a Estratégia de Migração

Descrição
A migração para a nuvem é uma etapa crucial para muitas organizações que buscam aumentar sua eficiência operacional e reduzir custos. A AWS oferece diversas estratégias de migração baseadas nas melhores práticas e experiências de seus clientes. Para garantir o sucesso da migração, é essencial escolher a estratégia correta para cada aplicativo ou sistema. Neste desafio, você será apresentado a uma série de cenários de migração, e seu objetivo é identificar a estratégia de migração mais adequada para cada um deles

Para exercitar os seus conhecimentos, complete o código deste desafio, associando o cenário recebido com a estratégia de migração mais adequada, dentre as Sete Estratégias de Migração para a Nuvem (as 7 Rs). Não precisa se preocupar com a linguagem de programação, com o tempo você vai notar que isso é apenas um detalhe. Assim, aproveite para sair um pouco da sua zona de conforto e experimentar uma das linguagens suportadas pela AWS na nuvem.

Entrada
A entrada consistirá em um cenário de migração, descrevendo brevemente o aplicativo ou sistema a ser migrado. Nesse contexto, os seguintes cenários são considerados válidos para este desafio de código:

"transicao de aplicativo sem valor comercial"
"aplicativo com necessidade de adiar sua migracao para a nuvem"
"substituir o aplicativo por uma versao ou produto diferente"
"modificar a arquitetura do aplicativo"
"mover aplicativos para a nuvem sem modifica-los"
"introduzir otimizacoes no aplicativo para opera-lo de forma eficiente"
"transferir servidores ou instancias para outra plataforma na nuvem"
Saída
A saída esperada é a estratégia de migração mais apropriada para o cenário fornecido como entrada, escolhida entre as 7 Rs. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"relocate"
"retire"
"refactor or re-architect"
"retain"
"repurchase"
"rehost"
"replatform"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada
transicao de aplicativo sem valor comercial

aplicativo com necessidade de adiar sua migracao para a nuvem

substituir o aplicativo por uma versao ou produto diferente

Saída
retire

retain

repurchase
'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um cenário e retornar a estratégia indicada.
def escolher_estrategia(cenario):
    if "aplicativo a ser descomissionado" in cenario or "sem valor comercial" in cenario:
        return "retire"
        
    # TODO: Preencha corretamente a estrátegia indicada para cada cenário, considerando as condições abaixo e Saídas possíveis:

    elif "manter aplicativos no ambiente de origem" in cenario or "adiar sua migracao para a nuvem" in cenario:
        return "retain"
        
    elif "mover aplicativos para a nuvem sem modifica-los" in cenario or "lift and shift" in cenario:
        return "rehost"
        
    elif "transferir servidores ou instancias para outra plataforma na nuvem" in cenario:
        return "replatform"
        
    elif "substituir o aplicativo por uma versao ou produto diferente" in cenario:
        return "repurchase"
        
    elif "mover o aplicativo para a nuvem" in cenario or "introduzir otimizacoes para opera-lo de forma eficiente" in cenario:
        return "relocate"
        
    elif "modificar a arquitetura do aplicativo" in cenario or "aproveitar os recursos nativos para melhorar agilidade" in cenario:
        return "refactor or re-architect"
        
# Imprime a estratégia indicada para o cenário recebido na "entrada" através da função "escolher_estrategia".
print(escolher_estrategia(entrada))