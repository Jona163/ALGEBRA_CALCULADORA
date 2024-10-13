# Autor: Jonathan Hernández
# Fecha: 12 octubre 2024
# Descripción: Calculadora Algebraica en Python.
# GitHub: https://github.com/Jona163


import matplotlib.pyplot as plt
import tkinter as tk
import cmath
import math 
import numpy as np

def menu():
    print("----------MENU----------")
    print("1. SUMA")
    print("2. RESTA")
    print("3. MULTIPLICACION")
    print("4. DIVISION")
    print("5. POTENCIAS A LA N")
    print("6. POTENCIAS DE I")
    print("7. RAICES DE NUMEROS COMPLEJOS")

def switch(case, q, w, e, r):
    sw={
    }
    return sw.get(case,default())

def default():
    return "La opcion %s no existe en el menu"% case

repetir=True
while repetir:
    print("**************Calculadora de Numeros Complejos**************")
    print("Numeros de la forma a+bi")
    print("Con a como la parte real y b la parte imaginaria")
    print("************************************************************")
    menu()
    case=int(input("Selecciona una operacion "))
    if case == 1:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Numero ingresado: ",(z))
        n=a+c
        m=b+d
        z= complex(n, m)
        print ("El resultado es", z)
        x = [n]
        y = [m]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.title("Gráfica cartesiana",  fontsize=15, color="r", name="Times New Roman")
        plt.show()
        rep=input("¿Desea realizar otra operacion? [Si/No]")
        if rep == "si" or rep == "Si":
                repetir = True
       else:
                repetir=False
           
   elif case == 2:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Numero ingresado: ",(z))
        n=a-c
        m=b-d
        z= complex(n,m)
        print ("El resultado es", z)
        x = [n]
        y = [m]
        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.title("Gráfica cartesiana",  fontsize=15, color="r", name="Times New Roman")
        plt.show()
        rep=input("¿Desea realizar otra operacion? [Si/No]")
        if rep == "si" or rep == "Si":
                repetir = True
        else:
                repetir=False

    elif case == 3:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Nunero ingresado: ",(z))
        n = (a*c) - (b*d)
        m = (b*c) + (a*d)
        z = complex (n,m)
        print("El resultado es", z)
        x = [n]
        y = [m]

        plt.scatter(x,y)
        plt.ylabel('Imaginario')
        plt.xlabel('Real')
        plt.title("Gráfica cartesiana",  fontsize=15, color="r", name="Times New Roman")
        plt.show()
        rep=input("¿Desea realizar otra operacion? [Si/No]")
        if rep == "si" or rep == "Si":
                repetir = True
        else:
                repetir=False

    elif case == 4:
        a=int(input("Digite la parte real del primer numero complejo "))
        b=int(input("Digite la parte imaginaria del primer numero complejo "))
        z = complex(a,b)
        print("Numero ingresado: ",(z))
        c=int(input("Digite la parte real del segundo numero complejo "))
        d=int(input("Digite la parte imaginaria del segundo numero complejo "))
        z = complex(c,d)
        print("Numero ingresado: ",(z))
        modulo2 = c*c + d*d
        n = (a*c) + (b*d)
        real = n / modulo2
        m = (b*c) - (a*d)
        imag = m / modulo2
        z = complex(real,imag)
        print("El resultado es", z)
        x = [real]
        y = [imag]
