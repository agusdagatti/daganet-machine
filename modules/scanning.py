import subprocess
from utils.helpers import check_dependency, Colors, clear_screen, print_banner

def run_nmap():
    if check_dependency("nmap"):
        target = input(f"{Colors.CYAN}Ingrese la IP o dominio objetivo: {Colors.ENDC}")
        if target:
            print(f"\n{Colors.HEADER}TIPOS DE ESCANEO{Colors.ENDC}")
            print("1. Rápido (-F)")
            print("2. Detección de Versiones y Servicios (-sV)")
            print("3. Agresivo/Completo (-A)")
            scan_type = input(f"{Colors.GREEN}Seleccione opción: {Colors.ENDC}")

            cmd = ["nmap", target]
            if scan_type == '1':
                cmd.insert(1, "-F")
            elif scan_type == '2':
                cmd.insert(1, "-sV")
            elif scan_type == '3':
                cmd.insert(1, "-A")
            
            print(f"{Colors.BLUE}[*] Ejecutando Nmap en {target}...{Colors.ENDC}")
            subprocess.call(cmd)
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def run_searchsploit():
    if check_dependency("searchsploit"):
        query = input(f"{Colors.CYAN}Término de búsqueda (ej. apache 2.4): {Colors.ENDC}")
        if query:
            print(f"{Colors.BLUE}[*] Buscando exploits para: {query}...{Colors.ENDC}")
            subprocess.call(["searchsploit", query])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def scanning_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{Colors.HEADER}MÓDULO ESCANEO Y ENUMERACIÓN{Colors.ENDC}")
        print("1. Escaneo de Puertos (Nmap)")
        print("2. Búsqueda de Exploits (Searchsploit)")
        print("0. Volver al menú principal")
        
        choice = input(f"\n{Colors.GREEN}Seleccione una herramienta: {Colors.ENDC}")

        if choice == '1':
            run_nmap()
        elif choice == '2':
            run_searchsploit()
        elif choice == '0':
            break
        else:
            input(f"\n{Colors.FAIL}Opción inválida.{Colors.ENDC}")
