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
