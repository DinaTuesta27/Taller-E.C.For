sum=0
c=0
for k in range (1,1000):
    if(sum<1000):
        sum=sum+((k**2)+1)/k #la operación esta dentro de la condición e imprime eso
        if(sum<1000): #por eso necesita otra cond.
           print(sum)
           c=c+1
           print(c) #terminos que uso para obtener el valor
    else:
        break #para romper el bucle si no se cumple
    #es mejor usar un while
    



