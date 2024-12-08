import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import datetime
from tqdm import tqdm
from time import sleep
import random
import socks
import socket
from fake_useragent import UserAgent
import random

count = 0

ua = UserAgent()

def my_function():
    global count
    count += 1

def sendemail(senderemail, senderpassword, recipientemail, subject, messagetext):
    try:
        headers = {'User-Agent': ua.random}
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(senderemail, senderpassword)

        message = MIMEMultipart()
        message['From'] = senderemail
        message['To'] = recipientemail
        message['Subject'] = subject

        body = messagetext
        message.attach(MIMEText(body, 'plain'))

        server.send_message(message)
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        my_function()
        print(f"Письмо от {senderemail} успешно отправлено на {recipientemail}\n Всего Отправлено", count, "сообщений\n Текст сообщения", messagetext, "")

        server.quit()
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")

senders = [ 
("editt1345@gmail.com", "hezf xuel hzvz jzur"),
("dlyabravla655@gmail.com", "kprn ihvr bgia vdys"),
("dlatt7055@gmail.com", "tpzd nxle odaw uqwf")
]

recipients = [
"support@discordapp.com",
"support@discordapp.com",
"support@discordapp.com",
"support@discordapp.com",
]

messages = [ # можешь написать и больше сообщений по аналогии
    "Hello, I want to complain about the user (жертва), the fact is that he uses the virtual number: +8801766323470, and also deals with deanonymization of personality and swatting, which violates the rules of your platform! I ask you to block this person for violating the rules of the Messenger!!!",
    "Здравствуйте, хочу пожаловаться на пользователя (жертва), дело в том, что он использует виртуальный номер: +8801766323470, а также занимается деанонимизацией личности и прихлопыванием, что нарушает правила вашей платформы! Прошу заблокировать этого человека за нарушение правил Мессенджера!",
    "Hello, I want to complain about the user (жертва), the fact is that he uses the virtual number: +8801766323470, and also deals with deanonymization of personality and swatting, which violates the rules of your platform!I ask you to block this person for violating the rules of the Messenger!!! BAN HIM! His terrorist Channel",
        "Здравствуйте, хочу пожаловаться на пользователя (жертва), дело в том, что он использует виртуальный номер: +8801766323470, а также занимается деанонимизацией личности и прихлопыванием, лжеминированием, занимается терроризмом, что нарушает правила вашей платформы! Прошу заблокировать этого человека за нарушение правил Мессенджера!!! Его канал с нпрушениями",
            "hello,help me, I want to complain about a user who clearly violates the telegram rules, his account (жертва) this user uses a virtual number +8801766323470, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action!",
]

subjects = [ # можешь написать и больше тем по аналогии
    "Report for User",
    "Reporting",
    "Help pls",
    "Report User",
    "Report",
]

for senderemail, senderpassword in senders:
    for recipientemail in recipients:
        subject = random.choice(subjects)
        messagetext = random.choice(messages)
        sendemail(senderemail, senderpassword, recipientemail, subject, messagetext)
        time.sleep(0) # время задержки между сообщ в секундах
