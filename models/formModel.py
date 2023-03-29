import sqlite3
import datetime
from flask import request
#from controllers.formController import response

def validate_logic():
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
                requests2['DDD'] = ''
        except:
            requests2['DDD'] = ''

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

        return data2


        #return insert_values

def insert_values():
    con = sqlite3.connect('pweb.db')
    cur = con.cursor()

    dicio = request.form

    nomeAluno = dicio['nomeAluno']
    dataa = f"{dicio['diaNascimento']}-{dicio['mesNascimento']}-{dicio['anoNascimento']}"
    nomeMae = dicio['nomeMae']
    nomePai = dicio['nomePai']
    telefone = f"({dicio['ddd']}) {dicio['tel']} {dicio['ramal']}"
    serie = dicio['serie']
    turno = dicio['turno']
      

    cur.execute('''CREATE TABLE IF NOT EXISTS formulario (alu_id integer primary key autoincrement, nom_aluno text, dat_nascimento text, nom_mae text, nom_pai text, tel text, serie text, turno text)''')
    
    cur.execute("INSERT INTO formulario VALUES (?, ?, ?, ?, ?, ?, ?)", (nomeAluno, dataa, nomeMae, nomePai, telefone, serie, turno))
    
    #cur.execute("INSERT INTO formulario VALUES (?, ?, ?, ?, ?, ?, ?)", (nomeAluno, dataa, nomeMae, nomePai, telefone, serie, turno))
    
    
    con.commit()

    for row in cur.execute('SELECT * FROM formulario'):
        print(row)

    cur.execute('SELECT * FROM formulario')

    result = cur.fetchall()

    return result
    # cur.execute('DROP TABLE formulario')

    #con.commit()

    #con.close