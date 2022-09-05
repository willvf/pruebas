# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia ")
print ("Pondremos a prueba tus conocimientos")

# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre: ")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas
print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿Quién es el creador de facebook?")
print ("a) Mark zuckerberg")
print ("b) Susy diaz")
print ("c) Majimbu")
print ("d) El cuto guadalupe")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
while respuesta_1 not in ("a" ,"b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")
x = respuesta_1
if x  in ("a"):
  print ("Es correcto:\n")
else:
  print("Equivocado:\n")

# Pregunta 2
print ("1) ¿Quién dice MEE!?")
print ("a) cristian cueva")
print ("b) la chabelita")
print ("c) Majimbu")
print ("d) magaly")
# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_2 = input("\nTu respuesta: ")
while respuesta_2 not in ("a","b","c","d"):
  respuesta_2 = input("Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")
x = respuesta_2
if x  in ("c"):
  print ("Es correcto")
else:
  print("Equivocado")