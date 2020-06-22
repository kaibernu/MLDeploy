from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def home():
    return "Bem-Vindo"


@app.route('/calculo')
def add():
    a = 10
    b = 10

    return str(a+b)



if __name__ == '__main__':
    app.run()
