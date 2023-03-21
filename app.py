from flask import Flask, render_template,redirect,request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()





app = Flask(__name__)
app.secret_key = "pingu"


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA")
}


app.config.update(mail_settings)
mail = Mail(app)


class Contato:
    def __init__(self,nome,email,msg):
        self.nome = nome
        self.email = email
        self.msg = msg


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == "POST":
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["msg"],
        )
        msgs = Message(
            subject=f'{formContato.nome} envio mensagem do Portfolio',
            sender= app.config.get("MAIL_USERNAME"),
            recipients=['afaethy@gmail.com'],
            body=f'''
                    {formContato.nome} entrou em contato pelo {formContato.email}, te envio a 
                    seguite mensagem:
                    
                    {formContato.msg}
                
                    '''
            
        )
        mail.send(msgs)
        flash("Mensagem Enviada com sucesso!")
        
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True),