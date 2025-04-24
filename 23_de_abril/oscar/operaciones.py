'''
 Crear las funciones suma, resta,
 multiplicación, división (validar 0 denominador),
 división piso
 crear una función que genere un número aleatorio
 (import random)
 crear una función operación módulo
'''
import random
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a/b
def numero_aleatorio():
    return random.randint(1, 100)


    
