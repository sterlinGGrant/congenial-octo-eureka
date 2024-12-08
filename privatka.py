
import asyncio
import os
import re
import time
from colorama import Fore, Style
from telethon import TelegramClient, events
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import config

client = TelegramClient('session', config.api_id, config.api_hash)

async def get_channel_id():
    while True:
        raw_channel_id = input("[+] Введите ID: ")
        try:
            channel_id = int(raw_channel_id)
            return channel_id
        except ValueError:
            print("[-] Введенный ID канала некорректен. Пожалуйста, введите корректный ID.")

async def get_channel_name(channel_id):
    try:
        full_chat = await client(GetFullChannelRequest(channel_id))
        if full_chat:
            return full_chat.chats[0].title
    except Exception as e:
        print(f"[-] Не удалось получить информацию о канале: {e}")
    return None

async def activate_channel(channel_link):
    try:
        result = await client(ImportChatInviteRequest(channel_link))
        channel_name = result.chats[0].title
        print(f"[+] Присоединился к каналу: {Fore.GREEN}{channel_name}{Style.RESET_ALL}")
        return channel_name
    except Exception as e:
        print(f"[-] Ошибка при активации канала: {e}")
        return None

async def main():
    try:
        await client.start()
        channel_id = await get_channel_id() 
        tracked_channel_name = await get_channel_name(channel_id)
        if tracked_channel_name:
            print(f"[+] Отслеживаемый канал: {Fore.GREEN}{tracked_channel_name}{Style.RESET_ALL}")
        else:
            print(f"[+] Не удалось получить информацию о канале с ID: {channel_id}")

        @client.on(events.NewMessage(chats=channel_id))
        async def handle_new_message(event):
            start_time = time.time()
            message_text = event.message.text
            url_regex = re.compile(r"https:\/\/t\.me\/\+([\w-]{1,})(?![\w-]*\?)|joinchat\/([\w-]+)", re.IGNORECASE)

            urls = url_regex.findall(message_text)
            if urls:
                unique_urls = set()
                for url_tuple in urls:
                    for url in url_tuple:
                        if url and url not in unique_urls:
                            unique_urls.add(url)
                            print(f"[+] Найдена ссылка: {Fore.CYAN}{url}{Style.RESET_ALL}")
                            priv_channel_name = await activate_channel(url)
                            if priv_channel_name:
                                end_time = time.time()
                                elapsed_time = end_time - start_time
                                print(f"[+] Приватка словлена за: {elapsed_time:.3f} секунд")
                            else:
                                print("[-] Ошибка при активации канала")
                                end_time = time.time()
                                elapsed_time = end_time - start_time
                                print(f"[-] Время на словление: {elapsed_time:.3f} секунд.")

        await client.run_until_disconnected()
    except Exception as e:
        error_message = f"Ошибка соединения: {e}"
        print(error_message)  

asyncio.run(main())