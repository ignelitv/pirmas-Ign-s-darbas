from flask import Flask, request, render_template_string

app = Flask(__name__)

history = []

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
    
    history_items = "".join([f"<li>{item}</li>" for item in history])

    template = """
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
                    
                    <h2>Veiksmų istorija:</h2>
                    <ul>
                        {% for item in history_items %}
                            <li>{{ item }}</li>
                        {% endfor %}
                    </ul>
                </body>
                </html>
            """
    return render_template_string(template, history=history)

@app.route("/skaiciuotuvas", methods =['POST'])
def skaiciuoti():
    expression = request.form['expression']
    try:
        num1, operacija, num2 = expression.split() #išskaidoma išraiška į tris elementus atskiriant juos pagal tarpus
        num1 = float(num1)
        num2 = float(num2)

    
        if operacija == '+':
            result = sudetis(num1, num2)

        elif operacija == '-':
            result = atimtis (num1, num2)

        elif operacija == '*':
            result = daugyba (num1, num2)

        elif operacija == '/':
            result = dalyba (num1, num2)

        history.append(f"{num1} {operacija} {num2} = {result}")
        print(history)

        return f"Rezultatas: {result}" #Jeigu išraiška įvesta teisingai, išspausdinamas gautas rezultatas
    except Exception as e:
        error = f"Įvyko klaida įvertinant išraiską: {e}" #Jeigu programa išraiškos nesupranta, išspausdinama žinutė, kad nepavyko gauti rezultato
        return f"Klaida: {error}"

if __name__ == '__main__':
    app.run() #Programos paleidimas







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