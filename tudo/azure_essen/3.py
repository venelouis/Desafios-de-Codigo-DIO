'''
Explorando Arquitetura e Serviços Azure com Lógica de Programação
3 / 3 - Associando Recursos de Identidade, Acesso e Segurança

Descrição
No Microsoft Azure, identidade, acesso e segurança são fundamentais para proteger recursos e gerenciar quem tem acesso a eles. Seu desafio é criar um código que associe as ferramentas e serviços de identidade, acesso e segurança do Azure com suas respectivas descrições. O objetivo é identificar e mapear corretamente cada ferramenta para sua função principal na segurança e gerenciamento de identidades.

Entrada
A entrada para o desafio consiste em uma ferramenta ou serviço de identidade, acesso e segurança do Azure para o qual você deve retornar a descrição correspondente. Os seguintes serviços e ferramentas são válidos para este desafio:

"Microsoft Entra ID"
"Multi-Factor Authentication"
"Azure Role-Based Access Control"
"Azure Security Center"
"Azure Key Vault"
Saída
A saída esperada é a descrição associada ao serviço ou ferramenta fornecida como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

"Possibilita um gerenciamento de acesso refinado dos recursos"
"Permite armazenar e acessar segredos de maneira segura"
"Serviço de gerenciamento de identidades e acessos"
"Proporciona uma camada adicional de segurança"
"Oferece visibilidade e controle sobre a segurança dos recursos"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
Microsoft Entra ID	

Saída
Serviço de gerenciamento de identidades e acessos

'''

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber um serviço ou ferramenta e retornar sua respectiva descrição.
def associar_recurso(recurso):
	if recurso == "Azure Role-Based Access Control":
			return "Possibilita um gerenciamento de acesso refinado dos recursos"
			
	# TODO: Preencha corretamente a descrição de cada serviço ou ferramenta, considerando as condições abaixo e Saídas possíveis:		
	elif recurso == "Microsoft Entra ID":
	    return "Serviço de gerenciamento de identidades e acessos"
	    
	elif recurso == "Multi-Factor Authentication":
	    return "Proporciona uma camada adicional de segurança"
	    	    	
	elif recurso == "Azure Key Vault":
	    return "Permite armazenar e acessar segredos de maneira segura"
  
	elif recurso == "Azure Security Center":
			return "Oferece visibilidade e controle sobre a segurança dos recursos"


print(associar_recurso(entrada))
