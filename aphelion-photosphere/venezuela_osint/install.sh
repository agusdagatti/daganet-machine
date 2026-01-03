#!/bin/bash

# Colores
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[*] Inicializando configuración de Venezuela OSINT Tool...${NC}"

# Verificar si pip está instalado
if ! command -v pip3 &> /dev/null
then
    echo "pip3 no encontrado. Intentando instalar..."
    sudo apt-get update
    sudo apt-get install python3-pip -y
fi

echo -e "${GREEN}[*] Instalando librerías de Python...${NC}"
pip3 install -r requirements.txt

echo -e "${GREEN}[*] Asignando permisos de ejecución...${NC}"
chmod +x venez_osint.py

echo -e "${GREEN}[+] Instalación completada exitosamente.${NC}"
echo -e "Ejemplo de uso: python3 venez_osint.py -q \"FANB\" -m all"
