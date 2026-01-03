# config.py
# Configuración para Venezuela OSINT Tool

# Lista de User-Agents para rotación y respeto a los servidores
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0"
]

# Fuentes de noticias venezolanas (RSS y URLs directas)
NEWS_SOURCES = {
    "El Nacional": "https://www.elnacional.com/feed/",
    "El Universal": "https://www.eluniversal.com/rss",
    "Efecto Cocuyo": "https://efectococuyo.com/feed/",
    "TalCual": "https://talcualdigital.com/feed/",
    "La Patilla": "https://www.lapatilla.com/feed/"
}

# Palabras clave para filtrado y categorización militar
MILITARY_KEYWORDS = [
    "FANB",
    "Fuerza Armada Nacional Bolivariana",
    "operaciones militares",
    "CEOFANB",
    "ejercicios militares",
    "frontera",
    "defensa",
    "Sukhoi",
    "F-16",
    "tanques",
    "blindados",
    "milicia",
    "GNB",
    "Ejército",
    "Aviación",
    "Armada",
    "SEBIN",
    "DGCIM",
    "apure",
    "táchira",
    "zulia",
    "bolívar"
]

# Configuración de retardos (en segundos)
REQUEST_DELAY = 1.5
