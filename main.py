
def sudetis(x,y):
    return x + y

def atimtis(x,y):
    return x - y

def daugyba(x,y):
    return x * y

def dalyba(x,y):
    if y == 0:
        print("Dalyba is nulio negalima!")
        return
    else:
        return x / y


#meniu pasirinkimas:
while True:
    try:
         skaiciai_ir_operacija = input("Iveskite skaicius ir operacija (pvz.: 5+7): ")
         skaiciai_ir_operacija = skaiciai_ir_operacija.split()

         num1 = float(skaiciai_ir_operacija[0])
         operacija = skaiciai_ir_operacija[1]
         num2 = float(skaiciai_ir_operacija[2])

    except ValueError:
         print("Neteisinga ivestis. Pasirinkite dar karta.")
         continue

        #pasirinktų operacijų įgyvendinimas: 
    if operacija == '+':
        print(num1, "+", num2, "=", sudetis(num1, num2))

    elif operacija == '-':
        print(num1, "-", num2, "=", atimtis(num1, num2))

    elif operacija == '*':
        print(num1, "*", num2, "=", daugyba(num1, num2))

    elif operacija == '/':
        print(num1, "/", num2, "=", dalyba(num1, num2))


        kitas_skaiciavimas = input("Ar norite atlikti dar viena operacija? (taip/ne): ")
        if kitas_skaiciavimas == "ne":
            break
