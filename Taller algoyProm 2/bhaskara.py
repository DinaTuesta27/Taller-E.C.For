#Entradas
import math
num=input("")
a,b,c=num.split(" ")
a=float(a)
b=float(b)
c=float(c)
print(a,b,c)
#Caja negra1
form1=("")
form2=("")
if(a==0 and a==0.0):
    print("Impossivel calcular")
else:
    form1=round((-b+math.sqrt(b**2-4*a*c)/(a*2),5))
    form2=round((-b-math.sqrt(b**2-4*a*c)/(a*2),5))
    print("R1=",form1)
    print("R2=",form2)