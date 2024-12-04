'''Descrição
Você foi encarregado de desenvolver uma ferramenta automatizada para gerar comandos kubectl relacionados à persistência de dados em clusters Kubernetes. A ferramenta deverá interpretar ações específicas e gerar o comando correspondente para manipulação de PersistentVolumes (PV) e PersistentVolumeClaims (PVC).

Saiba mais em: kubectl reference

O sistema deve interpretar as seguintes ações:

criar-pv: para criar um PersistentVolume a partir de um arquivo YAML.
deletar-pv: para deletar um PersistentVolume existente.
criar-pvc: para criar um PersistentVolumeClaim a partir de um arquivo YAML.
deletar-pvc: para deletar um PersistentVolumeClaim existente.
Sua missão é desenvolver um programa que leia a ação e o nome do arquivo YAML (para criação de PV ou PVC) ou o nome do recurso (para deleção de PV ou PVC), e retorne o comando kubectl apropriado.

Entrada
A entrada será uma string com dois valores separados por vírgula. O primeiro valor é o comando de ação (criar ou deletar) e o segundo valor é o nome do arquivo YAML (para criação) ou o nome do PersistentVolume (PV) ou PersistentVolumeClaim (PVC) (para deleção).

Saída
O programa deve retornar o comando kubectl correspondente à ação informada. Por exemplo, se o comando for "criar-pv" seguido do arquivo pv.yaml, o comando gerado será kubectl create -f pv.yaml.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada
criar-pv, pv.yaml
deletar-pv, my-volume
criar-pvc, pvc.yaml

Saída
kubectl create -f pv.yaml
kubectl delete pv my-volume
kubectl create -f pvc.yaml
'''

# Recebe a entrada do usuário
input_string = input()

def kubectl_command(input_string):
    # Separa a entrada em ação e nome do volume ou claim
    action, resource_name = input_string.split(", ")
    
    # COMPLETE AQUI: Mapeie ações para comandos kubectl correspondentes
    actions_to_commands = {
        "criar-pv": "kubectl create -f",
        "deletar-pv": "kubectl delete pv",
        "criar-pvc": "kubectl create -f",
        "deletar-pvc": "kubectl delete pvc"
    }
    
    # Verifica se a ação está mapeada e retorna o comando correspondente
    if action in actions_to_commands:
        return f"{actions_to_commands[action]} {resource_name}"

# Gera e exibe o comando kubectl correspondente
print(kubectl_command(input_string))