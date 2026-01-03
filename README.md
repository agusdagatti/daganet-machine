# DAGANET MACHINE

**Herramienta Educativa Integral de Ciberseguridad para Kali Linux**

DAGANET MACHINE es un framework modular diseñado para centralizar y facilitar el uso de herramientas de auditoría y pruebas de penetración en entornos Kali Linux. Está diseñado con fines **educativos y de formación profesional**.

## 🚀 Características

- **Modularidad**: Arquitectura limpia dividida en módulos (Wi-Fi, Red, OSINT, etc.).
- **Gestión de Dependencias**: Verificación automática de herramientas instaladas.
- **Interfaz Intuitiva**: Menú basado en CLI fácil de navegar.
- **Optimizado para Kali**: Utiliza rutas y herramientas nativas de la distribución.

## 🛠️ Herramientas Integradas

1. **Auditoría Wi-Fi**: Wifite, Aircrack-ng, Kismet
2. **Escaneo y Enumeración**: Nmap, Searchsploit
3. **Ataques de Red**: Bettercap, Arpwatch, Wifiphisher
4. **Ingeniería Social**: Social-Engineer Toolkit (SET)
5. **OSINT**: Sherlock, Recon-ng

## 📋 Requisitos

- **Sistema Operativo**: Kali Linux (Recomendado) o Debian-based con herramientas de seguridad instaladas.
- **Python**: 3.x
- **Permisos**: Privilegios de superusuario (root) son requeridos para la mayoría de ataques de red.

## 📥 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/daganet-machine.git
   cd daganet-machine
   ```

2. Instalar dependencias pre-requisito (si faltan en Kali):
   ```bash
   sudo apt update
   sudo apt install nmap wifite aircrack-ng kismet safe-rm bettercap unrar
   # Algunas herramientas como sherlock pueden requerir instalación pip
   pip3 install -r requirements.txt
   ```

## 💻 Uso

Ejecutar el script principal con permisos de root:

```bash
sudo python3 daganet.py
```

O para verificar dependencias sin entrar al menú:

```bash
sudo python3 daganet.py --check
```

## ⚠️ DISCLAIMER (Descargo de Responsabilidad)

**LEA ATENTAMENTE ANTES DE USAR:**

Esta herramienta ha sido creada exclusivamente con fines **EDUCATIVOS, DE INVESTIGACIÓN Y DE HACKING ÉTICO**.

- El uso de DAGANET MACHINE para atacar objetivos sin el consentimiento previo, mutuo y explícito es **ILEGAL**.
- Es responsabilidad del usuario final obedecer todas las leyes locales, estatales y federales aplicables.
- Los desarrolladores NO asumen responsabilidad alguna y NO son responsables por cualquier mal uso o daño causado por este programa.
- Al utilizar este software, usted se compromete a usarlo únicamente en entornos controlados (laboratorios propios) o en auditorías autorizadas.

---
Hecho con 🐍 y ❤️ para la comunidad de Ciberseguridad.
