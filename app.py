from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Traefik — EGrupo 2</title>

    <!-- ICONOS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

    <!-- ESTILOS -->
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f5f7ff;
            color: #333;
        }

        /* ---------------- HEADER ---------------- */
        header {
            background: white;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            position: sticky;
            top: 0;
            z-index: 10;
        }

        header h2 {
            margin: 0;
            color: #0056ff;
            font-size: 26px;
        }

        nav a {
            margin-left: 25px;
            color: #333;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            transition: 0.3s;
        }

        nav a:hover {
            color: #0056ff;
        }

        /* ---------------- HERO ---------------- */
        .hero {
            background: url('https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80') no-repeat center/cover;
            height: 75vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            padding: 20px;
        }

        .hero h1 {
            font-size: 48px;
            text-shadow: 0 3px 8px rgba(0,0,0,0.4);
        }

        .hero p {
            font-size: 20px;
            max-width: 700px;
            margin: 20px auto;
        }

        .hero button {
            background: #0056ff;
            border: none;
            padding: 14px 28px;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
            transition: 0.3s;
        }

        .hero button:hover {
            background: #003dbb;
        }

        /* ---------------- FEATURES ---------------- */
        .features {
            padding: 60px 40px;
            text-align: center;
        }

        .features h2 {
            font-size: 36px;
            margin-bottom: 40px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 25px;
            max-width: 1100px;
            margin: auto;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
            transition: 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card i {
            font-size: 45px;
            color: #0056ff;
            margin-bottom: 15px;
        }

        .card h3 {
            margin-bottom: 10px;
            font-size: 22px;
        }

        .card p {
            color: #666;
        }

        /* ---------------- FOOTER ---------------- */
        footer {
            background: #0d1b3d;
            padding: 25px;
            text-align: center;
            color: white;
            margin-top: 60px;
        }
    </style>
</head>
<body>

    <!-- HEADER -->
    <header>
        <h2>🚀 Proyecto CI/CD</h2>
        <nav>
            <a onclick="window.scrollTo(0,0)">Inicio</a>
            <a onclick="alert('Traefik + Docker Swarm + GitHub Actions')">Tecnologías</a>
            <a onclick="alert('Desarrollado por grupo 2')">Sobre mí</a>
        </nav>
    </header>

    <!-- HERO -->
    <section class="hero">
        <div>
            <h1>Despliegue Profesional con Traefik</h1>
            <p>Aplicación Flask desplegada automáticamente con CI/CD, Docker Swarm, Traefik y SSL de Let's Encrypt.</p>
            <button onclick="alert('¡Felicidades! El despliegue está funcionando ✨')">Ver más</button>
        </div>
    </section>

    <!-- FEATURES -->
    <section class="features">
        <h2>Características del Proyecto</h2>

        <div class="cards">

            <div class="card">
                <i class="fa-solid fa-network-wired"></i>
                <h3>Traefik Reverse Proxy</h3>
                <p>Gestión automática de enrutamiento, puertos y certificados SSL.</p>
            </div>

            <div class="card">
                <i class="fa-brands fa-docker"></i>
                <h3>Docker Swarm</h3>
                <p>Orquestación de contenedores en un entorno distribuido.</p>
            </div>

            <div class="card">
                <i class="fa-brands fa-github"></i>
                <h3>GitHub Actions</h3>
                <p>Pipeline automatizado para construcción y despliegue continuo.</p>
            </div>

            <div class="card">
                <i class="fa-solid fa-lock"></i>
                <h3>SSL Automático</h3>
                <p>Certificados siempre actualizados con Let's Encrypt.</p>
            </div>

        </div>
    </section>

    <!-- FOOTER -->
    <footer>
        © 2025 — App de ejemplo con Traefik y Flask
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return HTML_PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
