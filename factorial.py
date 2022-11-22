## Mejia Galindo Carlos Alejandro 1154 Nov 21
import os
import sys

def factorial(x):
    base = 1
    if x != 0: ## Se inicia el bucle para obtener el produto 
        for i in range(x):
            base *= i+1 
    else:
        base = 1
    return base

def main():
    print(factorial(int(sys.argv[1])))

if __name__=="__main__":
    main()
