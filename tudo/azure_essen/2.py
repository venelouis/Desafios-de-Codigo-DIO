'''
Explorando Arquitetura e Serviços Azure com Lógica de Programação
2 / 3 - Explorando os Serviços de Armazenamento do Azure

Descrição
O armazenamento na Microsoft Azure oferece uma variedade de serviços para atender diferentes necessidades. Seu desafio é criar um código que associe os serviços de armazenamento do Azure com suas respectivas descrições. O objetivo é mapear cada serviço de armazenamento para a sua funcionalidade principal, conforme fornecido.

Entrada
A entrada para o desafio consiste em um serviço de armazenamento do Azure para o qual você deve retornar a descrição correspondente. Os seguintes tipos de armazenamento são válidos para este desafio:

"Blob do Azure"
"Disco do Azure"
"Fila do Azure"
"Arquivos do Azure"
"Tabelas do Azure"
Saída
A saída esperada é a descrição associada ao serviço de armazenamento fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

"Armazenamento de dados estruturados não relacionais em tabelas"
"Armazenamento de alto desempenho para máquinas virtuais"
"Armazenamento de arquivos compartilhados acessíveis por meio de SMB”
"Armazenamento de mensagens para comunicação entre aplicações"
"Armazenamento de arquivos grandes e não estruturados"
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	
Blob do Azure	

Saída
Armazenamento de arquivos grandes e não estruturados
'''

# Solução:

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()


# Função responsável por receber um serviço de armazenamento e retornar sua respectiva descrição.
def identificar_servico_armazenamento(servico):
	if servico == "Arquivos do Azure":
			return "Armazenamento de arquivos compartilhados acessíveis por meio de SMB"
			
	# TODO: Preencha o serviço de acordo com a descrição, considerando as condições abaixo e Saídas possíveis:		
	elif servico == "Blob do Azure":
	    return "Armazenamento de arquivos grandes e não estruturados"
	    
	elif servico == "Fila do Azure":
	    return "Armazenamento de mensagens para comunicação entre aplicações"
	    	    	
	elif servico == "Tabelas do Azure":
	    return "Armazenamento de dados estruturados não relacionais em tabelas"
	    
	elif servico == "Disco do Azure":
	    return "Armazenamento de alto desempenho para máquinas virtuais"
	    
print(identificar_servico_armazenamento(entrada))