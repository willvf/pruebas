import random  # Importamos la librería random

# variable llamada "puntaje", la que inicializamos en 0.
puntaje = random.randint(0, 10000)



print("\033[34mSoy Akira toriyama creador del anime Dragon ball, ¿Cuál es tu nombre? \033[39m\n")


# almacenando sus nombres en una variable

nombre = input("")
import time

# Ejemplo 1
time.sleep(1)

print(
    "\n\033[34mHola", nombre,
    "Esperame 5 segundos ya regreso y si sigues aca te contare sobre dragon ball \033[39m\n"
)
import time
import time


time.sleep(5) 

print("\033[34m!Oh vaya!, sigues aca que bueno que me hayas esperado\033[39m\n")
import time

import time


time.sleep(3) 


print("\033[35mPues te contare, cree dragon ball ya hace muchos años, publique")
import time


time.sleep(3)
print("el manga en la revista Shonen Jump, de la editorial Shueisha")
import time


time.sleep(3)
print("en japon en el año 1984. El manga tuvo 519 Capítulos impresos")
import time


time.sleep(3)
print("recopilados en 42 volúmenes dos años después la empresa Toei")
import time


time.sleep(3)
print("Animation lo convirtió en anime y lo transmitió por el canal Fuji television.\033[39m\n")
import time


time.sleep(3)

print("\033[34m¡Ahora quiero saber cuánto sabes sobre dragon ball!\n")
import time


time.sleep(3)
print("Quiero saber si eres un verdadero saiyayin o si eres un insecto asi como  dice Vegeta.\n")
import time

time.sleep(3)

print ("Comenzaras con ", puntaje, "puntos, Cada respuesta correcta se te sumara Mil puntos, el puntaje determinara tu nivel de pelea\033[39m\n")

import time

time.sleep(3)


# Pregunta 1
print("1) ¿Como se llama el abuelito de Goku?\n")

import time

time.sleep(1)

print("a) Gohan")
print("b) Yamcha")
print("c) Majimbu")
print("d) Maestro roshi")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:\n")

if respuesta_1 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_1 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_1 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 2
print("2) ¿Quién es el Padre de goku?\n")
import time

time.sleep(1)
print("a) Picoro")
print("b) El gran patriarca")
print("c) Bardock")
print("d) Raditz")
# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")
while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")


if respuesta_2 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_2 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_2 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 3
print("3) ¿Como se llama el hermano de goku?\n")
import time

time.sleep(1)
print("a) Freezer")
print("b) Den Den")
print("c) kaiosama")
print("d) Raditz")
# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")
while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")
  
if respuesta_3 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_3 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_3 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

#Pregunta 4

print("4) ¿Cual es el nombre completo de Picoro?\n")
import time

time.sleep(1)
print("a) Picoro Daimaku")
print("b) Picoro Quispe")
print("c) Picoro Fujimori")
print("d) Picoro Mamaní")

# Almacenamos la respuesta del usuario en la variable "respuesta_4"
respuesta_4 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_4 not in ("a", "b", "c", "d"):
    respuesta_4 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_4 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_4 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_4 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

#Pregunta 5
  print("5) ¿Quién le enseño el Kame hame ha a goku?\n")
import time

time.sleep(1)
  
print("a) Maestro roshi")
print("b) Maestro suru")
print("c) Kamisama")
print("d) Kaiosama")

# Almacenamos la respuesta del usuario en la variable "respuesta_5"
respuesta_5 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_5 not in ("a", "b", "c", "d"):
    respuesta_5 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_5 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_5 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_5 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

#Pregunta 6
  print("6) ¿Con quién se caso Goku?\n")
import time

time.sleep(1)
print("a) Bulma")
print("b) Milk")
print("c) Tigresa del oriente")
print("d) Sheyla rojas")

# Almacenamos la respuesta del usuario en la variable "respuesta_6"
respuesta_6 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_6 not in ("a", "b", "c", "d"):
    respuesta_6 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_6 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_6 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_6 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")
import time

time.sleep(1)
#Pregunta 7
print("7) ¿En que se transforma goku?\n")
import time

time.sleep(1)
print("a) En super Saiyayin")
print("b) En timoteo")
print("c) En barney")
print("d) En Superman")

