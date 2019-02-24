
#___DATA TYPE___
z = 5.23234
print(type(z))


#___STRINGS___
x = "awesome"
y = "Python is " + x
print(y)
cadena = "The quick brown fox jumps over the lazy dog."
print(cadena.upper())
print(cadena.split(" "))


#___INPUT___
print("Enter your name please:")
x = input()
print("\nThank you dawg!")
print("\nMy nigga, your name is: " + x +".\n")


#___ARRAYS___
listado = ["Pera","Papaya","Sandia","Uva"]
listado[2] = "Reemplazo"
print(listado)

lista = list(("E_1", "E_2", "E_3"))
lista.remove("E_1")
print(lista)

tupla = ("carro", "avión", "barco")
print(tupla)

conjunto = {"uno", "dos", "tres"}
print(conjunto)

datos = dict( gato = "cat", perro = "dog", loro = "parrot" )
del(datos["gato"])
print(datos)



def Examen(parcial1, parcial2):
 nota_parciales = parcial1 + parcial2
 media = nota_parciales / 2
 if media < 6:
  print ("Reprobado")
 else:
  if media < 7:
   print ("Suficiente")
  else:
   if media < 8:
    print ("Bien")
   else:
    if media < 9:
     print ("Notable")
    else:
     if media >= 9:
      print ("Sobresaliente!")

Examen(2,9)

#//////////////////////////////////////////


import turtle

from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425,225)
pantalla.screensize(400,200)

dibuja = Turtle()
dibuja.forward(100)
dibuja.write("A \n\n")
dibuja.forward(130)
dibuja.write("B \n\n")
dibuja.forward(140)
dibuja.write("C \n\n")
dibuja.forward(140)
dibuja.write("D \n\n")
dibuja.forward(140)


pantalla.exitonclick()

#///////////////////////////////////////////

