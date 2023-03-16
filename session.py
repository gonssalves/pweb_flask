from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/valida", methods=['POST', 'GET'])
def valida_sessao():
    if request.method == 'POST':
        requests = request.form

        requests_dict = requests.copy()
        
        for value in requests_dict:
            if requests_dict[value] == '':
                    return render_template('resposta_invalida.html')
        
        diaNascimento = request.form['diaNascimento']
        mesNascimento = request.form['mesNascimento']
        anoNascimento = request.form['anoNascimento']

        dataNascimento = f'{diaNascimento}-{mesNascimento}-{anoNascimento}'
        dataFormato = '%d-%m-%Y'

        try: data = datetime.datetime.strptime(dataNascimento, dataFormato)

        except ValueError: return render_template('resposta_invalida.html')

        # diaNascimento = request.form['diaNascimento']
        # if int(diaNascimento) < 1 or int(diaNascimento) > 31:
        #     return render_template('resposta_invalida.html')
        
        # mesNascimento = request.form['mesNascimento']
        # if int(mesNascimento) < 1 or int(mesNascimento) > 12:
        #     return render_template('resposta_invalida.html')
        
        # anoNascimento = request.form['anoNascimento']
        # if int(anoNascimento) < 1000 or int(anoNascimento) > 9999:
        #     return render_template('resposta_invalida.html')
        
        ddd = request.form['ddd']
        listaDDD = [61, 62, 64, 65, 66, 67, 82, 71, 73, 74, 75, 77, 85, 88, 98, 99, 83, 81, 87, 86, 89, 84, 79, 68, 96, 92, 97, 91, 93, 94, 69, 95, 63, 27, 28, 31, 32, 33, 34, 35, 37, 38, 21, 22, 24, 11, 12, 13, 14, 15, 16, 17, 18, 19, 41, 42, 43, 44, 45, 46, 51, 53, 54, 55, 47, 48, 49]

        if not int(ddd) in listaDDD:
            return render_template('resposta_invalida.html')

        email = request.form['email']
        
        if '.' not in email or '@' not in email:
            return render_template('resposta_invalida.html')
    
        atv_extra = request.form.getlist('atv_extra')
        
        if len(atv_extra) > 3:
            return render_template('resposta_invalida.html')
        else:
            return render_template('resposta_valida.html')
            
    else: 
        return 'estou esperando um post'