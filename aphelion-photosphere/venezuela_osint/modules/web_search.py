import requests
from bs4 import BeautifulSoup
import random
import time
from config import USER_AGENTS, REQUEST_DELAY

def search_duckduckgo(query, limit=10, date_filter=None):
    """
    Realiza una búsqueda en DuckDuckGo (versión HTML) para evitar bloqueos de API.
    """
    url = "https://html.duckduckgo.com/html/"
    headers = {'User-Agent': random.choice(USER_AGENTS)}
    data = {'q': query}
    
    # Si hubiera filtro de fechas, DDG es complicado vía HTML simple, 
    # pero podemos agregar el año al query si es necesario.
    # Por ahora, búsqueda estándar.

    try:
        time.sleep(REQUEST_DELAY)
        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        results = []

        for result in soup.find_all('div', class_='result'):
            if len(results) >= limit:
                break
            
            title_tag = result.find('a', class_='result__a')
            if not title_tag:
                continue
                
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            snippet_tag = result.find('a', class_='result__snippet')
            snippet = snippet_tag.get_text(strip=True) if snippet_tag else "No description available"

            results.append({
                'title': title,
                'link': link,
                'description': snippet,
                'source': 'DuckDuckGo',
                'date': 'N/A' # DDG HTML no siempre da fecha clara
            })

        return results

    except Exception as e:
        print(f"[-] Error en DuckDuckGo Search: {e}")
        return []

def search_google_dork(query, limit=10):
    """
    Opcional: Búsqueda limitada en Google si es necesario, 
    pero DDG es preferido para evitar captchas agresivos.
    Aquí se deja el placeholder estructural.
    """
    pass
