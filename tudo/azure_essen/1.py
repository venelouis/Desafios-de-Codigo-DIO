'''
Explorando Arquitetura e Serviços Azure com Lógica de Programação
1 / 3 - Identificando os Componentes de Arquitetura do Azure

Descrição
No Microsoft Azure, a arquitetura é composta por diversos componentes que colaboram para construir soluções escaláveis e resilientes. Seu desafio é criar um código que associe cada componente de arquitetura do Azure com sua descrição correspondente. O objetivo é identificar e mapear corretamente os componentes para suas funções principais.

Entrada
A entrada para o desafio consiste em um componente de arquitetura do Azure para o qual você deve retornar a descrição correspondente. Os seguintes componentes são válidos para este desafio:

"Regiões do Azure"
"Zonas de Disponibilidade"
"Datacenters"
"Assinaturas"
"Grupos de Gerenciamento"
Saída
A saída esperada é a descrição associada ao componente fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

"Unidades de faturamento que agrupam recursos e serviços do Azure"
"Instalações físicas que abrigam servidores e outros recursos"
"Estruturas hierárquicas que gerenciam múltiplas assinaturas"
"Garante alta disponibilidade ao isolar falhas"
"Localizações geográficas onde os serviços são disponibilizados"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber um componente e retornar sua respectiva descrição.
def identificar_componente(componente):
	if componente == "Datacenters":
			return "Instalações físicas que abrigam servidores e outros recursos"
			
	# TODO: Preencha corretamente a descrição de cada componente, considerando as condições abaixo e Saídas possíveis:		
	elif componente == "Regiões do Azure":
	    return "Localizações geográficas onde os serviços são disponibilizados"
	    
	elif componente == "Assinaturas":
	    return "Unidades de faturamento que agrupam recursos e serviços do Azure"
	    	    	
	elif componente == "Zonas de Disponibilidade":
	    return "Garante alta disponibilidade ao isolar falhas"
	    
	elif componente == "Grupos de Gerenciamento":
	    return "Estruturas hierárquicas que gerenciam múltiplas assinaturas"	    


print(identificar_componente(entrada))