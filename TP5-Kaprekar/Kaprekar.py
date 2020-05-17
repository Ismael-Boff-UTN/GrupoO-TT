

tab = []
loop = 'loop'


# tab will hold all Kaprekar numbers found
# loop is just for better wording

def asc(n):
    # Organizo los numeros en ASCENDENTE
    return int(''.join(sorted(str(n))))


def desc(n):
    # Organizo los números de forma DESCENDENTE
    return int(''.join(sorted(str(n))[::-1]))


n = input("Escribe Un Número : ")
try:
    n = int(n)
except:
    # Asumiendo que el numero es 2016 para evitar que crashee mi programa
    print("\nNumero Invalido!!!\nAsumiendo numero = 2016.")
    n = "2016"
print("\nTransformando ", str(n) + ":")

while True:
    # voy iterando, asignando la nueva diferencia
    print(desc(n), "-", asc(n), "=", desc(n) - asc(n))
    n = desc(n) - asc(n)

    if n not in tab:
        # chequeo si el numero ya existe
        tab.append(n)
    else:
        if tab.index(n) == len(tab) - 1:

            tab = []
            tab.append(n)
            loop = 'constant'
        else:

            tab = tab[tab.index(n):]

        break

print('Kaprekar', loop, 'Alcanzado :', tab)