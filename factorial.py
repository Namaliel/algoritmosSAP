## Mejia Galindo Carlos Alejandro 1154 Nov 21
import os
import sys

def factorial(x):
    base = 1
    if x != 0: ## Se inicia el bucle para obtener el produto 
        for i in range(x):
            base *= i+1 ## Se obtienen los productos de los números menores a x
    else:
        base = 1
    return base

def main():
    print(f"El factorial de {sys.argv[1]} es: {factorial(int(sys.argv[1]))}")

if __name__=="__main__":
    main()
