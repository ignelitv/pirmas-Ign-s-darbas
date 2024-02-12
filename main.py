
def sudetis(x,y):
    return x + y

def atimtis(x,y):
    return x - y

def daugyba(x,y)
    return x * y

def dalyba(x,y)
    return x / y

print("Pasirinkite operacija:")
print("1. Sudetis")
print("2. Atimtis")
print("3. Daugyba")
print("4. Dalyba")

while true:
    pasirinkimas = input("Iveskite pasirinkima (1/2/3/4): ")

    if pasirinkimas in ('1', '2', '3', '4'):
        try:
            num1 = float(input("iveskite pirmaji skaiciu: "))
            num2 = float(input("iveskite antraji skaiciu: "))
        except valueerror:
            print("Neteisinga ivestis. Pasirinkite dar karta.")
            continue

        if pasirinkimas == '1':
            print(num1, "+", num2, "=" sudetis(num1, num2))
