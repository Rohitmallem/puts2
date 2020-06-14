from flask import Flask, request
from fractions import Fraction
from decimal import Decimal
app = Flask(__name__)
@app.route('/')
def index():
    return 'Usage;\nOperation?A=<value1>&B=<value2>\n'

@app.route('/mul')
def multiplication():
    try:
        value1=request.args.get('A',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value1='Nothing'
    try:
        value2=request.args.get('B',default = 0, type = Fraction)
    except ZeroDivisionError as error:
        value2='Nothing'
    if value1 == 'Nothing' or value2 == 'Nothing' :
        return 'Nothing'
    else:
        E = Fraction(value1)
        F = Fraction(value2)
        return str(float(A*B))

if __name__ == "__main__":
    app.run()
