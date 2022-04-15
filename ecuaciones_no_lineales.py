# -*- coding: utf-8 -*-
"""Ecuaciones no lineales.ipynb

Ecuaciones no lineales. Metodos de aproximar la raiz.
"""

#Metodo de la biseccion

import sympy
import matplotlib.pyplot as plt
import numpy as np

x = sympy.symbols("x")
#Take intergers to know the interval graphing
a = 0 #Lower Limit
b = 1 #Upper Limit
n = 200 #Iterations

def y(x):
  return np.e**(x-1)-1.5*x
sumatory = 0
f_a = y(a)
f_b = y(b)

if (f_a*f_b > 0):
  print("No hay raiz entre los extremos dados. Intente con otros extremos.")
else:
  if (f_a*f_b == 0):
    if(f_a == 0): 
      print(a, "es la raiz de la funcion")
    else:
      print(b, "es la raiz de la funcion")
  else: #f_a*f_b < 0
    for i in range(n):
      x_m = (a+b)/2
      f_xm = y(x_m)
      if (f_a*f_xm > 0):
        a = x_m
      else:
        b = x_m
  print("La raiz aproximada es", x_m)
  

x = np.linspace(a-3,b+3, 1000) 
lista_y = y(x)
plt.plot(x,lista_y,"-r")
plt.plot([x_m],[0],marker="o") #Solucion
plt.grid()
