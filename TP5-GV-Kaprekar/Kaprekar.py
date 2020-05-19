
# Funcion que comprueba si todos los digitos son iguales
def todosDigitosIguales(numero):
    digitos = str(numero)
    for digito in digitos:
        if digito != digitos[0]: # Si algún digito es distinto al inicial, no son todos iguales
            return False
    return True

# Función que devuelve el numero de iteraciones hasta alcanzar 6174 aplicando la rutina de Kaprekar
def kaprekar(num):
    if todosDigitosIguales(num):
        return 8  # Devuelve 8 si son todos los digitos iguales
    i = 0
    while num != 6174:
        num = str(num).zfill(4)                     # Completa con 0 hasta los 4 digitos
        numDesc = "".join(sorted(num,reverse=True)) # Ordena los caracteres en forma descendiente y los une
        numAsc  = "".join(reversed(numDesc))        # Invierte los caracteres en otra cadena
        num = int(numDesc) - int(numAsc)            # Castea la cadena ordenada e invertica a entero y los resta
        i += 1                                      # Cuenta las iteraciones realizadas hasta alcanzar 6174
    return i

# Pide cantidad de numeros a ingresar
cantDeNum = input("ingrese cantidad de casos de prueba\n")
listaDeNumeros = list()
for i in range(int(cantDeNum)):                         # Bucle de Ingreso de Numeros
    while True:                                         # Bucle de validaciones
        num = input(f"ingrese num ({i+1} de {cantDeNum}): ")               # Pide el ingreso de numeros
        if not(num.isnumeric()):                        # Valida que solo se ingresen digitos
            print("Solo puede ingresar numeros")
            continue
        elif len(num) > 4:                              # Valida que sean hasta 4 digitos
            print("El numero debe tener menos de 4 digitos")
            continue
        elif len(num) < 2:                              # Valida que sean al menos 2 digitos
            print("El numero debe tener al menos de 2 digitos")
            continue
        else:
            listaDeNumeros.append(int(num))
            break

# Muestra los numeros elegidos
print(f"\nLos numeros son:\n{listaDeNumeros}")  

# Obtiene la cantidad de iteraciones para cada numero
lista_iter_kaprekar = list()
for n in listaDeNumeros:
    lista_iter_kaprekar.append(kaprekar(n))

# Muestra el numero de iteraciones de cada numero
print(f"\nLos cantidad de iteraciones son:\n{lista_iter_kaprekar}")

