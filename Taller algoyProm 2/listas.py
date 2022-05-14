lista=[1,2,3,4,5,6,7,8,9,10]
frutas=["Mango","Kiwi","Fresa","pera"]
"""len-->tamaño
 #print(len(lista))
#la última posición
 #print(lista[0])
#Métodos de las listas
"""
#append
#lista.append(55)
#print(lista)

#index
#p=lista.index(8)
#print(p)

#count
#lista=[1,2,3,4,5,6,7,8,9,10,1]
#cuenta=lista.count(1) #()elemento que quiere contar
#print(cuenta) #2

#remove
#lista.remove(10)
#print(lista)

#clear
#lista.clear()
#print(lista)

#pop
#lista.pop()
#print(lista)

#copy
#copia=lista.copy()
#print(copia)

#extend
#lista.extend(frutas)
#print(lista)

#insert
#lista.insert(5,"banano") #primero se pone la posición a donde agregar y luego el objeto
#print(lista)

#reverse
#lista.reverse()
#print(lista)

#sort
frutas.sort() #ordena los números de forma ascendente
lista.sort(reverse=True)#Para ordenarlos de manera descendente
print(frutas) #con letras imprime como el abecedario
print(lista)
