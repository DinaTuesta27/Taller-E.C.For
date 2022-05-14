edad=int(input("Digite edad: "))
#indeterminado. No sabes cuantas vueltas va a hacer
while(edad<0):
    print("No se puede digitar edad negativa.")
    edad=int(input("Digite edad: "))

#Determinado. Tien un límite
c=0
while(c<=100):
    print(c)
c=c+1
