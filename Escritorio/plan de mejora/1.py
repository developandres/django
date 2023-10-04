
def lista_principal(cantidad):
    """LLenar una lista

        :param cantidad de elementos de la lista
        :return Lista
    """
    lista = []
    for i in range (cantidad):
        num = int(input("Digite un precio: "))
        lista.append(num)
    return lista
def descuento(lista):
    descuento = 0.20
    lista_20 = []
    for i in range(len(lista)):
        lista[i] * descuento
        lista_20.append(lista[i])
    return lista_20

def booleans(lista):
    lista_bool = [True,False, ]

def main():
    """Funcion principal que llama a otras funciones

    :var nombre asignado para llamar la funcion

    :function funcion a ser llamada

    :args argumentos que utilizan las funciones
    """

    cantidad = int(input("Ingrese la cantidad de precios: "))
    lista_llena = lista_principal(cantidad)

    
    print(lista_llena),
    """Se imprimen las variables con las funciones asigandas"""
    
    
if __name__ == '__main__':
    main()  
