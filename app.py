from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify('Hello, Welcome to simple calculation!')

@app.route('/api/calculator', methods=['POST'])
def calculator():
    # Get the request data
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operation = data['operation']

    # Perform the requested operation
    if operation == 'add':
        result = num1 + num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    elif operation == 'subtract':
        result = num1 - num2
    else:
        return jsonify({'error': 'Invalid operation! Please specify a valid operation: add, multiply, divide, or subtract'}), 400

    # Return the result as a JSON object
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()

# Result:
"""
import requests

url = 'http://localhost:5000/api/calculator'
data = {'num1': 99, 'num2': 30, 'operation': 'divide'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)

print(response.json())

"""

"""
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()

"""