# Almacenamos la respuesta del usuario en la variable "respuesta_7"
respuesta_7 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_7 not in ("a", "b", "c", "d"):
    respuesta_7 = input(
         "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_7 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_7 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_7 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 8
print("8) ¿Qué mascota tiene roshi?\n")
import time

time.sleep(1)
print("a) El Zorro run run")
print("b) Un perro")
print("c) Una tortuga")
print("d) Un conejo")

# Almacenamos la respuesta del usuario en la variable "respuesta_8"
respuesta_8 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_8 not in ("a", "b", "c", "d"):
    respuesta_8 = input(
         "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_8 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_8 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_8 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 9
print("9) ¿De que planeta es picoro?\n")
import time

time.sleep(1)
print("a) Marte")
print("b) Tierra")
print("c) Namekusein")
print("d) Vegita")

# Almacenamos la respuesta del usuario en la variable "respuesta_9"
respuesta_9 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_9 not in ("a", "b", "c", "d"):
    respuesta_9 = input(
         "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_9 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_9 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_9 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 10
print("10) ¿Quien es el asistente de kamizama?\n")
import time

time.sleep(1)
print("a) Mister popo")
print("b) Yamcha")
print("c) vegeta")
print("d) Ulon")

# Almacenamos la respuesta del usuario en la variable "respuesta_10"
respuesta_10 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_10 not in ("a", "b", "c", "d"):
    respuesta_10 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_10 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_10 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_10 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 11
print("11) ¿Como se llama la Mamá de goku?\n")
import time

time.sleep(1)
print("a) Magaly")
print("b) Gine")
print("c) Dayanita")
print("d) Shirley")

# Almacenamos la respuesta del usuario en la variable "respuesta_11"
respuesta_11 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_11 not in ("a", "b", "c", "d"):
    respuesta_11 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_11 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_11 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_11 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 12
print("12) Cuando el maestro roshi entreno a goku, Quién fue su commpañero?\n")
import time

time.sleep(1)
print("a) Yamcha")
print("b) Majimbu")
print("c) Ten chin han")
print("d) Krilin")

# Almacenamos la respuesta del usuario en la variable "respuesta_12"
respuesta_12 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_12 not in ("a", "b", "c", "d"):
    respuesta_12 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_12 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_12 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_12 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 13
print("13) ¿Como se llama el Legendario Super Saiyayin?\n")
import time

time.sleep(1)
print("a) Broly")
print("b) Trunks")
print("c) Vegeta")
print("d) Nappa")

# Almacenamos la respuesta del usuario en la variable "respuesta_13"
respuesta_13 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_13 not in ("a", "b", "c", "d"):
    respuesta_13 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_13 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_13 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_13 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 14
print("14) ¿Quién mato a Nappa?\n")
import time

time.sleep(1)
print("a) Picoro")
print("b) Vegeta")
print("c) krilin")
print("d) Gohan")

# Almacenamos la respuesta del usuario en la variable "respuesta_14"
respuesta_14 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_14 not in ("a", "b", "c", "d"):
    respuesta_14 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_14 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_14 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_14 == "d":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

# Pregunta 15
print("15) ¿Quién entreno a gohan de niño?\n")
import time

time.sleep(1)
print("a) Krilin")
print("b) Mister popo")
print("c) Yamcha")
print("d) Picoro")

# Almacenamos la respuesta del usuario en la variable "respuesta_15"
respuesta_15 = input("\n\033[33m Tu respuesta\033[39m:")
while respuesta_15 not in ("a", "b", "c", "d"):
    respuesta_15 = input(
        "Debes responder a, b, c o d. ingresa nuevamente tu respuesta:")

if respuesta_15 == "a":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_15 == "b":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
elif respuesta_15 == "c":
  print("\033[31mIncorrecto\033[39m", nombre, "!\n")
else:
  puntaje += 1000
  print("\n\033[32mMuy bien tu nivel de pelea se incrementa\033[39m", nombre, "!\n")

import time


time.sleep(2)

print ("\033[34mSí superaste los 13 mil nivel de pelea eres un guerrero de clase alta, Si no eres un insecto\033[39m\n")

import time


time.sleep(3)


input("Ahora presiona Enter para ver tu nivel de pelea\n")

import time


time.sleep(4)
  
print ("\033[33mtu nivel de pelea es de\033[39m", puntaje, "\n")

import time


time.sleep(3)

print ("\033[36mGracias", nombre, "por jugar mi trivia\033[39m\n")





























   





