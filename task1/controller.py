from statistics import mode
import task1.model as model

def Iniciar_Dados() -> None:
    model.Lista_Pais = model.LinkedList()

#Registar país no *início* da lista
#Retorna a lista ligada atual
def Registar_no_Inicio(pais : str) -> model.LinkedList:
    #Inserir no inicio
    model.Lista_Pais.insert_at_start(pais)
    #returnar lista ligada
    return model.Lista_Pais.traverse_list()

#Registar país no *fim* da lista
#Retorna a lista ligada atual
def Registar_no_Fim(pais : str) -> model.LinkedList:
    #Inserir no fim
    model.Lista_Pais.insert_at_end(pais)
    #returnar lista ligada
    return model.Lista_Pais.traverse_list()

#Registar país *depois* de outro elemento
#Retorna a lista ligada atual
def Registar_Depois(pais : str, pais_registado : str) -> model.LinkedList:
    #Inserir depois de elemento
    model.Lista_Pais.insert_after_item(pais_registado, pais)
    #returnar lista ligada
    return model.Lista_Pais.traverse_list()    

#Registar país *antes* de outro elemento
#Retorna a lista ligada atual
def Registar_Antes(pais : str, pais_registado : str) -> model.LinkedList:
    #Inserir no fim
    model.Lista_Pais.insert_before_item(pais_registado, pais)
    #returnar lista ligada
    return model.Lista_Pais.traverse_list()

#Registar país *antes* de outro elemento
#Retorna a lista ligada atual
def Registar_Indice(pais : str, indice : int) -> model.LinkedList:
    #Inserir no fim
    model.Lista_Pais.insert_at_index(indice,pais)
    #returnar lista ligada
    return model.Lista_Pais.traverse_list()

#Conta os elementos da lista
def Contar_Elementos() -> int:
    return model.Lista_Pais.get_count()

#Verificar a existencia de um pais pelo nome do proprio
#Retorna True se existir e False se não existir
def Verificar_Pais(pais : str) -> bool:
    return model.Lista_Pais.search_item(pais)

#Elimina o primeiro elemento da lista
#Retorna o elemento eliminado
def Eliminar_Primeiro() -> model.Node:
    model.Lista_Pais.reverse_linkedlist()
    elemento_eliminado : model.Node = model.Lista_Pais.get_last_node()
    model.Lista_Pais.reverse_linkedlist()
    model.Lista_Pais.delete_at_start()
    return elemento_eliminado

#Elimina o ultimo elemento da lista
#Retorna o elemento eliminado
def Eliminar_Ultimo() -> model.Node:
    elemento_eliminado : model.Node = model.Lista_Pais.get_last_node()
    model.Lista_Pais.delete_at_end()
    return elemento_eliminado

#Elimina o elemento da lista respectivo
def Eliminar_Pais(pais : str) -> None:
    model.Lista_Pais.delete_element_by_value(pais)