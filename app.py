from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime')
def bem_vindo():
    hora = datetime.now()
    hora_output = f'{hora.strftime("%d")}/{hora.strftime("%m")}/{hora.strftime("%Y")} {hora.strftime("%H")}:{hora.strftime("%M")}:{hora.strftime("%S")} {hora.strftime("%p")}'
    saudacao = "Boa noite!"
    if hora.strftime("%H") < "12":
        saudacao = "Bom dia!"
    elif hora.strftime("%H") < "18":
        saudacao = "Boa tarde!"


    return {"current_datetime": hora_output, "message": saudacao}

    
