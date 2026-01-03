import subprocess
from utils.helpers import check_dependency, Colors, clear_screen, print_banner

def run_bettercap():
    if check_dependency("bettercap"):
        print(f"{Colors.BLUE}[*] Iniciando Bettercap...{Colors.ENDC}")
        # Se lanza sin argumentos para modo interactivo
        subprocess.call(["bettercap"])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def run_arpwatch():
    if check_dependency("arpwatch"):
        interface = input(f"{Colors.CYAN}Ingrese interfaz (ej. eth0): {Colors.ENDC}")
        if interface:
            print(f"{Colors.BLUE}[*] Iniciando Arpwatch en {interface}...{Colors.ENDC}")
            # Arpwatch suele correr como demonio, aquí se intenta correr en foreground si posible o iniciar servicio
            print(f"{Colors.WARNING}Nota: Arpwatch generalmente corre como servicio.{Colors.ENDC}")
            subprocess.call(["sudo", "service", "arpwatch", "start"])
            print("Servicio iniciado (si está instalado y configurado).")
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def run_wifiphisher():
    if check_dependency("wifiphisher"):
        print(f"{Colors.BLUE}[*] Iniciando Wifiphisher...{Colors.ENDC}")
        subprocess.call(["wifiphisher"])
    input(f"\n{Colors.WARNING}Presione Enter para volver al menú.{Colors.ENDC}")

def network_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{Colors.HEADER}MÓDULO ATAQUES DE RED Y MITM{Colors.ENDC}")
        print("1. Bettercap (MITM y Red)")
        print("2. Arpwatch (Monitorización ARP)")
        print("3. Wifiphisher (Phishing Wi-Fi)")
        print("0. Volver al menú principal")
        
        choice = input(f"\n{Colors.GREEN}Seleccione una herramienta: {Colors.ENDC}")

        if choice == '1':
            run_bettercap()
        elif choice == '2':
            run_arpwatch()
        elif choice == '3':
            run_wifiphisher()
        elif choice == '0':
            break
        else:
            input(f"\n{Colors.FAIL}Opción inválida.{Colors.ENDC}")
