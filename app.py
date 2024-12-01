from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'CICD Pipeline updated'

if __name__ == '__main__':
    app.run()

