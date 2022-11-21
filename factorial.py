import os
import sys

def factorial(x):
    sol = 1
    for i in range(x):
        sol *= i+1
    return sol

def main():
    print(factorial(int(sys.argv[1])))

if __name__=="__main__":
    main()
