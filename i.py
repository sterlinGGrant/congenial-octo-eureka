import os
from colorama import Fore, Style
from pystyle import Colorate, Colors
import colorama
from pystyle import *

def xyu():
    xyec = """ПЕРЕД ЗАПУСКОМ DDOSBOTA ЗАЙДИТЕ В ФАЙЛ ddosbot.py И ПОМЕНЯЙТЕ ТАМ СТРОЧКУ
"сюда токен" НА СВОЙ ТОКЕН ДДОС БОТА В ТЕЛЕГРАММ(ТОКЕН ПОЛУЧИТЬ В @BotFather)

ПЕРЕД ЗАПУСКОМ CATCHER CHECK ЗАЙДИТЕ В ФАЙЛ config.ini И ВСТАВЬТЕ ТУДА СВОЙ  API ID И API HASH И АЙДИ ЧАТА В СООТВЕСТВУЮЩИЕ СТРОЧКИ

ПЕРЕД ЗАПУСКОМ CATCHER PRIVATES ЗАЙДИТЕ В ФАЙЛ config (2).py И ЗАМЕНИТЕ ТАМ API HASH И API ID В СООТВЕТСТВУЮЩИЕ СТРОЧКИ 

ПЕРЕД ЗАПУСКОМ UNBAN ACCOUNT BOT ЗАЙДИТЕ В ФАЙЛ bot.py НАЙДИТЕ СТРОЧКУ
ApplicationBuilder().token("8017924930:AAHGnpx-G-2ow2Z2h0nDXf3SHYVssIdPjZo").build()
И В "ТУТ" ЗАМЕНИТЕ НА СВОЙ ТОКЕН БОТА

ПЕРЕД ЗАПУСКОМ DISCORD SNOS ЗАЙДИТЕ В ФАЙЛ discord.py И В ЖАЛОБАХ ЗАМЕНИТЕ (жертва) НА ЮЗ ВАШЕЙ ЖЕРТВЫ В DISCORD

ПЕРЕД ЗАПУСКОМ OBFUSCATOR(MEDIUM) ВАМ НУЖНО НЕ ЗАШИФРОВАННЫЙ ФАЙЛ ПЕРЕИМЕНОВАТЬ В script.py НА ВЫХОДЕ ПОЛУЧИТСЯ kapral.py

ПЕРЕД ЗАПУСКОМ SEND MAIL ЗАЙДИТЕ В ФАЙЛ send.py И ИЗМЕНИТЕ SUBJECT ="сюда тему" НА СВОЮ ТЕМА ПИСЬМА

ИЗ ЛЮБОГО СОФТА ГДЕ НЕТ ВЫХОДА МОЖНО ВЫЙТИ CTRL +C!!!
"""
    print(Colorate.Horizontal(Colors.red_to_white,(xyec)))

while True:
    xyu()
    exit = input(Fore.RED + "Нажми ENTER что бы выйти" + Style.RESET_ALL)
    if exit == '':
      break 
               