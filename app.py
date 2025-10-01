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
            .bottom-img {
                position: fixed;
                bottom: 10px;
                left: 50%;
                transform: translateX(-50%);
                width: 180px;
                height: auto;
                z-index: 10;
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
        <div class="bottom-img">
            <!-- Przykładowy SVG rycerza z zieloną tarczą i mieczem -->
            <svg width="180" height="120" viewBox="0 0 180 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- Tarcza -->
                <ellipse cx="50" cy="90" rx="25" ry="30" fill="#1aff1a" stroke="#006400" stroke-width="4"/>
                <!-- Miecz -->
                <rect x="120" y="40" width="10" height="50" fill="#1aff1a" stroke="#006400" stroke-width="2"/>
                <rect x="118" y="35" width="14" height="10" fill="#b3b3b3" stroke="#333" stroke-width="2"/>
                <!-- Rycerz: głowa -->
                <circle cx="80" cy="60" r="18" fill="#cccccc" stroke="#333" stroke-width="3"/>
                <!-- Rycerz: tułów -->
                <rect x="70" y="78" width="20" height="30" fill="#cccccc" stroke="#333" stroke-width="3"/>
                <!-- Rycerz: ręka -->
                <rect x="60" y="85" width="10" height="8" fill="#cccccc" stroke="#333" stroke-width="2"/>
                <rect x="90" y="85" width="10" height="8" fill="#cccccc" stroke="#333" stroke-width="2"/>
                <!-- Rycerz: nogi -->
                <rect x="75" y="108" width="6" height="12" fill="#333"/>
                <rect x="89" y="108" width="6" height="12" fill="#333"/>
            </svg>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)