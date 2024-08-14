#Definimos la funcion factorial
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

#dEfinimos la funcion productoria
def productoria(producto):
    resultado = 1
    for numero in producto:
        resultado *= numero
    return resultado

#Definimos la funcion para calcular con kwargs dependiento de como empieza la sentencia
def calcular(**kwargs):
    for key, valor in kwargs.items():
        if key.startswith("fact_"):
            resultado = factorial(valor)
            print(f"El factorial de {valor} es {resultado}")
        elif key.startswith("prod_"):
            resultado = productoria(valor)
            print(f"La productoria de {valor} es {resultado}")


#ejecutamos la funcion calcular para comprobar los resultados
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)