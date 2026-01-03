import os
import shutil
import sys
import time

# Colores para la terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_root():
    """Verifica si el script se está ejecutando como root."""
    if os.geteuid() != 0:
        print(f"{Colors.FAIL}[!] Este script debe ejecutarse como root.{Colors.ENDC}")
        print(f"{Colors.WARNING}Uso: sudo python3 daganet.py{Colors.ENDC}")
        sys.exit(1)

def check_dependency(tool_name):
    """Verifica si una herramienta está instalada en el sistema."""
    path = shutil.which(tool_name)
    if path:
        return True
    else:
        print(f"{Colors.FAIL}[!] La herramienta '{tool_name}' no se encuentra instalada.{Colors.ENDC}")
        print(f"{Colors.WARNING}[*] Instálala usando: sudo apt install {tool_name}{Colors.ENDC}")
        return False

def clear_screen():
    os.system('clear')

def print_banner():
    banner = f"""{Colors.CYAN}
    ██████╗  █████╗  ██████╗  █████╗ ███╗   ██╗███████╗████████╗
    ██╔══██╗██╔══██╗██╔════╝ ██╔══██╗████╗  ██║██╔════╝╚══██╔══╝
    ██║  ██║███████║██║  ███╗███████║██╔██╗ ██║█████╗     ██║   
    ██║  ██║██╔══██║██║   ██║██╔══██║██║╚██╗██║██╔══╝     ██║   
    ██████╔╝██║  ██║╚██████╔╝██║  ██║██║ ╚████║███████╗   ██║   
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   
    {Colors.ENDC}{Colors.BOLD}       MACHINE - Herramienta Educativa de Ciberseguridad{Colors.ENDC}
    """
    print(banner)
    print(f"{Colors.BLUE}[*] Autor: DAGANET User{Colors.ENDC}")
    print(f"{Colors.WARNING}[!] USO EXCLUSIVAMENTE EDUCATIVO Y ÉTICO{Colors.ENDC}")
    print("-" * 60)
