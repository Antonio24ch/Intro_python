' ' '#1 Utlizando las variables de abajo, imprime la frase: "Sumando 10 con 20 tenemos 30" ' ' '
var1 = 10
var2 = 20
var3 = 'Sumando'
var4 = 'con'
var5 = 'tenemos'

print(var3 + (' ') + str(var1) + (' ') + var4 + (' ') + str(var2) + (' ') + (var5) + (' ') +  str(var1 + var2))

print(' - - - - - - - - - - - ')

' ' ' #2 Escribe un programa que reciba el año de nacimiento del usuario y retorne su edad en años en el 2020 ' ' '

fecnac = int(input('¿Cuál es tu año de nacimiento? \t'))

edad_act = 2020 - (fecnac)

print(f'Tu edad actual es: {edad_act} años')

print('- - - - - - - - - - - -')

' ' ' #3 Escribe un programa que reciba las informaciones sobre el peso(kilos) y la altura(metros) de un' ' '
' ' 'usuario e imprima su índice de masa corporal(IMC). Para obtener el IMC debemos dividir el peso del usuario' ' ' 
' ' ' por su altura elevada al cuadrado' ' '

kilos = float(input('¿Cúal es tu peso? \t'))
altura = float(input('¿Cúal es tu altura? \t'))

imc = kilos / (altura ** 2)

print(f'Tu IMC es de: {imc}')