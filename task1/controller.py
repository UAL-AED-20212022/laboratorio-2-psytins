import model
from models.LinkedList import LinkedList
from models.Node import Node

#Registar país no *início* da lista
#Retorna a lista ligada atual
def Registar_no_Inicio(pais : str) -> LinkedList: #ish
    pass

#Registar país no *fim* da lista
#Retorna a lista ligada atual
def Registar_no_Fim(pais : str) -> LinkedList: #ish
    pass

#Registar país *depois* de outro elemento
#Retorna a lista ligada atual
def Registar_Depois(pais : str, pais_registado : str) -> LinkedList: #ish
    pass

#Registar país *antes* de outro elemento
#Retorna a lista ligada atual
def Registar_Antes(pais : str, pais_registado : str) -> LinkedList: #ish
    pass

#Registar país *antes* de outro elemento
#Retorna a lista ligada atual
def Registar_Indice(pais : str, indice : int) -> LinkedList: #ish
    pass

#Conta os elementos da lista
def Contar_Elementos() -> int:
    pass

#Verificar a existencia de um pais pelo nome do proprio
#Retorna True se existir e False se não existir
def Verificar_Pais(pais : str) -> bool:
    pass

#Elimina o primeiro elemento da lista
#Retorna o elemento eliminado
def Eliminar_Primeiro() -> Node: # or LinkedList
    pass

#Elimina o ultimo elemento da lista
#Retorna o elemento eliminado
def Eliminar_Ultimo() -> Node: # or LinkedList
    pass

#Elimina o elemento da lista respectivo
def Eliminar_Pais(pais : str) -> None:
    pass