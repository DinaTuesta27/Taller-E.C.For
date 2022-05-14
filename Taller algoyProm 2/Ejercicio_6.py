#Entradas
mujeres=int(input("Cantidad de mujeres: ")) #int
hombres=int(input("Cantidad de hombres: ")) #int
#Caja negra
total_de_estudiantes=mujeres+hombres #int
mp=mujeres*100/total_de_estudiantes #float
hp=hombres*100/total_de_estudiantes #float
#Salida
print(f"El pocentaje de mujeres es:{round(mp,2)} y el de hombres es: {round(hp,2)}")