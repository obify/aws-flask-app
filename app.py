from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'CICD Pipeline 2024'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

