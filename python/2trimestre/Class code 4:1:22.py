#comentarios 

''' hola '''

#print(mensaje): permite mandar info a la pantalla
print("hola")

print("saludos")

print(5)

print(5+5)

#constantes son datos que no cambian 

dia=4

print("dia")

pie=3.14

print(pie)

#variables son datos que pueden o no cambiar 

calificacion=6

print(calificacion)

calificacion=calificacion+2

print(calificacion)

#print mas bonito 

print("tu calificacion es: ", calificacion)

print("hoy es ", dia, "de enero")

print(pie, "es el valor de pi que usaremos")

#operadores matematicos 

# + sumar, - restar, / dividir, * multiplicar 

a=2
b=3

print(a+b)
print(a-b)
print(a*b)
print(b/a)

print((a+b)*b)

print(a+b*b)

#jerarquia de operaciones (parentesis, potencias, multiplicaciones, sumas)

#loop: se refiere a cualquier codigo que se pueda ciclar o repetir n numero de veces

#WHILE: mientras una cindicion ocurra (o no) se ejecuta todo el codigo dentro de la misma 


#operadores logicos
#a>b a es mayor que b
#a<b a es menor que b 
#a==b a es identico a b

#a>=b a es mayor que o igual que b
#a>=b a es menor que o igual que b

tomate=2
while(tomate>0)
  print("hay tomate")
  tomate=tomate-1 

#identacion nos dice que lineas pertenecen a un ciclo o condiciom, puede ser un simple espacio o tab

#while True es una condicion que pregunta si se puede ejecutar, si respondes que si el codigo funciona

while True:
  print("hola")


#input(): nos permite ingresar información al codigo desde la consola, se debe presionar enter una vez que termines


#nombre es una variable porque puede cambiar si se ejecuta de nuevo
nombre=input()
print("saludos mr. ", nombre)
#####################################
apellido=input("apellido: ")
print("saludos mr. ", apellido)

edad=input()
print(edad*10)
#input solo recibe strings necesitas convertirlo si quieres trabajar con números 

#int() convertir letras a numeros enteros
edad=int(input())