import requests
from colored import Fore

def check_admin_panel(url):
    paths = [
        "/admin",
        "/admin/login",
        "/administrator",
        "/adminpanel",
        "/wp-admin",
        "/wp-login.php",
        "/user/login",
        "/login",
        "/panel",
        "/controlpanel"
    ]

    for path in paths:
        admin_url = url.rstrip("/") + path
        response = requests.head(admin_url)
        if response.status_code == 200:
            print(Fore.RED + "Найдена административная панель:", admin_url)
            return

    print(Fore.RED + "Административная панель не найдена")

def menu():
    while True:
        url = input("Введите URL сайта: ")
        check_admin_panel(url)

        input(Fore.RED + 'Нажмите Enter, чтобы вернуться в меню...')

if __name__ == '__main__':
    menu()
