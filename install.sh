#!/bin/bash

# Daganet Machine - Dependency Installer
# Run as root: sudo ./install.sh

if [ "$EUID" -ne 0 ]; then 
  echo "Please run as root (sudo ./install.sh)"
  exit
fi

echo "[*] Updating repositories..."
apt update

echo "[*] Installing core tools..."
apt install -y nmap wifite aircrack-ng kismet safe-rm bettercap arpwatch wifiphisher exploitdb

echo "[*] Installing OSINT tools..."
apt install -y recon-ng sherlock

echo "[*] Installing Social Engineer Toolkit (SET)..."
# Try apt first, fall back to git clone
if apt-cache show setoolkit >/dev/null 2>&1; then
    apt install -y setoolkit
else
    echo "[!] 'setoolkit' not in apt repositories. Installing from GitHub..."
    # Install git and python3-venv if missing
    apt install -y git python3-pip python3-venv
    
    # Clone to /opt/setoolkit
    if [ ! -d "/opt/setoolkit" ]; then
        git clone https://github.com/trustedsec/social-engineer-toolkit/ /opt/setoolkit
        cd /opt/setoolkit
        # Fix: pycrypto is dead and breaks on Python 3.11+. Replace with pycryptodome.
        sed -i 's/pycrypto/pycryptodome/' requirements.txt
        # Fix: Prevent pip from trying to downgrade system packages (causes errors)
        sed -i '/pyopenssl/Id' requirements.txt
        sed -i '/cryptography/Id' requirements.txt
        
        pip3 install -r requirements.txt --break-system-packages
        python3 setup.py install
        echo "[*] SET installed to /opt/setoolkit"
    else
        echo "[*] /opt/setoolkit already exists. Skipping clone."
    fi
fi

echo "[*] Installation complete!"
echo "[*] Run Daganet: sudo python3 daganet.py"
