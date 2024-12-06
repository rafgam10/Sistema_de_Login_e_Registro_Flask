from flask import Flask, render_template, request

app = Flask(__name__)


#Code:
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['username']
        senha = request.form['password']
        lembreAtivo = bool(request.form['ativo'])
        if lembreAtivo:
            print(f"{nome} e {senha}: {lembreAtivo}")
        return "Login com Sucesso!"
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)