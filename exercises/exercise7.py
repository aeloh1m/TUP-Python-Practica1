""""Tuplas y Desempaquetado"""


"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

from calendar import c


lista = ["casa", "perro", "pato", "gato"]

# COMPLETAR - INICIO

tupla = tuple(lista)

print(tupla)

# COMPLETAR - FIN

assert tupla == ("casa", "perro", "pato", "gato")


"""
A partir de la siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

# COMPLETAR - INICIO

lista = list(tupla)

print(lista)

# COMPLETAR - FIN

assert lista == ["casa", "perro", "pato", "gato", "tenedor"]


"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

# COMPLETAR - INICIO

(a, b, c) = tupla

print(tupla)

# COMPLETAR - FIN

assert a == "primer" and b == 25 and c == [1, 2, 3]


"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

# COMPLETAR - INICIO

(a, b, c, d, e, f) = tupla

total = a + b + c + d + e + f

print(total)

# COMPLETAR - FIN

assert total == 300


"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO

(e, m, s, a, c) = lista

string_concatenado = f"{e} {m} {s} {a} {c}"

print(string_concatenado)

# COMPLETAR - FIN

assert string_concatenado == "esta mañana sali a correr"


"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

# COMPLETAR - INICIO

(primer, b, c, d, e) = tupla

print(primer)

# COMPLETAR - FIN

assert primer == 73


"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

# COMPLETAR - INICIO

(elem_1, b, c, d, elem_2) = lista

suma = elem_1 + elem_2

print(suma)

# COMPLETAR - FIN

assert suma == 75


"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

# COMPLETAR - INICIO

(elem_1, elem_2, elem_3, elem_4, elem_5, f, g, h, i) = tupla

string_concatenado = f"{elem_1} {elem_2} {elem_3} {elem_4} {elem_5}"

print(string_concatenado)

# COMPLETAR - FIN

assert string_concatenado == "anoche fui a la fiesta"