import requests
import re
import telebot
import time
from colorama import Fore, Style
import colorama

def main():
    print(Fore.RED + "Предупреждение! Если у вас мало оперативной памяти, не указывайте большой диапазон" + Style.RESET_ALL)
    bot_token = input(Fore.YELLOW + "Ваш токен @botFather -> " + Style.RESET_ALL)
    start_number = input(Fore.YELLOW + "Введите начальный номер диапазона (Пример: 79000000000) -> " + Style.RESET_ALL)
    end_number = input(Fore.YELLOW + "Введите конечный номер диапазона (Пример: 79999999999) -> " + Style.RESET_ALL)

    if not start_number.isdigit() or not end_number.isdigit():
        print(Fore.RED + "Номера должны быть числовыми значениями." + Style.RESET_ALL)
        return

    start_number = int(start_number)
    end_number = int(end_number)

    if start_number >= end_number:
        print(Fore.RED + "Начальный номер должен быть меньше конечного номера." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "Ваш бот вступил в работу, чтобы его активировать, перейдите в бот, который вы создали." + Style.RESET_ALL)
    time.sleep(2)

    bot = telebot.TeleBot(bot_token)

    @bot.message_handler(commands=['start'])
    def start_handler(message):
        args = message.text.split()
        if len(args) < 3:
            bot.send_message(message.chat.id, 'Неверный формат ввода. Введите диапазон в формате: /start start_number end_number')
            return

        try:
            user_start_number = int(args[1])
            user_end_number = int(args[2])
        except ValueError:
            bot.send_message(message.chat.id, 'Диапазон должен содержать только цифры.')
            return

        if user_start_number >= user_end_number:
            bot.send_message(message.chat.id, 'Введенный диапазон некорректен. Введите диапазон в формате: /start start_number end_number')
            return

        bot.send_message(message.chat.id, 'Начался перебор номеров...')
        usernames = set()
        for number in range(user_start_number, user_end_number + 1):
            url = f'https://t.me/{number}'
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    pattern_username = r'<a href="/(\w+)">'
                    pattern_id = r'<a href="/im\?p=(.*?)">'
                    match_username = re.search(pattern_username, response.text)
                    match_id = re.search(pattern_id, response.text)
                    if match_username and match_id:
                        usernames.add(match_username.group(1))
                        bot.send_message(message.chat.id, f'Номер телефона: {number}\nТег: {match_username.group(1)}\nID: {match_id.group(1)}')
            except requests.exceptions.RequestException as e:
                bot.send_message(message.chat.id, f'Ошибка при отправке запроса: {e}')
        
        bot.send_message(message.chat.id, 'Перебор номеров завершен.')

    bot.polling()

if __name__ == '__main__':
    main()
