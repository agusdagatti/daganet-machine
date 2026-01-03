import subprocess
from utils.helpers import check_dependency, Colors, clear_screen, print_banner

def run_wifite():
    if check_dependency("wifite"):
        print(f"{Colors.BLUE}[*] Iniciando Wifite...{Colors.ENDC}")
        subprocess.call(["wifite"])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def run_aircrack():
    if check_dependency("aircrack-ng"):
        print(f"{Colors.BLUE}[*] Aircrack-ng - Cracking de Handshake{Colors.ENDC}")
        cap_file = input(f"{Colors.CYAN}Ingrese la ruta del archivo .cap: {Colors.ENDC}")
        wordlist = input(f"{Colors.CYAN}Ingrese la ruta del diccionario (Enter para default /usr/share/wordlists/rockyou.txt): {Colors.ENDC}")
        
        if not wordlist:
            wordlist = "/usr/share/wordlists/rockyou.txt"
            
        if cap_file:
             print(f"{Colors.BLUE}[*] Iniciando ataque de diccionario con Aircrack-ng...{Colors.ENDC}")
             # sudo aircrack-ng -w [wordlist] [capfile]
             subprocess.call(["aircrack-ng", "-w", wordlist, cap_file])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def run_kismet():
    if check_dependency("kismet"):
        print(f"{Colors.BLUE}[*] Iniciando Kismet...{Colors.ENDC}")
        subprocess.call(["kismet"])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def wifi_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{Colors.HEADER}MÓDULO AUDITORÍA WI-FI{Colors.ENDC}")
        print("1. Ejecutar Wifite (Automatizado)")
        print("2. Aircrack-ng (Suite Manual)")
        print("3. Ejecutar Kismet (Sniffer)")
        print("0. Volver al menú principal")
        
        choice = input(f"\n{Colors.GREEN}Seleccione una herramienta: {Colors.ENDC}")

        if choice == '1':
            run_wifite()
        elif choice == '2':
            run_aircrack()
        elif choice == '3':
            run_kismet()
        elif choice == '0':
            break
        else:
            input(f"\n{Colors.FAIL}Opción inválida.{Colors.ENDC}")
