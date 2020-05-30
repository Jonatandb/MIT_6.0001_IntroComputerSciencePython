###################
## EXAMPLE: strings
###################
# pal1 = "Jonatandb"
# pal2 = "Está estudiando Python"
# pal3 = "."
# print(pal1, pal2 + pal3 * 3)
# Con la coma se separan los strings con espacios
# Con la concatenación con + hay que agregar espacios
# Con la multiplicación se repite n veces un string


####################
## EXAMPLE: input
####################
# text = input("Escriba algo: ")
# print("Texto ingresado * 5 -> ", 5 * text)
# num = int(input("Esciba un número entero: "))
# print("Número ingresado * 5 -> ", 5 * num)


# Casteo de datos
# ingreso1 = input("Ingrese un entero: ")
# print("type(ingreso1) -> ", type(ingreso1))
# print("print() siempre devuelve un string")
# print("")
# ingreso2 = input("Ingrese otro entero: ")
# print("type(int(ingreso2)) -> ", type(int(ingreso2)))
# print("")
# ingreso3 = input("Ingrese un decimal: ")
# print("type(float(ingreso3)) -> ", type(float(ingreso3)))


# Range
# range(start, stop, step) devuelve un conjunto de números
#   se le pueden pasar 1, 2 o 3 parámetros
# si se pasa un parámetro, se usa como último número
#   stop nunca se incluye en el resultado
#   si no se especifíca start, siempre comienza por 0
# result1 = ""
# for i in range(10):
#     result1 += str(i)
# print("range(10) ->", range(10), "->", result1)

# Si se pasan dos parámetros, se toman como start y stop
# result2 = ""
# for i in range(4, 10):
#     result2 += str(i)
# print("range(4, 10) ->", range(4, 10), "->", result2)

# Si se pasan tres parámetros, se toman como start, stop y step
# result3 = ""
# for i in range(4, 10, 2):
#     result3 += str(i)
# print("range(4, 10, 2) ->", range(4, 10, 2), "->", result3)

####################
## TEST YOURSELF!
## Modify the perfect squares example to print
## imaginary perfect sqrts if given a negative num.
####################
## Perfect squares
####################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
if neg_flag:
    while ans ** 2 < -x:
        ans = ans + 1
    if ans ** 2 == -x:
        print("Square root of", x, "is", str(ans) + "i")
    else:
        print(-x, "is not a perfect square")
else:
    while ans ** 2 < x:
        ans = ans + 1
    if ans ** 2 == x:
        print("Square root of", x, "is", ans)
    else:
        print(x, "is not a perfect square")
