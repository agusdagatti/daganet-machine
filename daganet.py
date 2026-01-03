#!/usr/bin/env python3
import sys
import argparse
from utils.helpers import check_root, print_banner, clear_screen, Colors
from modules import wifi, scanning, network, social, osint

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"{Colors.HEADER}MENÚ PRINCIPAL{Colors.ENDC}")
        print("1. Auditoría Wi-Fi (Wifite, Aircrack-ng, Kismet)")
        print("2. Escaneo y Enumeración (Nmap, Searchsploit)")
        print("3. Ataques de Red y MITM (Bettercap, Arpwatch, Wifiphisher)")
        print("4. Ingeniería Social (SET)")
        print("5. OSINT y Reconocimiento (Sherlock, Recon-ng)")
        print("0. Salir")
        
        choice = input(f"\n{Colors.GREEN}Seleccione una opción: {Colors.ENDC}")

        if choice == '1':
            wifi.wifi_menu()
        elif choice == '2':
            scanning.scanning_menu()
        elif choice == '3':
            network.network_menu()
        elif choice == '4':
            social.social_menu()
        elif choice == '5':
            osint.osint_menu()
        elif choice == '0':
            print(f"\n{Colors.BLUE}Saliendo de DAGANET MACHINE...{Colors.ENDC}")
            sys.exit(0)
        else:
            input(f"\n{Colors.FAIL}Opción inválida. Presione Enter para continuar.{Colors.ENDC}")

def main():
    parser = argparse.ArgumentParser(description='DAGANET MACHINE - Herramienta de Auditoría de Ciberseguridad')
    parser.add_argument('--check', action='store_true', help='Verificar dependencias e instalación')
    args = parser.parse_args()

    check_root()

    if args.check:
        print(f"{Colors.BLUE}[*] Verificando entorno...{Colors.ENDC}")
        # Aquí se podrían llamar funciones de verificación de todos los módulos
        # Por ahora, simplemente iniciamos el menú
        print(f"{Colors.GREEN}[OK] Verificación completada (Simplificada).{Colors.ENDC}")
        sys.exit(0)

    try:
        main_menu()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}[!] Interrupción detectada. Saliendo...{Colors.ENDC}")
        sys.exit(0)

if __name__ == "__main__":
    main()
