from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='Treehouse'):
    name = request.args.get('name', name)
    return render_template('index.html', name=name)

@app.route('/<int:number1>/<int:number2>')
@app.route('/<float:number1>/<float:number2>')
@app.route('/<float:number1>/<int:number2>')
@app.route('/<int:number1>/<float:number2>')
def add(number1, number2):
    context = {'num1': number1, 'num2': number2}
    return render_template('add.html', **context)

@app.route('/multiply/<int:number1>/<int:number2>')
@app.route('/multiply/<float:number1>/<float:number2>')
@app.route('/multiply/<float:number1>/<int:number2>')
@app.route('/multiply/<int:number1>/<float:number2>')
@app.route('/multiply/')
def multiply(number1=5, number2=5):
    context = {'num1': number1, 'num2': number2}
    return render_template('multiply.html', **context)

app.run(debug=True, port=8000, host='0.0.0.0')