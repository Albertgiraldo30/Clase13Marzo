bandas= []

opcion=100

while(opcion != 5):
    print('***Festival alta voz***')
    print('************************')
    print('1.Registrar banda')
    print('2.ver el carteñ de festival')
    print('3.Registrar bada')
    print('4.Modificar banda')
    print('5.Finalizar')
    
    opcion=int(input("digita una opcion: "))
    if opcion == 1:
        banda={}
        #se llena el obeto de banda
        banda["id"]=int(input("Digite el Id: "))
        banda["nombre"]=input("Digita el nombre: ")
        banda["Genero"]=input("Genero: ")
        banda["costo de la banda"]=int(input("Digita Precio banda: "))
        banda["Tiempo"]=input("Digita el Tiempo: ")
        
        #como agrego un diccionario a una lista

        bandas.append(banda)
        

    elif opcion == 2:
        #recorriendo una lista para inprimirsus elementos
        for bandaAuxiliar in bandas:
         print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")   
    elif opcion == 3:
        #buscando un elemeto dentro de una lista
        bandaBuscada=input("digita la banda que quieres buscar")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandaBuscada:
                print("oe la encontre")
            else:
                ("no lo encontro")

            #como detener el siclo
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print("opcion invalida")

    

    