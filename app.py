from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traefik — estefany</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            text-align: center;
            width: 420px;
        }

        h1 {
            color: #444;
            margin-bottom: 10px;
        }

        p {
            color: #666;
            font-size: 18px;
        }

        .tag {
            background: #005eff;
            color: white;
            padding: 6px 14px;
            border-radius: 50px;
            display: inline-block;
            margin-top: 15px;
        }
    </style>
</head>
<body>

    <div class="card">
        <h1>🚀 Traefik + Flask</h1>
        <p>Proyecto CI/CD desarrollado por <strong>estefany</strong>.</p>
        <p>Esta aplicación está desplegada con:</p>

        <div class="tag">Traefik Reverse Proxy</div><br>
        <div class="tag">Docker Swarm</div><br>
        <div class="tag">GitHub Actions</div><br>
        <div class="tag">SSL Let’s Encrypt</div>
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
