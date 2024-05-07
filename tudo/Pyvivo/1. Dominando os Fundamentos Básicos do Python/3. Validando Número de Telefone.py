'''3 / 3 - Validando Número de Telefone
Desafio:
Imagine que você trabalha para uma empresa de telecomunicações 
e é responsável por validar se um número de telefone fornecido pelo cliente está em um formato correto. 
Para garantir a precisão dos registros, é essencial que os números de telefone estejam no formato padrão. 
Desenvolva uma função programa que valide se um número de telefone tem o formato correto.

Formato esperado:
O formato aceito para números de telefone é: (XX) 9XXXX-XXXX, onde X representa um dígito de 0 a 9. 
Lembre-se de respeitar os espaços entre os números quando preciso.

Entrada:
Uma string representando o número de telefone.

Saída:
Uma mensagem indicando se o número de telefone é válido ou inválido.

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
(88) 98888-8888

Saída:
Número de telefone válido.

Entrada:
(11)91111-1111	

Saída:
Número de telefone inválido.

Entrada:
225555-555

Saída:
Número de telefone inválido.

# Providenciado pela DIO:
# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


 # TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
   
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
   
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
       
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.

# Imprime o resultado:
print(result)
'''

# Solução:

# Módulo 're' que fornece operações com expressões regulares.
import re

# Cria uma função chamada 'validate_numero_telefone' que aceita um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    # Define um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = re.compile(r'^\(\d{2}\) 9\d{4}-\d{4}$')
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
        # Agora cria um return, para retornar que o número de telefone é válido:
        return 'Número de telefone válido.'
    # Cria um else e return, caso não o número de telefone seja inválido:
    else:
        return 'Número de telefone inválido.'
    
# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()

# Chama a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazena o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)