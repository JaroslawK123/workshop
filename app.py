from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Global Azure 2025!<br>Dzisiaj jest 01.10.2025 środa - warsztaty z Azure"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)