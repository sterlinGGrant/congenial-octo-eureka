import requests
from bs4 import BeautifulSoup

def check_nickname(nickname):
    links = {
        'Instagram': 'https://www.instagram.com/',
        'GitHub': 'https://github.com/',
        'VK': 'https://vk.com/',
        'Tumblr': 'https://www.tumblr.com/blog/view/',
        'Twitter': 'https://twitter.com/',
        'Telegram': 'https://t.me/',
        'Viber': 'viber://chat?number=',
        'WhatsApp': 'https://wa.me/',
        'Одноклассники': 'https://ok.ru/profile/'
    }
    found_links = []
    for platform, base_url in links.items():
        url = base_url + nickname
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            if nickname in str(soup):
                found_links.append(f"{platform}: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при проверке {platform}: {e}")
    return found_links

while True:
    nickname = input("Введите никнейм: ")
    found_links = check_nickname(nickname)
    if found_links:
        print("Найдено на следующих платформах:")
        for link in found_links:
            print(link)
    else:
        print("Никнейм не найден ни на одной из платформ.")
    if input("Нажмите Enter... ") == "":
        break
