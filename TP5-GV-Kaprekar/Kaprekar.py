
def todosDigitosIguales(numero):
    num = list(numero)
    primerDig = num[0]
    for dig in num:
        if dig != primerDig:
            return False
    return True


def kaprekar(num):
    if todosDigitosIguales(str(num)):
        print(8)
        return
    tmp = num
    i = 0
    while tmp != 6174:
        tmp = '{:0>4}'.format(tmp)
        tmp = list(str(tmp))
        tmp.sort(reverse=True)
        tmp = "".join(tmp)
        numRev = "".join(reversed(tmp))
        tmp = int(tmp) - int(numRev)
        i += 1

    print(i)


cantDeNum = input("ingrese cantidad de casos de prueba\n")
lista = list()
for i in range(int(cantDeNum)):

    while True:
        num = input(f"ingrese num {i}: ")

        if not(num.isnumeric()):
            print("Solo puede ingresar numeros")
            continue
        elif len(num) != 4:
            print("El numero debe tener 4 digitos")
            continue
        elif int(num) < 0:
            print("El numero debe ser positivo")
            continue
        else:
            lista.append(int(num))
            break

print(f"\nLos numeros son:\n{lista}")

for n in lista:
    kaprekar(n)

