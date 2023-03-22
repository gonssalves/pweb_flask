from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('form.html')


@app.route("/valida", methods=['POST', 'GET'])
def valida_sessao():
    if request.method == 'POST':
        requests = request.form
        requests2 = requests.copy()
    
        diaNascimento = request.form['diaNascimento']
        mesNascimento = request.form['mesNascimento']
        anoNascimento = request.form['anoNascimento']

        dataNascimento = f'{diaNascimento}-{mesNascimento}-{anoNascimento}'
        dataFormato = '%d-%m-%Y'

        try: 
           datetime.datetime.strptime(dataNascimento, dataFormato)
           
        except ValueError: 
            requests2['nascimento'] = ''
 
        ddd = request.form['ddd']
        listaDDD = [61, 62, 64, 65, 66, 67, 82, 71, 73, 74, 75, 77, 85, 88, 98, 99, 83, 81, 87, 86, 89, 84, 79, 68, 96, 92, 97, 91, 93, 94, 69, 95, 63, 27, 28, 31, 32, 33, 34, 35, 37, 38, 21, 22, 24, 11, 12, 13, 14, 15, 16, 17, 18, 19, 41, 42, 43, 44, 45, 46, 51, 53, 54, 55, 47, 48, 49]
        
        try:
            if not int(ddd) in listaDDD:
                requests2['ddd'] = ''
        except:
            requests2['ddd'] = ''

        email = request.form['email']
        
        if '.' not in email or '@' not in email:
            requests2['email'] = ''
        
        atv_extra = request.form.getlist('atv_extra')
        
        if len(atv_extra) > 3:
            requests2['atv_extra'] = ''         

        data2 = {}

        for key, value in requests2.items():
            if value == '':
                data2[key] = value

        try:
            request.form['turno']
        except:
            data2['turno'] = ''


        if len(request.form['tel']) == 9:
            try:
                t = int(request.form['tel'])
            except:
                data2['tel'] = ''
        else:
            data2['tel'] = ''

        try:
            int(request.form['ramal'])
        except:
            data2['ramal'] = ''
        
        return render_template('resposta.html', data=requests2, data2 = data2, requests=requests)
