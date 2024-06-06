'''3 / 3 - Selecionando um Modelo Amazon Bedrock Ideal
Descrição:
Você foi contratado para desenvolver uma lista de dicionários chamado modelos_disponiveis 
contendo os modelos de inteligência artificial (IA) da Amazon Bedrock, 
dentro da lista crie três dicionários, sendo, nome, pontuacao_desempenho e preco_mensal, 
cada um deles representa um modelo disponível para recomendação e suas características.

Em seguida crie uma função chamada recomendar_modelo e receba dois parâmetros que será modelos 
e orçamento, que representa uma lista de modelos e o orçamento do usuário em unidades monetárias. 
Dentro da função recomendar_modelo verifique se o orçamento fornecido é suficiente para recomendar 
algum modelo. Se o orçamento for inferior a 250 unidades monetárias, 
a função retorna uma tupla com dois elementos:

1. "None": indicando que nenhum modelo pode ser recomendado.
2. Uma mensagem de aviso informando que o orçamento é muito baixo para recomendar um modelo adequado..

O objetivo geral do desafio é selecionar o melhor modelo que é escolhido com base no orçamento, 
priorizando modelos com preço mais próximo ao orçamento fornecido pelo usuário.

Detalhes dos Modelos:
- Modelo: Claude 3 Opus. Desempenho: 9. Preço mensal: $ 600;
- Modelo: Claude 3 Sonnet. Desempenho: 8. Preço mensal: $ 450;
- Modelo: Claude 3 Haiku. Desempenho: 7. Preço mensal: $ 350;

Atenção:
Alguns dados que utilizados são simulados e podem não representar situações reais.

Entrada:
O usuário deve fornecer os detalhes seu orçamento para que seja avaliado o melhor modelo com base 
no seu orçamento pelo preço mensal e desempenho.

Saída:
Com base nos modelos fornecidos e no orçamento especificado, 
a função deve recomendar o modelo adequado conforme o seu orçamento. 
O melhor modelo sugerido deve ser escolhido com base no orçamento, 
priorizando modelos com preço mais próximo ao orçamento fornecido pelo usuário. 
Caso o orçamento seja menor do que 250, retorne uma mensagem informando: 
"Se orçamento é muito baixo para recomendar um modelo adequado."

Exemplos:
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. 
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada:
300	

Saída:
Claude 3 Haiku. Este modelo está mais próximo do seu orçamento.

Entrada:
700	

Saída:
Claude 3 Opus. Melhor desempenho dentro do seu orçamento.

Entrada:
550	

Saída:
Claude 3 Sonnet. Melhor desempenho dentro do seu orçamento.

Entrada:
249	

Saída:
Seu orçamento é muito baixo para recomendar um modelo adequado.
'''


# TODO: Crie uma lista de dicionários representando os três modelos do Amazon Bedrock, com 'nome', 'pontuacao_desempenho' e 'preco_mensal' :
modelos_disponiveis = [
  {'nome': 'Claude 3 Opus', 'pontuacao_desempenho': 9, 'preco_mensal': 600.00},
  {'nome': 'Claude 3 Sonnet', 'pontuacao_desempenho': 8, 'preco_mensal': 450.00},
  {'nome': 'Claude 3 Haiku', 'pontuacao_desempenho': 7, 'preco_mensal': 350.00}
]

# TODO: Defina a função 'recomendar_modelo' e seus dois parâmetros 'modelos' e 'orcamento':

def recomendar_modelo(modelos, orcamento):
  """
  Recomenda um modelo de acordo com o orçamento e desempenho.

  Args:
    modelos (list): Lista de dicionários, cada um representando um modelo com 'nome', 'pontuacao_desempenho' e 'preco_mensal'.
    orcamento (float): Orçamento do usuário.

  Returns:
    tuple: Um tupla contendo o nome do modelo recomendado e uma string explicando o motivo da recomendação.
  """

# TODO: Verifique se o orçamento fornecido é suficiente. Se o orçamento for inferior a 250, implemente a resposta adequada:
  
  if orcamento < 250:
    return None, "Seu orçamento é muito baixo para recomendar um modelo adequado."  
    return None, "TODO"

  modelos_dentro_orcamento = [modelo for modelo in modelos if modelo['preco_mensal'] <= orcamento]

  # Caso nenhum modelo esteja dentro do orçamento
  if not modelos_dentro_orcamento:
    modelo_mais_proximo = min(modelos, key=lambda x: abs(x['preco_mensal'] - orcamento))
    return modelo_mais_proximo['nome'], "Este modelo está mais próximo do seu orçamento."

  # Caso todos os modelos estejam dentro do orçamento
  melhor_modelo = max(modelos_dentro_orcamento, key=lambda x: x['pontuacao_desempenho'])
  return melhor_modelo['nome'], "Melhor desempenho dentro do seu orçamento."

# Solicitar orçamento do usuário
orcamento_usuario = float(input())

# Chamada da função para recomendar o modelo
modelo_recomendado, motivo = recomendar_modelo(modelos_disponiveis, orcamento_usuario)

# Saída da recomendação
if modelo_recomendado:
  print(modelo_recomendado + ". " + motivo)
else:
  print(motivo)