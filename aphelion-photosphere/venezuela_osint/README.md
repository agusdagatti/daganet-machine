# Venezuela OSINT Tool 🇻🇪

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Linux-black)
![License](https://img.shields.io/badge/License-MIT-green)

Herramienta de Inteligencia de Fuentes Abiertas (OSINT) especializada en la recolección y análisis de información pública sobre operaciones militares, seguridad y defensa en Venezuela. Diseñada para investigadores, periodistas y analistas.

## 🚀 Características

- **Búsqueda Multi-vector**:
  - 📰 **Noticias**: Rastreo RSS de medios principales (El Nacional, TalCual, etc.)
  - 🌐 **Web**: Búsqueda anónima vía DuckDuckGo (HTML scraping).
  - 🐦 **Social**: Monitorización de Twitter/X (vía Nitter) y Dorks para Telegram/Facebook.
- **Reportes Premium**: Generación automática de reportes HTML con diseño moderno (Dark Blue), mapas de calor de datos y exportación a JSON/CSV.
- **Seguridad Operacional**: Rotación de User-Agents y retardos aleatorios para evitar bloqueos.
- **Filtros Avanzados**: Búsqueda por rango de fechas y palabras clave militares predefinidas.

## 🛠 Instalación

Esta herramienta está optimizada para **Kali Linux** y entornos Debian-based.

```bash
# 1. Clonar el repositorio
git clone https://github.com/usuario/venezuela-osint.git

# 2. Entrar al directorio
cd venezuela-osint

# 3. Ejecutar script de instalación
chmod +x install.sh
./install.sh
```

## 💻 Uso

La interfaz es vía línea de comandos (CLI) para máxima eficiencia.

### Comandos Básicos

```bash
# Búsqueda rápida de noticias
python3 venez_osint.py -q "operaciones militares" -m news

# Búsqueda completa (Web + Social + News) con reporte HTML
python3 venez_osint.py -q "ejercicios FANB" -m all -e html

# Búsqueda filtrando por fechas
python3 venez_osint.py -q "frontera apure" --date-from 2023-01-01 --date-to 2023-12-31
```

### Argumentos

| Argumento | Descripción |
|-----------|-------------|
| `-q`, `--query` | Término de búsqueda (Requerido). |
| `-m`, `--mode` | Modo de búsqueda: `news`, `web`, `social`, `all`. Default: `all`. |
| `-e`, `--export` | Formato de reporte: `html`, `json`, `csv`, `all`. Default: `html`. |
| `--date-from` | Fecha de inicio (YYYY-MM-DD). |
| `--date-to` | Fecha de fin (YYYY-MM-DD). |
| `-l`, `--limit` | Límite de resultados por fuente. |

## ⚖️ Aviso Legal y Ético (DISCLAIMER)

**POR FAVOR LEA ATENTAMENTE:**

Esta herramienta ha sido desarrollada con fines **exclusivamente académicos, periodísticos y de investigación legítima**.

1. **Fuentes Públicas**: La herramienta solo accede a información disponible públicamente en Internet (Open Source). No realiza intrusiones, hackeos ni accede a sistemas protegidos.
2. **Responsabilidad**: El usuario final es el único responsable del uso que se le dé a la información recopilada. Los desarrolladores no se hacen responsables por el mal uso de este software.
3. **Privacidad**: Respete las leyes de privacidad y protección de datos locales e internacionales al procesar información personal.

---
*Desarrollado con fines educativos.*
