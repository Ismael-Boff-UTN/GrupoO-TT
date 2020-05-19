
#función que obtiene los números ordenados
def constante(numeros):
#transformo los numeros a string
    numeros=str(numeros)


#inicializo 2 vectores
    digito=[]
    digitoInverso=[]


#agrego 0 para casos de números de menos de 4 dígitos
    for n in numeros:
       n = int(n)
       digito.append(n)
       digitoInverso.append(n)
    while (len(digito)!=4):
      digito.append(0)
      digitoInverso.append(0)


#ordeno los 2 números uno ascendente otro descendente
    digito.sort()

    digitoInverso.sort(reverse=True)
#transformo los vectores en una sola cadena y luego en int
    cadena=[str(i) for i in digito]
    cuenta2= int("".join(cadena))
    cadena = [str(i) for i in digitoInverso]
    cuenta1 = int("".join(cadena))






#retorno el número ordenado ascendente y descendente
    return cuenta1, cuenta2

# función que hace la operación matemática y devuelve el resultado
def resta(cuenta1,cuenta2):
    resultado = cuenta1-cuenta2
    return resultado
#declaro el vector que va a tener todos los casos
todos_los_resultados=[]
#pregunto la cantidad de casos a comprobar
casos = int(input("declare cuantos casos desea comprobar"))
#declaro una variable de control de iteraciones
repeticion = 0
while (repeticion!=casos):
    repeticion+=1
    #declaro un contador para ver las veces que itera el programa hasta llegar a 6174
    contador=0
   #compruebo que el número sea de 4 cifras o menos
    resultado= input("ingrese un número de 4 dígitos que tenga al menos 2 números diferentes")
    while (len(resultado)>4):
     print("debe ingresar un número de 4 cifras o menor")
     resultado = input("ingrese un número de 4 dígitos que tenga al menos 2 números diferentes")
    # tomo el input y lo transformo en int
    resultado = int(resultado)


    #declaro un while, en caso de que los números fueran todos iguales el programa tendería a infinito por lo cual a la 8va iteración se que se han ingresado números iguales y corto la iteración
    while (resultado!=6174 and contador!=8):
        cuenta1, cuenta2= constante(resultado)
        resultado = resta(cuenta1,cuenta2)
        contador+=1

    todos_los_resultados.append(contador)

#muestro los resultados
print("El resultado de las iteraciones es " + str(todos_los_resultados))



