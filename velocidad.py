#Actividad 2

#Lista de velocidades
velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

#Se define una función llamada 'promedio' que toma la variable "lista" como un argumento
def promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio #devolver el valor del promedio calculado

#Definimos la función "filtrar" que toma la variable "lista" y el promedio calculado anteriormente como argumentos
def filtrar(lista, promedio):
    #Creamos una lista vacía para almacenar las velocidades que están sobre el promedio
    lista_sobre_promedio = []

#Creamos un Ciclo For iterable para cada elemento que compone la lista de velocidades. Si la condición es verdadera, es decir, si hay velocidades mayores al promedio, deberán integrarse a la lista vacía creada anteriormente
    for i in range(len(lista)):
        if lista[i]>promedio:
            lista_sobre_promedio.append(i)
    return lista_sobre_promedio

#Resultado se imprimen las posiciones de los valores que están por sobre el promedio.
print(filtrar(velocidad, promedio(velocidad)))