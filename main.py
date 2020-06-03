from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\nOperation?A=<input1>&B=<input2>\n'

@app.route('/add')
def addition():
    try:
        input1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        input1='None'
    try:
        input2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        input2='None'
    if input1 == 'None' or input2 == 'None' :
        return 'None'
    else:
        C = Fraction(input1)
        D = Fraction(input2)
        return str(float(C+D))#removed round function and results in float

@app.route('/sub')
def subtraction():
    try:
        input1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        input1='None'
    try:
        input2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        input2='None'
    if input1 == 'None' or input2 == 'None' :
        return 'None'
    else:
        C = Fraction(input1)
        D = Fraction(input2)
        return str(float(C-D))


if __name__ == "__main__":
    app.run()
