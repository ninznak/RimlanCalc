
romanSimple = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")

romanSimple2 = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", "C")

romanBig = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M")

desision = input("Введите арифметическое выражение: \n")

romeDigits = {"": 0, "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10}



def converter(xx):  # конвертирует большие цифры в римские до 1000
    if (xx > 0):
        if (xx > 0 and xx <= 10):
            returnRoman = romanSimple[xx - 1]
        elif (xx > 10 and xx < 100):
            returnRoman = romanSimple2[xx // 10] + romanSimple[xx % 10]
        elif (xx == 100 or xx > 100 and xx <= 1000):
            returnRoman = (romanBig[xx // 100] + romanSimple2[(xx % 100) // 10]
                           + romanSimple[xx % 10])
    else:
        print("Error")
    return returnRoman


def processing(x):  # разделение на части и проверка на корректность лействий

    if "*" in x:
        x = x.split("*")
    elif "+" in x:
        x = x.split("+")
    elif "-" in x:
        x = x.split("-")
    elif "/" in x:
        x = x.split("/")
    else:
        raise Exception
    return x


def argumentTypes(x, y):  # определение типа аргументов и их корректности справа и слева
    if (x in romanSimple) and (y in romanSimple):
        arg1 = romeDigits[x]
        arg2 = romeDigits[y]
        return converter(resultA(arg1, arg2))
    elif (int(x) in romeDigits.values() and int(y) in romeDigits.values()):
        arg1 = int(x)
        arg2 = int(y)
        return resultA(arg1, arg2)
    else:
        raise Exception


def resultA(x, y):  # вычисление результата

    if "*" in desision:
        answer = x*y
    elif "+" in desision:
        answer = x+y
    elif "-" in desision:
        answer = x-y
    elif "/" in desision:
        answer = x/y
    #else:
        #raise Exception
    return answer


massiv = processing(desision)

#print(massiv) // проверка что в массиве на выходе

print(argumentTypes(massiv[0], massiv[1])) # печать результата