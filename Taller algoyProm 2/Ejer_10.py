#Entrada
cantidad=int(input("Digite cantidad de estudiantes: "))
altM=0 #altura mayor
for i in range(1,cantidad+1): #+1 para que no le reste a la cantidad
    #entrada
    altura=float(input("Digite altura: "))
    #caja negra
    if(altM<=altura):
        altM=altura
#Salida
print(altM)
