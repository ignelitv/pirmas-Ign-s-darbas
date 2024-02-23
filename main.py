
from flask import Flask, request

app = Flask(__name__)

def sudetis(x,y):
    return x + y

def atimtis(x,y):
    return x - y

def daugyba(x,y):
    return x * y

def dalyba(x,y):
    if y == 0:
        print("Dalyba is nulio negalima!")
    else:
        return x / y

@app.route("/")
def hello_world():
    return f"""
                <!DOCTYPE html>
                <html lang="lt">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Skaičiuotuvas</title>
                </head>
                <body>
                    <form action="/skaiciuotuvas" method="post">
                        <label for="expression">Įveskite išraišką:</label>
                        <input type="text" id="expression" name="expression">
                        <button type="submit">Skaičiuoti</button>
                    </form>
                </body>
                </html>
            """


@app.route("/skaiciuotuvas", methods =['POST'])
def skaiciuoti():
    expression = request.form['expression']
    try:
        num1, operacija, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)


    
        if operacija == '+':
            result = sudetis(num1, num2)

        elif operacija == '-':
            result = atimtis(num1, num2)

        elif operacija == '*':
            result = daugyba(num1, num2)

        elif operacija == '/':
            result = dalyba(num1, num2)

        return f"Rezultatas: {result}"
    except Exception as e:
        return f"Įvyko klaida įvertinant išraiską: {e}"


if __name__ == '__main__':
    app.run() 







"""
def sudetis(x,y):
    return x + y

def atimtis(x,y):
    return x - y

def daugyba(x,y):
    return x * y

def dalyba(x,y):
    if y == 0:
        print("Dalyba is nulio negalima!")
        returnut("Iveskite skaicius ir operacija (pvz.: 5+7): ")

    else:
        return x / y


#meniu pasirinkimas:
while True:

    skaiciai_ir_operacija = inp
    if len(skaiciai_ir_operacija) != 3 or skaiciai_ir_operacija[1] not in ['+', '-','*', '/']:
        print ("Neteisingas formatas!")
        continue
    
    num1, operacija, num2 = skaiciai_ir_operacija

    num1 = float(num1)
    num2 = float(num2)


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
"""