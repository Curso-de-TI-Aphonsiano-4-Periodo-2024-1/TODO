#!\bin\python
print("-"*30)
print("------- Meu App TODO  ------")
print("-"*30)

lista_de_tarefas = [
    "Escovar os dentes",
    "Tomar banho gelado",
    "Passar roupas",
    "Levar as crianças na escola"
] #definindo variável tipo lista

def mostra_lista(): #definindo uma função de nome mostra_lista
    if len(lista_de_tarefas) > 0: #condição que verifica lista
        indice = 1
        print("Lista de tarefa:")
        for tarefa in lista_de_tarefas: #laço para percorrer a lista
            print(str(indice) + " - " + tarefa) #imprime o item da lista
            indice += 1
    else:
        print("Sem tarefas!!")

def add_item():
    nova_tarefa = input("Descrição: ")
    lista_de_tarefas.append(nova_tarefa)

def remover_item(indice):
    #TODO: Implementar remoção de item da lista
    # Será informado o indice do item e o mesmo 
    # deve ser deletado
    pass

while True:
    print("Opções:")
    print(" 0 - Sair")
    print(" 1 - Mostrar lista")
    print(" 2 - Adicionar item")
    print(" 3 - Remover item")
    opcao = int(input("Informe a opção: "))

    #TODO: Aplicar boas práticas de código
    # Altere os `if elif else` para `match case`
    if(opcao == 1):        
        mostra_lista()
    elif(opcao == 2):        
        add_item()
    elif(opcao == 3):        
        remover_item()
    elif(opcao == 0):
        exit()
    else:
        print("Opção inválida!")        
    
