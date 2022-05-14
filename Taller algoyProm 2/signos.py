#Entrada
#Saca fecha actual del sistema
from datetime import datetime
ahora=datetime.now
año_actual=ahora.year
mes_actual=ahora.month
dia_actual=ahora.day
#pedir fecha
fechan=input("Digite fecha de nacimiento: ")
año_nacimiento,mes_nacimiento,dia_nacimiento=fechan.split("/")
año_nacimiento=int(año_nacimiento)
mes_nacimiento=int(mes_nacimiento)
dia_nacimiento=int(dia_nacimiento)
#calcular edad
edad=0
edad=año_actual-año_nacimiento
#Calcular signo
if(mes_nacimiento>=11 and dia_nacimiento>=22) and (mes_nacimiento>=12 and dia_nacimiento>=21):
    zodiaco="Sagitario"
elif