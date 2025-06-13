#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    output = '\n'.join(str(i) for i in range(param)) + '\n'
    return Response(output, mimetype='text/plain')

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return Response("Error: Division by zero", mimetype='text/plain')
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return Response("Error: Modulo by zero", mimetype='text/plain')
        result = num1 % num2
    else:
        return Response("Error: Invalid operation", mimetype='text/plain')
    
    return Response(str(result), mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
