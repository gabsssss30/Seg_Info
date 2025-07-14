from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Rota pública para mostrar informações auto
@app.route('/informacoesauto')
def informacoes_auto():
    return render_template('auto.html')

# Rota pública para mostrar informações emp
@app.route('/informacoesemp')
def informacoes_emp():
    return render_template('emp.html')

if __name__ == '__main__':
    app.run(debug=True)
