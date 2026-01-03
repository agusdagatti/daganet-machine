import subprocess
from utils.helpers import check_dependency, Colors, clear_screen, print_banner

def run_set():
    if check_dependency("setoolkit"):
        print(f"{Colors.BLUE}[*] Iniciando Social-Engineer Toolkit (SET)...{Colors.ENDC}")
        subprocess.call(["setoolkit"])
    elif check_dependency("se-toolkit"): # Nombre alternativo a veces
         subprocess.call(["se-toolkit"])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def social_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{Colors.HEADER}MÓDULO INGENIERÍA SOCIAL{Colors.ENDC}")
        print("1. Social-Engineer Toolkit (SET)")
        print("0. Volver al menú principal")
        
        choice = input(f"\n{Colors.GREEN}Seleccione una herramienta: {Colors.ENDC}")

        if choice == '1':
            run_set()
        elif choice == '0':
            break
        else:
            input(f"\n{Colors.FAIL}Opción inválida.{Colors.ENDC}")
