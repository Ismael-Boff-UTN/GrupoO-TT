
# Funcion que comprueba si todos los digitos son iguales
def todosDigitosIguales(numero):
    num = list(numero)
    primerDig = num[0]
    for dig in num:
        if dig != primerDig:
            return False
    return True

# Funcion que devuelve el numero de iteraciones hasta alcanzar 6174 aplicando la rutina de Kaprekar
def kaprekar(num):
    if todosDigitosIguales(str(num)):
        return 8  # Devuelve 8 si son todos los digitos iguales
    tmp = num
    i = 0
    while tmp != 6174:
        tmp = '{:0>4}'.format(tmp)  # Completa con 0 hasta los 4 digitos
        tmp = list(str(tmp))  # Pasa de string a lista de caracteres
        tmp.sort(reverse=True)  # Ordena los caracteres en forma descendiente
        tmp = "".join(tmp)  # Une los caracteres en una cadena
        numRev = "".join(reversed(tmp))# Invierte los caracteres en otra cadena
        tmp = int(tmp) - int(numRev)# Castea la cadena ordenada e invertica a entero y los resta
        i += 1  # Cuenta las iteraciones realizadas hasta alcanzar 6174

    return i


# Pide cantidad de numero a ingresar
cantDeNum = input("ingrese cantidad de casos de prueba\n")
lista = list()
for i in range(int(cantDeNum)):

    while True:                                         # Bucle de validaciones
        num = input(f"ingrese num {i}: ")

        if not(num.isnumeric()):                        # Que solo se ingresen digitos
            print("Solo puede ingresar numeros")
            continue
        elif len(num) != 4:                             # Que solo sean 4 digitos
            print("El numero debe tener 4 digitos")
            continue
        else:
            lista.append(int(num))
            break

print(f"\nLos numeros son:\n{lista}")  # Muestra los numeros elegidos

lista_iter_kaprekar = list()
for n in lista:
    # Obtiene la cantidad de iteraciones para cada numero
    lista_iter_kaprekar.append(kaprekar(n))

# Muestra el numero de iteraciones de cada numero
print(f"\nLos cantidad de iteraciones son:\n{lista_iter_kaprekar}")
