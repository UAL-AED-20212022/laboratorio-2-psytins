import task1.controller as controller

def main():
    #Inicializar Dados
    controller.Iniciar_Dados()

    while(True):
        try:
            # Entrada de dados
            menu_input : str = input()
            menu_split : list = menu_input.split()
        except EOFError:
            return
        
        #Funcionalidades
        if(menu_split[0] == "RPI"):
            # REGISTAR PAÍS NO *INÍCIO* DA LISTA

            #país
            pais_novo : str = menu_split[1]

            # Sem saídas de insucesso ---

            # Inserir país no início da lista (País registado apresentado no início)
            print(controller.Registar_no_Inicio(pais_novo))
            
        elif(menu_split[0] == "RPF"):
            # REGISTAR PAÍS NO *FIM* DA LISTA

            #país
            pais_novo : str = menu_split[1]

            # Sem saídas de insucesso ---

            # Inserir país no fim da lista (País registado apresentado no fim)
            print(controller.Registar_no_Fim(pais_novo))

        elif(menu_split[0] == "RPDE"):
            # REGISTAR PAÍS *DEPOIS* DE OUTRO ELEMENTO

            #país
            pais_novo : str = menu_split[1]
            pais_registado : str = menu_split[2]

            # Sem saídas de insucesso ---

            # Inserir país depois de outro elemento (Mostrar país de 1 para n)
            print(controller.Registar_Depois(pais_novo, pais_registado))

        elif(menu_split[0] == "RPAE"):
            # REGISTAR PAÍS *ANTES* DE OUTRO ELEMENTO

            #país
            pais_novo : str = menu_split[1]
            pais_registado : str = menu_split[2]

            # Sem saídas de insucesso ---

            # Inserir país antes de outro elemento (Mostrar país de 1 para n)
            print(controller.Registar_Antes(pais_novo, pais_registado))

        elif(menu_split[0] == "RPII"):
            # REGISTAR PAÍS NUM DETERMINADO ÍNDICE

            #país
            pais_novo : str = menu_split[1]
            indice : int = menu_split[2]

            # Sem saídas de insucesso ---

            # Inserir país num determinado indice
            print(controller.Registar_Indice(pais_novo, indice))

        elif(menu_split[0] == "VNE"):
            # VERIFICAR NÚMEROS DE ELEMENTOS DA LISTA

            # Sem saídas de insucesso ---

            # Verificar numeros de elementos
            print(f"O número de elementos são {controller.Contar_Elementos()}.")

        elif(menu_split[0] == "VP"):
            # VERIFICAR A EXISTENCIA DE UM PAIS

            #país
            pais : str = menu_split[1]

            # Verificar
            cod = controller.Verificar_Pais(pais)
            if(cod == True):
                #Sucesso
                print(f"O país {pais} encontra-se na lista.")
            elif(cod == False):
                #Insucesso
                print(f"O país {pais} não se encontra na lista.")           

        elif(menu_split[0] == "EPE"):
            # ELIMINAR PRIMEIRO ELEMENTO DA LISTA

            # Sem saídas de insucesso ---

            # Eliminar primeiro
            pais_eliminado : controller.Node = controller.Eliminar_Primeiro() #Ter atenção com o tipo de dados
            print(f"O país {pais_eliminado} foi eliminado da lista.")

        elif(menu_split[0] == "EUE"):
            # ELIMINAR ULTIMO ELEMENTO DA LISTA

            # Sem saídas de insucesso ---

            # Eliminar ultimo
            pais_eliminado : controller.Node = controller.Eliminar_Ultimo() #Ter atenção com o tipo de dados
            print(f"O país {pais_eliminado} foi eliminado da lista.")

        elif(menu_split[0] == "EP"):
            # ELIMINAR ELEMENTO
            error_ep : bool = False
            
            #pais
            pais_eliminar : str = menu_split[1]

            # Saídas de insucesso ---
            if(controller.Verificar_Pais(pais_eliminar) == False):
                print(f"O país {pais_eliminar} não se encontra na lista.")
                error_ep = True
            # ------------------

            # Eliminar ultimo
            if(error_ep == False):
                controller.Eliminar_Pais(pais_eliminar)
                print(f"O país {pais_eliminado} foi eliminado da lista.")

        else:
            #Debug
            print(controller.model.Lista_Pais.traverse_list())
            