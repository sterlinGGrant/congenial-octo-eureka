import whois

# ANSI escape код для красного цвета
RED = "\033[91m"
RESET = "\033[0m"


def get_domain_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as e:
        return f"{RED}Ошибка при получении информации о домене: {str(e)}{RESET}"


if __name__ == "__main__":
    domain_name = input(f"{RED}Введите ссылку на веб-сайт/домен: {RESET}")
    domain_info = get_domain_info(domain_name)

    print(f"{RED}\nИнформация о домене:{RESET}")
    print(domain_info)

    input(f"{RED}\nНажмите Enter для завершения...{RESET}")