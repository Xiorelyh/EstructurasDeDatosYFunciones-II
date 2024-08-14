#Importacion de bibliotecas
import sys

#generamos diccionario de precios
precios = {'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000}

#el usuario ingresa valor de umbral
umbral = int(sys.argv[1])


#Generamos funciones para los filtros especificos
def filtrar_mayor(diccionario, umbral):
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
    nombre = list(filtro.keys())
    nombre = ", ".join(nombre)
    salida_texto = f"Los productos mayores al umbral son: {nombre}"
    return salida_texto

def filtrar_menor(diccionario, umbral):
    filtro = {k:v for k,v in diccionario.items() if v < umbral}
    nombre = list(filtro.keys())
    nombre = ", ".join(nombre)
    salida_texto = f"Los productos menores al umbral son: {nombre}"
    return salida_texto


#Condicional para que utilice las funciones de acuerdo a si el usuario ingresa un valor de menor, mayor u otro que no coincida
if len(sys.argv) > 2:
    if sys.argv[2] == "mayor":
        print(filtrar_mayor(precios, umbral))
    elif sys.argv[2] == "menor":
        print(filtrar_menor(precios, umbral))
    elif sys.argv[2] != "mayor" or regla != "menor" or regla != "":
        print("Lo sentimos, no es una operación válida")
#Condicional para que si no se le ingresa un tercer argumento, por defecto filtre los valores mayores que
elif len(sys.argv) < 3:
    print(filtrar_mayor(precios, umbral))