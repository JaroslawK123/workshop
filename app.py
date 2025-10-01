from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body {
                background-color: #0074D9;
                color: white;
                font-family: Arial, sans-serif;
            }
            .top-bar {
                display: flex;
                justify-content: flex-end;
                align-items: center;
                padding: 20px;
            }
            .hello-btn {
                background-color: #FFDC00;
                color: #0074D9;
                border: none;
                padding: 10px 20px;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="top-bar">
            <button class="hello-btn">Dzień dobry</button>
        </div>
        <div style="padding: 40px;">
            <h1>Hello, Global Azure 2025!</h1>
            <p>Dzisiaj jest 01.10.2025 środa - warsztaty z Azure</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)