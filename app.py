from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/args')
def ArgumentosURL():
    print(request.args)
    return 'args'

@app.route('/file')
def FileURL():
    print(request.files)
    return 'files'

@app.route('/values')
def ValueURL():
    print(request.values)
    return 'value'

@app.route('/form', methods = ['POST'])
def FormURL():
    print(request.form)
    return 'form'

@app.route('/JSON', methods = ['POST'])
def JsonURL():
    print(request.get_json())
    return 'json'

#main
if __name__ == '__main__':
    app.run()
