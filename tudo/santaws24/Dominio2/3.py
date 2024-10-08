'''
Desafios de Código Básicos - AWS Domínio 2
3 / 3 - Grupos de Segurança vs ACLs de Rede

Descrição
Neste desafio, você explorará os conceitos de grupos de segurança e ACLs (Listas de Controle de Acesso) de rede em serviços de nuvem. Grupos de segurança e ACLs de rede são ferramentas essenciais para controlar o tráfego de rede em ambientes em nuvem, mas cada um tem sua função específica e utilizações apropriadas. Os grupos de segurança são aplicados em nível de instância, enquanto as ACLs são aplicadas em nível de sub-rede.

Você será apresentado a uma série de cenários relacionados a requisitos de segurança e controle de acesso em uma infraestrutura em nuvem. Com base nessas situações, você deve completar o código deste desafio indicando se é mais apropriado usar um grupo de segurança ou uma ACL de rede para atender aos requisitos.

Entrada
A entrada consistirá em descrições de cenários que envolvem requisitos de segurança e controle de acesso em uma infraestrutura em nuvem. Os seguintes cenários são considerados válidos para este desafio de código:

"uma aplicacao precisa permitir o trafego apenas na porta 80"
"uma sub-rede precisa bloquear todo o trafego de entrada"
"bloquear trafego externo para instancias em uma sub-rede privada"
"permitir acesso SSH a uma instancia somente para um endereço IP"
Saída
A saída esperada é indicar se um grupo de segurança ou uma ACL de rede seria mais adequado para cada cenário apresentado. Seguem as saídas possíveis, para que você possa analisar e associar corretamente considerando o template de código deste desafio:

"grupo de seguranca"
"ACL de rede"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
uma aplicacao precisa permitir o trafego apenas na porta 80	

Saída
grupo de seguranca
'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função encarregada de receber um cenário e retornar se é mais apropriado usar um grupo de segurança ou uma ACL.
def determinar_mecanismo_controle(cenario):
    if "uma aplicacao precisa permitir o trafego apenas na porta 80" in cenario:
        return "grupo de seguranca"
        
    # TODO: Preencha corretamente, considerando as condições abaixo e Saídas possíveis:
        
    elif "uma sub-rede precisa bloquear todo o trafego de entrada" in cenario:
        return "ACL de rede"
        
    elif "bloquear trafego externo para instancias em uma sub-rede privada" in cenario:
        return "ACL de rede"
        
    elif "permitir acesso SSH a uma instancia somente para um endereço IP" in cenario:
        return "grupo de seguranca"
        
# Imprime o mecanismo de controle indicado para o cenário fornecido na "entrada" através da função "determinar_mecanismo_controle".
print(determinar_mecanismo_controle(entrada))