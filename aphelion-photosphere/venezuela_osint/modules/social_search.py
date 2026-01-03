from .web_search import search_duckduckgo
import requests
from bs4 import BeautifulSoup
import random
import time
from config import USER_AGENTS, REQUEST_DELAY

def search_nitter(query, limit=5):
    """
    Busca en una instancia de Nitter (Twitter frontend open source).
    """
    # Instancias de Nitter públicas (pueden cambiar)
    # nitter.net a veces tiene rate limit, probamos otra si falla
    nitter_instance = "https://nitter.net" 
    url = f"{nitter_instance}/search"
    params = {'f': 'tweets', 'q': query}
    headers = {'User-Agent': random.choice(USER_AGENTS)}

    try:
        time.sleep(REQUEST_DELAY)
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        tweets = soup.find_all('div', class_='timeline-item')
        for tweet in tweets:
            if len(results) >= limit:
                break
            
            # Extraer contenido
            content_div = tweet.find('div', class_='tweet-content')
            if not content_div:
                continue
            text = content_div.get_text(strip=True)
            
            # Extraer autor
            user_a = tweet.find('a', class_='username')
            user = user_a.get_text(strip=True) if user_a else "Unknown"
            
            # Extraer fecha
            date_span = tweet.find('span', class_='tweet-date')
            date_a = date_span.find('a') if date_span else None
            date = date_a['title'] if date_a else "Unknown Date"
            link = nitter_instance + date_a['href'] if date_a else ""

            results.append({
                'title': f"Tweet by {user}",
                'link': link,
                'description': text,
                'source': 'Twitter (Nitter)',
                'date': date,
                'type': 'Social Media'
            })
            
        return results

    except Exception as e:
        print(f"[-] Nitter Search Error: {e}")
        return []

def search_social_media(query, limit=10):
    """
    Busca en redes sociales usando Nitter para Twitter y Dorks para otros.
    """
    results = []
    
    # 1. Twitter visual (Nitter)
    print("    [>] Buscando en Twitter (vía Nitter)...")
    results.extend(search_nitter(query, limit=5))
    
    # 2. Telegram Dorks (vía DuckDuckGo)
    print("    [>] Buscando canales de Telegram...")
    telegram_query = f'site:t.me "Venezuela" {query}'
    tg_results = search_duckduckgo(telegram_query, limit=5)
    for r in tg_results:
        r['source'] = 'Telegram (Web)'
        r['type'] = 'Social Media'
    results.extend(tg_results)

    # 3. Facebook Public Dorks
    print("    [>] Buscando en Facebook (Público)...")
    fb_query = f'site:facebook.com "Venezuela" {query}'
    fb_results = search_duckduckgo(fb_query, limit=5)
    for r in fb_results:
        r['source'] = 'Facebook (Public)'
        r['type'] = 'Social Media'
    results.extend(fb_results)

    return results
