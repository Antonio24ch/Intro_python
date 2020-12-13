# str.format ()
' ' ' El método format del objeto str ejecuta una operación de formato en una string. El string en el cual ' ' ' 
' ' ' este método es llamado puede contener texto o campos de sustitución delimitados por llaves {}.' ' '

# Ejemplo
print('Hola, {}!'.format('Antonio'))

' ' ' Cada campo de sustitución {} contiene un índice numérico correspondiente a los argumentos pasados' ' ' 
print('- - - - - - - - - - - - - - - - - - - - -')

print('Hola, {}. Tu edad es de {}' .format('Antonio', 26))

' ' ' Este método retorna una copia del string donde cada campo de sustitución {} es modificado por el' ' ' 
' ' ' valor correspondiente ' ' '

print(' - - - - - - - - - - - - - - - - - - - - ')
print('Hola, {nombre}. Tu edad es de {edad}' .format(nombre = 'Antonio', edad = 26))

' ' ' un f string puede contener campos de sustitución que pueden ser llenado por cualquier variable ' ' '

print('- - - - - - - - - - - - - - - - - - - - ')
nombre = 'Antonio'
edad = 26

print(f'Hola {nombre}. Tu edad es de: {edad}')


' '  ' La función input lee la lpinea de entrada, convierte una string y retorna ese valor' ' ' 

print(' - - - - - - - - - - - - - - - - - - - - ')
input('¿Cuál es tu nombre: ')

' ' ' Para utilizar un numero entero se ocupa la funcion int ' ' '
print(' - - - - - - - - - - - - - - - - - - - - ')
int(input('¿Cuál es tu edad? '))
