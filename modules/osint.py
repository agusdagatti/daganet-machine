import subprocess
from utils.helpers import check_dependency, Colors, clear_screen, print_banner

def run_sherlock():
    # Sherlock a veces se instala como 'sherlock' o requiere correr 'python3 sherlock.py' si se clonó.
    # Asumiremos instalación en path o alias.
    if check_dependency("sherlock"):
        username = input(f"{Colors.CYAN}Ingrese nombre de usuario a investigar: {Colors.ENDC}")
        if username:
            print(f"{Colors.BLUE}[*] Buscando '{username}' en redes sociales...{Colors.ENDC}")
            subprocess.call(["sherlock", username])
    else:
        # Fallback simple si no está en path directo
        print(f"{Colors.WARNING}Sherlock no encontrado en el PATH. Asegúrese de haberlo instalado (ej: pip install sherlock-project).{Colors.ENDC}")
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def run_recon_ng():
    if check_dependency("recon-ng"):
        print(f"{Colors.BLUE}[*] Iniciando Recon-ng...{Colors.ENDC}")
        subprocess.call(["recon-ng"])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def osint_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{Colors.HEADER}MÓDULO OSINT Y RECONOCIMIENTO{Colors.ENDC}")
        print("1. Sherlock (Búsqueda de usuarios)")
        print("2. Recon-ng (Framework de reconocimiento)")
        print("0. Volver al menú principal")
        
        choice = input(f"\n{Colors.GREEN}Seleccione una herramienta: {Colors.ENDC}")

        if choice == '1':
            run_sherlock()
        elif choice == '2':
            run_recon_ng()
        elif choice == '0':
            break
        else:
            input(f"\n{Colors.FAIL}Opción inválida.{Colors.ENDC}")
