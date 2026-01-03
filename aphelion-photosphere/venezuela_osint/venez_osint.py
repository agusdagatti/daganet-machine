import argparse
import sys
import time
from datetime import datetime
from colorama import init, Fore, Style
from modules.web_search import search_duckduckgo
from modules.news_scraper import fetch_rss_news
from modules.social_search import search_social_media
from modules.report_generator import generate_reports

# Inicializar colorama
init(autoreset=True)

BANNER = f"""
{Fore.YELLOW}
 __      __                                 _            
 \ \    / /                                | |           
  \ \  / /__ _ __   ___ ______   ___  ___ _| | __ _      
   \ \/ / _ \ '_ \ / _ \_  / | | | |/ _ \_  / |/ _` |     
    \  /  __/ | | |  __// /| |_| | | (_) |/ /| | (_| |    
     \/ \___|_| |_|\___/___|\__,_|_|\___/___/|_|\__,_|    
                                                          
      {Fore.CYAN}VENEZUELA MILITARY OSINT MONITOR v1.0{Fore.YELLOW}
      {Fore.WHITE}Investigación de Fuentes Abiertas{Fore.YELLOW}
"""

def print_banner():
    print(BANNER)
    print(f"{Fore.GREEN}[+] Herramienta iniciada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{Fore.RED}[!] AVISO: Uso exclusivo para fines de investigación académica/periodística.")
    print("-" * 60)

def parse_date(date_str):
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print(f"{Fore.RED}[!] Formato de fecha inválido: {date_str}. Use YYYY-MM-DD")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Herramienta OSINT para Venezuela Monitor")
    parser.add_argument("-q", "--query", type=str, required=True, help="Término de búsqueda (ej: 'operaciones militares')")
    parser.add_argument("-m", "--mode", choices=['news', 'social', 'web', 'all'], default='all', help="Modo de búsqueda")
    parser.add_argument("-l", "--limit", type=int, default=10, help="Límite de resultados por fuente")
    parser.add_argument("--date-from", type=str, help="Fecha inicio (YYYY-MM-DD)")
    parser.add_argument("--date-to", type=str, help="Fecha fin (YYYY-MM-DD)")
    parser.add_argument("-e", "--export", choices=['json', 'csv', 'html', 'all'], default='html', help="Formato de reporte")
    
    args = parser.parse_args()
    
    print_banner()
    
    start_date = parse_date(args.date_from)
    end_date = parse_date(args.date_to)
    
    all_results = []
    
    print(f"{Fore.CYAN}[*] Iniciando búsqueda para: '{args.query}'")
    
    # 1. Búsqueda de Noticias (RSS)
    if args.mode in ['news', 'all']:
        print(f"\n{Fore.YELLOW}[1] Buscando en Fuentes de Noticias (RSS)...")
        # RSS filtra por keywords internas, pero podemos filtrar post-fetch si queremos ser estrictos con el query
        news_results = fetch_rss_news(limit_per_source=args.limit, date_from=start_date, date_to=end_date)
        # Filtrado adicional simple por query si no es vacía
        filtered_news = [n for n in news_results if args.query.lower() in n['title'].lower() or args.query.lower() in n['description'].lower()]
        print(f"{Fore.GREEN}    -> {len(filtered_news)} noticias encontradas.")
        all_results.extend(filtered_news)

    # 2. Búsqueda Web (DuckDuckGo HTML)
    if args.mode in ['web', 'all']:
        print(f"\n{Fore.YELLOW}[2] Realizando búsqueda Web (DuckDuckGo)...")
        web_results = search_duckduckgo(f"Venezuela {args.query}", limit=args.limit)
        print(f"{Fore.GREEN}    -> {len(web_results)} resultados web encontrados.")
        all_results.extend(web_results)

    # 3. Búsqueda Social (Nitter + Dorks)
    if args.mode in ['social', 'all']:
        print(f"\n{Fore.YELLOW}[3] Investigando Redes Sociales...")
        social_results = search_social_media(args.query, limit=args.limit)
        print(f"{Fore.GREEN}    -> {len(social_results)} resultados sociales encontrados.")
        all_results.extend(social_results)

    # Generación de Reportes
    print("\n" + "-" * 60)
    if not all_results:
        print(f"{Fore.RED}[!] No se encontraron resultados. Intente con términos más generales.")
    else:
        print(f"{Fore.CYAN}[*] Procesando {len(all_results)} resultados totales...")
        formats = ['json', 'csv', 'html'] if args.export == 'all' else [args.export]
        generate_reports(all_results, args.query, formats)
        
    print(f"\n{Fore.GREEN}[OK] Proceso completado. Happy Hunting!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Operación cancelada por el usuario.")
        sys.exit()
