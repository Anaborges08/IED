tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

def adicionar_tarefa(tarefa): #Função para adicionar uma tarefa 
    tarefas.append(tarefa) #Adiciona a tarefa à lista principal de tarefas
    historico.append(tarefa) #Adiciona a tarefa à lista historico, para que possa ser desfeita posteriormente
    fila_execucao.append(tarefa) #Inclui a tarefa na lista fila_execucao, que funciona como uma fila (FIFO)
    print(f"Tarefa '{tarefa}' adicionada!\n") #Exibe uma mensagem informando que a tarefa foi adicionada com sucesso

def desfazer_ultima_tarefa(): # Cria uma função chamada desfazer_ultima_tarefa que não recebe parâmetros
    if historico: # Verifica se a lista historico não está vazia
        ultima = historico.pop() #Remove e retorna a última tarefa da lista historico usando o método pop()
        tarefas.remove(ultima) #Remove a tarefa da lista tarefas.
        fila_execucao.remove(ultima) #Remove a tarefa da lista fila_execucao
        print(f"Tarefa '{ultima}' desfeita!\n") #Exibe uma mensagem indicando que a última tarefa foi desfeita
    else: #Se  o histórico estiver vazio, executa o bloco abaixo
        print("Nenhuma tarefa para desfazer.\n") #Informa que não há tarefas para desfazer

def atender_tarefa(): #Cria uma função chamada atender_tarefa
    if fila_execucao: # Verifica se a lista fila_execucao não está vazia.
        feita = fila_execucao.pop(0) # Remove e retorna o primeiro item da lista (FIFO - Primeiro a Entrar, Primeiro a Sair)
        tarefas.remove(feita) #Remove a tarefa da lista principal tarefas
        print(f"Tarefa '{feita}' atendida!\n") #Exibe uma mensagem indicando que a tarefa foi atendida
    else: #Se a fila estiver vazia, executa o bloco abaixo
        print("Nenhuma tarefa para atender.\n") # Informa que não há tarefas para atender

def mostrar_tarefas(): #Cria uma função chamada mostrar_tarefas
    print("\n Lista de Tarefas:") # Imprime um título para a lista de tarefas
    for i, t in enumerate(tarefas): # Itera sobre a lista tarefas, obtendo o índice e o valor
        print(f"{i + 1}. {t}") #Exibe cada tarefa com numeração a partir de 1
    print() #Insere um espaço em branco para melhorar a formatação

while True: #Mantém o programa em execução até o usuário escolher sair

    # Mostra as opções disponíveis para o usuário:

    print("1. Adicionar Tarefa") #Mostra a opção "adicionar tarefa" usando o 1
    print("2. Desfazer Última Tarefa") #Mostra a opção "desfazer ultima tarefa" usando o 2
    print("3. Atender Tarefa (modo fila)") #mostra a opção "atender tarefa" usando o 3
    print("4. Mostrar Tarefas") #mostra a opção "mostra tarefas" usando o 4
    print("5. Sair") #mostra a opção "sair" usando o 5

    opcao = input("Escolha uma opção: ") # Aguarda a entrada do usuário

    if opcao == '1': # Verifica se a opção é "1"
        tarefa = input("Digite a tarefa: ") # Esta linha solicita que o usuário digite uma tarefa
        data_de_inicio = input("Digite a data de inicio (mm/dd/aa): ") # Solicita que o usuário informe a data de início da tarefa
        data_final = input("Digite a data final (mm/dd/aa): ") #  Solicita que o usuário informe a data final da tarefa
        adicionar_tarefa(f'{tarefa}, Inicio: ({data_de_inicio}) - Fim: ({data_final})') # Chama uma função chamada adicionar_tarefa() e passa como argumento uma string formatada contendo a tarefa e suas datas

    elif opcao == '2': #Verifica se a variável opcao tem o valor '2'
        desfazer_ultima_tarefa() # Chama a função desfazer_ultima_tarefa()
    elif opcao == '3': #  Verifica se o valor da variável opcao é '3'
        atender_tarefa() # chama a função atender tarefa()
    elif opcao == '4': # verifica se o valor da variavel apção é '4'
        mostrar_tarefas() # chama a função mostrar tarefas()
    elif opcao == '5': #verifica se o valor da variavel apção é '5'
        print("Saindo do programa...") # O comando print() exibe a mensagem "Saindo do programa..." no console
        break # O comando print() exibe a mensagem "Saindo do programa..." no console
    else:
        print("Opção inválida!\n")

file_name= "lista_tarefa.txt" # Define o nome do arquivo para salvar as tarefas

        # Se a lista tarefas não estiver vazia, grava cada tarefa em uma linha
if tarefas: 
    with open(file_name, "w") as file:
        for item in tarefas:
            file.write(item + "\n")

    print(f'salvo em {file_name}!') 

