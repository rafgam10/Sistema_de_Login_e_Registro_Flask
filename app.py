from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


#Code:
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
            
        nome = request.form.get('username')
        senha = int(request.form.get('password'))
        AtivoOrNao = bool(request.form.get('ativo') == "on")

        if nome == "Rafael" and senha == 123 or AtivoOrNao == True:
            print(f"{nome} e {senha}: {AtivoOrNao}")
            
            return redirect(url_for('base'))
        
        return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    pass


#Base de registro:

registo = []


@app.route("/base")
def base():



    return render_template("base.html")



if __name__ == "__main__":
    app.run(debug=True)