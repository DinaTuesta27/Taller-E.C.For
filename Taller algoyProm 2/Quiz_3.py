#Entrada
from tokenize import String


l=int(input(""))#FILA
c=int(input(""))#cOLUMNA
#Caja nerga
mo=c%2
MI=l%2
resul=""
if(l>=1 and mo==1):
    resul="#000000"
elif(l<=1000 and mo==0):
    resul="#FFFFFFF"
#salida
print(resul)
