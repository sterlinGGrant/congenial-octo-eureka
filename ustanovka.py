import sys
import os 
import subprocess
import time

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"

required_modules = [
    "pystyle",
    "phonenumbers",
    "colorama",
    "requests",
    "faker",
    "qrcode",
    "bs4",
    "whois",
    "hashlib",
    "csv",
    "urllib.parse",
    "requests",
    "threading",
    "uuid",
    "socket",
    "smtplib",
    "xlrd",
    "getpass",
    "fake_useragent",
    "termcolor",
    "logging",
    "aiogram",
    "re",
    "telebot",
    "sys",
    "subprocess",
    "telethon",
    "pyfiglet",
    "webbrowser",
    "marshal",
    "base64"
]

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(
        GREEN_TEXT + "Здравствуйте это установщик модулей софта FAME пожалуйста подождите..." + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module} уже уставновлен" + RESET)
        except ImportError:
            print(f"Устонофка {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"установили модуль {module}" + RESET)

if __name__ == "__main__":
    check_and_install_modules()

    print_with_delay(GREEN_TEXT + "STARTING MAIN.PY IN FOLDER - (FAMETOOL)..." + RESET)
    os.system('python main.py')