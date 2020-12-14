' ' 'Secuencia de valores que pueden ser de cualquier tipo, identificados por un índice, iniciado por 0, []' ' '
' ' ' formas de crear listas' ' '
' ' ' -Utilizando corchetes: [], [1]' ' '
' ' ' -Corchetes con items separados por coma: [1,2,3]' ' '
' ' ' -Utilizando list o list(iterador)' ' '

# Corchetes con items separados por coma: [1,2,3]
accesorios = ['llantas de alineacion', 'cerraduras electricas', 'piloto automatico', 'bancos de cuero', 
            'aire acondicionado', 'sensor de estacionamiento', 'sensor crepuscular', 'sensor de lluvia']

print(accesorios)
print(' - - - - - - - - - - - - - - - - - ')

# Utilizando list o list(iterador)
lista2 = list((1,2,3,4,5,6,7,8,9,10))

print(lista2)
print('- - - - - - - - - - - - - - - - - ')
# Pasando como argumento una string
lista3 = list('123456789')
print(lista3)

print('- - - - - - - - - - - - - -')
#LISTAS CON TIPOS DE DATOS VARIADOS
# Listas anidadas
carro1 = ['jetta variant', 'motor 4.0 turbo', 2003, 44410.0, False, ['llantas de alineacion', 'cerraduras electricas', 
            'piloto automatico'], 88078.64]

carro2 = ['passat', 'motor diesel', 1991, 5712.0, False, ['central multimedia', 'techo panoramico', 
            'frenos ABS'], 106161.94]

carros = [carro1 + carro2]
print(carros)