import json
import csv
import os
from datetime import datetime
from jinja2 import Template

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Inteligencia - Venezuela OSINT</title>
    <style>
        :root {
            --bg-color: #0d1b2a;
            --header-bg: #1b263b;
            --card-bg: #ffffff;
            --text-primary: #333333;
            --text-secondary: #666666;
            --accent: #415a77;
            --highlight: #e0e1dd;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            background: linear-gradient(135deg, #0d1b2a 0%, #1b263b 100%);
            color: var(--highlight);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: rgba(27, 38, 59, 0.8);
            border-radius: 10px;
            backdrop-filter: blur(10px);
            border: 1px solid var(--accent);
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }

        h1 {
            color: #fff;
            margin: 0;
            font-size: 2.5em;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .meta {
            margin-top: 10px;
            color: #a0a0a0;
            font-size: 0.9em;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }

        .card {
            background: var(--card-bg);
            color: var(--text-primary);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        }

        .card-header {
            background: var(--accent);
            color: white;
            padding: 10px 15px;
            font-size: 0.85em;
            text-transform: uppercase;
            font-weight: bold;
            display: flex;
            justify-content: space-between;
        }

        .card-body {
            padding: 20px;
            flex-grow: 1;
        }

        .card-title {
            font-size: 1.2em;
            margin: 0 0 10px 0;
            color: #000;
            font-weight: 700;
        }

        .card-text {
            font-size: 0.95em;
            color: var(--text-secondary);
            line-height: 1.5;
        }

        .card-footer {
            padding: 15px;
            background: #f8f9fa;
            border-top: 1px solid #eee;
            text-align: right;
        }

        .btn {
            display: inline-block;
            text-decoration: none;
            background: var(--header-bg);
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 0.9em;
            transition: background 0.2s;
        }

        .btn:hover {
            background: var(--accent);
        }

        .disclaimer {
            margin-top: 50px;
            text-align: center;
            font-size: 0.8em;
            color: #aaa;
            padding: 20px;
            border-top: 1px solid var(--accent);
        }
    </style>
</head>
<body>
    <header>
        <h1>VENEZUELA OSINT</h1>
        <div class="meta">
            Reporte generado el: {{ report_date }}<br>
            Query: "{{ query }}" | Resultados: {{ count }}
        </div>
    </header>

    <div class="container">
        {% for item in data %}
        <div class="card">
            <div class="card-header">
                <span>{{ item.source }}</span>
                <span>{{ item.date }}</span>
            </div>
            <div class="card-body">
                <h3 class="card-title">{{ item.title }}</h3>
                <p class="card-text">{{ item.description }}</p>
            </div>
            <div class="card-footer">
                <a href="{{ item.link }}" target="_blank" class="btn">Ver Fuente</a>
            </div>
        </div>
        {% endfor %}
    </div>

    <div class="disclaimer">
        <p><strong>AVISO LEGAL:</strong> Esta herramienta es para fines de investigación académica y periodística exclusivamente (OSINT).</p>
        <p>Toda la información ha sido recopilada de fuentes públicas y abiertas. El usuario es responsable de su uso.</p>
    </div>
</body>
</html>
"""

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"[+] Reporte JSON guardado en: {filename}")

def save_csv(data, filename):
    if not data:
        return
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"[+] Reporte CSV guardado en: {filename}")

def save_html(data, filename, query):
    template = Template(HTML_TEMPLATE)
    html_content = template.render(
        data=data,
        query=query,
        report_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        count=len(data)
    )
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[+] Reporte HTML Premium guardado en: {filename}")

def generate_reports(data, query, formats=['html']):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"reporte_venezuela_{timestamp}"
    
    # Crear carpeta de reportes si no existe
    if not os.path.exists("reportes"):
        os.makedirs("reportes")
        
    base_path = os.path.join("reportes", base_name)

    if 'json' in formats or 'all' in formats:
        save_json(data, f"{base_path}.json")
    
    if 'csv' in formats or 'all' in formats:
        save_csv(data, f"{base_path}.csv")
        
    if 'html' in formats or 'all' in formats:
        save_html(data, f"{base_path}.html", query)
