"""
Entradas:
*a-->float-->a
*b-->float-->b
c-->float-->c
Salidas:
x1-->float-->x1
x2-->float-->x2
"""
import math
#Entradas
a=float(input("Digite a: "))
b=float(input("Digite b: "))
c=float(input("Digite c: "))
#Caja negra
d=b**2-(4*a*c)
x1=0.0 #variable global
x2=0.0
if(d>0):
    x1=(-b+math.sqrt(b**2-4*a*c)) #variable local
    print(x1)

