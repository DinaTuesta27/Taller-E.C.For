while True:
    datos=input()
    x,m=datos.split(" ")
    x=int(x)
    m=int(m)
    #Condición de cierre
    if(x==0 and m==0):
        break #romper el bucle para que no sea infinito
    #caja negra
    r=x*m
    #Salida
    print(r)