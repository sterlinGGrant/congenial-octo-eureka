import os
from colorama import Fore, Style
import colorama

def replace_chars(text, use_fence):
    replacements = {
        'А': 'А', 'а': 'а', 'Б': 'Б', 'б': 'б', 'В': 'B', 'в': 'в', 'Г': 'Г', 'г': 'г', 
        'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'Ё', 'ё': 'ё', 'Ж': 'Ж', 'ж': 'Ж', 
        'З': '3', 'з': '3', 'И': 'U', 'и': 'u', 'й': 'й', 'К': 'K', 'к': 'k', 'Л': 'JI', "л": "JI",
        'М': 'M', 'м': 'м', 'Н': 'Н', 'н': 'н', 'о': '0', 'п': 'n', 'р': 'p', 'с': 'c', "С": "S",
        'т': 'T', 'у': 'y', 'ф': 'ф', 'х': 'x', 'ч': '4', "Ч": "4",'ш': 'III', "Ш": "III", 'щ': 'щ', 'ъ': 'ъ', 
        'ы': 'bI', "Ы": "bI", 'ю': 'ю', 'я': 'я'
    }
    result = ''
    for char in text:
        if use_fence:
            result += replacements.get(char.upper(), char)
        else:
            result += replacements.get(char.upper(), char.upper())
    return result

print("1. ВыВоД вИдЕ зАбОрА.\n2. ВСЕ ЗАГЛАВНЫЕ.\n")
option = input("Выберите опцию:")
if option not in ['1', '2']:
    print("Неправильно выбранная опция попробуй еще раз")
    exit()

if option == '1':
    user_input = input(Fore.YELLOW + "Введите текст -> " + Style.RESET_ALL)
    replaced_text = replace_chars(user_input, True)
    print(Fore.GREEN + "Результат замены:/n" + Style.RESET_ALL)
    print(Fore.GREEN + replaced_text + Style.RESET_ALL)
else:
    user_input = input(Fore.YELLOW + "Введите текст -> " + Style.RESET_ALL)
    replaced_text = replace_chars(user_input, False)
    print(Fore.GREEN + "Результат замены:\n" + Style.RESET_ALL)
    print(Fore.GREEN + replaced_text + Style.RESET_ALL)

while True:
    exit = input(Fore.YELLOW + "нажми ENTER что бы выйти" + Style.RESET_ALL)
    if exit == '':
      break 

