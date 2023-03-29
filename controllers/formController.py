from flask import render_template
from models.formModel import validate_logic, insert_values

def index():
    return render_template('form.html')

def validate():
    data = validate_logic()

    if len(data) >= 1:
        return render_template('resposta.html', data=data)
    else:
        return view()

def view():
    tabela = insert_values()

    return render_template('viewStudents.html', tabela=tabela)