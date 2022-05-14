#entrada
tipo=str(input())
defi=str(input())
come=str(input())
#Caja negra
v="vertebrado"
a="ave"
m="mamifero"
o="onivoro"
c="carnivoro"
h="herbivoro"
inv="invertebrado"
ins="inseto"
an="anelideo"
he="hematofago"
ag="aguia"
p="pomba"
ho="homen"
va="vaca"
l="lagarta"
sa="sanguessuga"
mi="minhoca"
pul="pulga"
if(tipo==v and defi==a and come==c):
    
    print(ag)
elif(tipo==v and defi==a and come==o):
    
    print(p)
elif(tipo==v and defi==m and come==h):
    
    print(va)
elif(tipo==v and defi==m and come==o):
    
    print(ho)
elif(tipo==inv and defi==ins and come==he):
   
    print(pul)
elif(tipo==inv and defi==ins and come==h):
    
    print(l)
elif(tipo==inv and defi==an and come==he):
  
    print(sa)
elif(tipo==inv and defi==an and come==o):
    
    print(mi)

