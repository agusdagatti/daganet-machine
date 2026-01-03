import feedparser
import requests
from bs4 import BeautifulSoup
import random
import time
from datetime import datetime
from config import NEWS_SOURCES, MILITARY_KEYWORDS, USER_AGENTS, REQUEST_DELAY

def filter_by_keywords(text):
    text = text.lower()
    for keyword in MILITARY_KEYWORDS:
        if keyword.lower() in text:
            return True
    return False

def check_date_range(entry_date_struct, date_from, date_to):
    """
    Verifica si una fecha está dentro del rango.
    date_from y date_to deben ser objetos datetime (o None).
    """
    if not entry_date_struct:
        return True # Si no hay fecha, lo incluimos por defecto o lo descartamos. Decisión: incluir.
    
    # Convertir time.struct_time a datetime
    try:
        entry_dt = datetime(*entry_date_struct[:6])
    except:
        return True

    if date_from and entry_dt < date_from:
        return False
    if date_to and entry_dt > date_to:
        return False
    return True

def fetch_rss_news(limit_per_source=5, date_from=None, date_to=None):
    all_news = []
    
    print(f"[*] Escaneando fuentes RSS ({len(NEWS_SOURCES)} fuentes)...")

    for source_name, url in NEWS_SOURCES.items():
        try:
            feed = feedparser.parse(url)
            count = 0
            
            for entry in feed.entries:
                if count >= limit_per_source:
                    break
                
                title = entry.title
                link = entry.link
                summary = getattr(entry, 'summary', '')
                published_struct = getattr(entry, 'published_parsed', None)
                
                # Filtrado por fecha
                if not check_date_range(published_struct, date_from, date_to):
                    continue

                # Filtrado por palabras clave
                if filter_by_keywords(title) or filter_by_keywords(summary):
                    published_str = "Desconocida"
                    if published_struct:
                        published_str = datetime(*published_struct[:6]).strftime("%Y-%m-%d %H:%M:%S")

                    all_news.append({
                        'title': title,
                        'link': link,
                        'description': summary[:200] + "...",
                        'source': source_name,
                        'date': published_str,
                        'type': 'News (RSS)'
                    })
                    count += 1
            
            time.sleep(0.5) # Pequeño delay entre processar feeds localmente no es necesario, pero si requests

        except Exception as e:
            print(f"[-] Error leyendo RSS de {source_name}: {e}")

    return all_news

def direct_scraping(url):
    """
    Para sitios que no tengan RSS (placeholder para expansión futura).
    """
    pass
