#Listas
cadena="cadena de caracteres"
lista=["Nombre",20,True,"Juancho",cadena,100.25]
print(lista)
sexo="Masculino"
miLista=["Isaac","López",1.85,314310710,sexo]
print(miLista)
print(len(miLista))
print(type(miLista[3]))
car="Chevrolet"
miLista.append(car)
print(miLista)
print(miLista.index(car))
print(miLista.count(sexo))
miLista.extend([90,"hola"])
print(miLista)
input("......")
#count(objeto)devuele cantidad de objetos que hay en la lista
#ve cuantos objetos hay en la Listas
#Index(objeto)devuelve en que indice esta el objeto en l Listas
#append(objeto) Agrega el objeto a la lista hasta el final
#extend(secuencia) Añade una lista de datos
#insert(indice,objeto) añade un objeto en una parte especifica de la lista
#pop(indice)Elimina un indice
#remove(objeto)Retira de la lista el objeto indicado
