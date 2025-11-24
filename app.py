from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traefik — Estefany</title>

    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: linear-gradient(135deg, #5A8DEE, #699AF9, #A3C7FF);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            color: #333;
        }

        /* Header */
        header {
            background: white;
            padding: 20px 40px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        header h2 {
            margin: 0;
            color: #005eff;
        }

        nav button {
            background: #005eff;
            color: white;
            border: none;
            padding: 10px 18px;
            margin-left: 12px;
            border-radius: 8px;
            cursor: pointer;
            font-size: 15px;
            transition: 0.2s;
        }

        nav button:hover {
            background: #003bbb;
        }

        /* Contenedor */
        .container {
            margin-top: 80px;
            display: flex;
            justify-content: center;
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 4px 30px rgba(0,0,0,0.2);
            text-align: center;
            width: 450px;
            animation: fadeIn 0.8s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1 {
            color: #333;
            margin-bottom: 12px;
        }

        p {
            color: #555;
            font-size: 17px;
        }

        .tag {
            background: #005eff;
            color: white;
            padding: 8px 16px;
            border-radius: 50px;
            display: inline-block;
            margin-top: 12px;
            font-size: 14px;
        }

        footer {
            margin-top: 45px;
            text-align: center;
            color: white;
            opacity: 0.8;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <h2>🔥 Proyecto CI/CD</h2>
        <nav>
            <button onclick="alert('Este es un demo 😊')">Inicio</button>
            <button onclick="alert('Desplegado con Traefik, Docker y CI/CD')">Tecnologías</button>
            <button onclick="alert('Creado por Estefany ❤️')">Sobre mí</button>
        </nav>
    </header>

    <!-- Contenido -->
    <div class="container">
        <div class="card">
            <h1>🚀 Traefik + Flask</h1>
            <p>Proyecto CI/CD desarrollado por <strong>Estefany</strong>.</p>
            <p>Esta aplicación está completamente automatizada y desplegada en un servidor real.</p>

            <div class="tag">Traefik Reverse Proxy</div><br>
            <div class="tag">Docker Swarm</div><br>
            <div class="tag">GitHub Actions</div><br>
            <div class="tag">SSL Let’s Encrypt</div>
        </div>
    </div>

    <footer>© 2025 — Desarrollado con ❤️ por Estefany</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
