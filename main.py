archivo = open('paises_2.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
"""
for i in archivo:
    print(i)
"""
"""
#Imprima todos los paises
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
"""
#Imprima todas las Capitales
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
"""
#Cuente e imprima cuantas ciudades inician con la latra M  
lista=[]
ciudad=[]
c=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1): #(-1) para que no de el salto de linea
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    c=c+1
    print(i) 
print(c)
"""

#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
todos=[]
for i in archivo:
  t=i.index(":")
  for x in range(0,t+2):
    todos.append(i[x])
  t="".join(todos)
  if(t[0]=="U"):
    print(t)
  todos=[]

"""
#Cuente e imprima cuantos paises que hay en el archivo
pais=[]
pa=0
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    pais.append(i[r])
  a="".join(pais)
  print(a)
  pais=[]
  pa=pa+1
print(pa)
"""
"""
#Busque e imprima la ciudad de Singapur
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1): 
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="S"):
    p=ciudad.index('Singapur')
print(ciudad[162])
"""
"""
#Busque e imprima el pais de Venezuela y su capital
lista=[]
pais=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(i=='Venezuela: Caracas\n'):
    print(i)
"""
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
lista=[]
pais=[]
pai=0
for i in archivo:
  a=i.index(":")
  for r in range(0,a): 
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]
for i in pais:
  if(i[0]=="E"):
    pai=pai+1
    print(i) 
print(pai)
"""
"""
#Busque e imprima la Capital de Colombia
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1): 
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    b=ciudad.index('Bogotá')
print(ciudad[41])
"""
"""
#imprima la posicion del pais de Uganda
u=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(u)
"""
"""
#imprima la posicion del pais de Mexico
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México\n"):
    break
  lista=[]   
print(c)
"""
"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato

lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
for i in lista:
  lista.remove("Madagascar: rey julien\n")
  lista.insert(109,"Madagascar: Antananarivo\n") 
  break
print(lista)
"""
"""
#Agregue un país que no esté en la lista 
lista=[]
nuevo=["Bolivar: Cartagena\n"]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
for i in lista:
  lista.extend(nuevo)
  break
print(lista)
"""