# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo

suma = nombre +" "+ apellido #aqui se le agrega a la suma el string espacio para separar
print(suma) #aqui imprimimos el consola el resultado

# Almacenar su nombre completo en una variable
# nombre_completo = .....

nombre_completo = nombre + apellido #aqui almacenamos el resultado suma en la variable

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
 
print(len(nombre_completo))#aqui imprimimos la cantidad de letras que tiene el nombre completo
