from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/valida", methods=['POST'])
def valida_sessao():
    if request.method == 'POST':
        if request.form.get('nomeAluno'):
            nomeAluno = request.form['nomeAluno']
        else:
            return render_template("resposta.html")
        
        if request.form.get('diaNascimento'):
            diaNascimento = request.form['diaNascimento']
            if int(diaNascimento) > 0 and int(diaNascimento) < 32:
                temp = 'temp'
            else:
                return render_template('resposta.html')
        
        if request.form.get('mesNascimento'):
            mesNascimento = request.form['mesNascimento']
            if int(mesNascimento) > 0 and int(mesNascimento) < 13:
                temp = 'temp'
            else:
                return render_template('resposta.html')
        
        if request.form.get('anoNascimento'):
            anoNascimento = request.form['anoNascimento']
            if int(anoNascimento) > 999 and int(anoNascimento) < 10000:
                temp = 'temp'
            else:
                return render_template('resposta.html')
         
        if request.form.get('nomePai'):
            nomeMae = request.form['nomeMae']
        else:
            return render_template('resposta.html')
        
        if request.form.get('nomePai'):
            nomePai = request.form['nomePai']
        else:
            return render_template('resposta.html')
        
        if request.form.get('ddd'):
            ddd = request.form['ddd']
            listaDDD = [61, 62, 64, 65, 66, 67, 82, 71, 73, 74, 75, 77, 85, 88, 98, 99, 83, 81, 87, 86, 89, 84, 79, 68, 96, 92, 97, 91, 93, 94, 69, 95, 63, 27, 28, 31, 32, 33, 34, 35, 37, 38, 21, 22, 24, 11, 12, 13, 14, 15, 16, 17, 18, 19, 41, 42, 43, 44, 45, 46, 51, 53, 54, 55, 47, 48, 49]
            if int(ddd) in listaDDD:
                temp = temp
            else:
                return render_template('resposta.html')
        
        if request.form.get('tel'):
            tel = request.form['tel']
        else:
            return render_template('resposta.html')
        
        if request.form.get('ramal'):
            ramal = request.form['ramal']
        else:
            return render_template('resposta.html')
        
        if request.form.get('email'):
            email = request.form['email']
            if '@' in email and '.' in email:
                temp = 'temp'
            else:
                return render_template('resposta.html')
        
        if request.form.get('turno'):
            turno = request.form['turno']
        else:
            return render_template('resposta.html')
        
        atv_extra = request.form.getlist('atv_extra')
        
        if len(atv_extra) > 3:
            return render_template('resposta.html')
        else:
            return f'<h1>Dados válidos</h1>'
        
    else: 
        return 'estou esperando um post'

