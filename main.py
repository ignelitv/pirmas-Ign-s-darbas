from flask import Flask, render_template, request, redirect, url_for
import math

app = Flask(__name__)

def skaiciuoti_rezultata(num1, num2, operatorius):
    try:
        if operatorius == 'sudėti':
            return num1 + num2
        elif operatorius == 'atimti':
            return num1 - num2
        elif operatorius == 'dauginti':
            return num1 * num2
        elif operatorius == 'dalinti':
            if num2 != 0:
                return num1 / num2
            else:
                raise ZeroDivisionError("Dalyba iš nulio negalima!")
        elif operatorius == 'kvadratinė_šaknis':
            if num1 >= 0:
                return math.sqrt(num1)
            else:
                raise ValueError("Negalima skaičiuoti kvadratinės šaknies iš neigiamo skaičiaus!")
        elif operatorius == 'kvadratu':
            return num1 ** 2
        elif operatorius == 'faktorialas':
            if num1 >= 0:
                return math.factorial(num1)
            else:
                raise ValueError("Faktorialas negali būti skaičiuojamas iš neigiamo skaičiaus!")
        elif operatorius == 'sinusas':
            return math.sin(num1)
        elif operatorius == 'kosinusas':
            return math.cos(num1)
        else:
            raise ValueError("Neteisingas operatorius!")
    except (ValueError, ZeroDivisionError) as e:
        return str(e)  # Pakeičiame grąžinimą į string'ą, kad nebūtų grąžinamas None


@app.route('/')
def skaiciuotuvas():
    return render_template('skaiciuotuvas.html')

@app.route('/skaiciuoti', methods=['POST'])
def atlikti_skaiciavima():
    try:
        num1 = float(request.form['num1'])
        operatorius = request.form['operatorius']
        if operatorius not in ['kvadratinė_šaknis', 'kvadratu', 'faktorialas', 'sinusas', 'kosinusas']:
            num2 = float(request.form['num2'])
        else:
            num2 = None
        
        if operatorius == 'faktorialas':
            if num1.is_integer() and num1 >= 0:
                num1 = int(num1)
            else:
                raise ValueError("Faktorialas gali būti skaičiuojamas tik sveikam teigiamam skaičiui!")
        
        rezultatas = skaiciuoti_rezultata(num1, num2, operatorius)
        return render_template('skaiciuotuvas.html', rezultatas=rezultatas, num1=num1, num2=num2, operatorius=operatorius)
    except ValueError as e:
        return render_template('skaiciuotuvas.html', rezultatas=str(e), num1=request.form['num1'], num2=request.form['num2'], operatorius=request.form['operatorius'])

if __name__ == '__main__':
    app.run(debug=True)
