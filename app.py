from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"