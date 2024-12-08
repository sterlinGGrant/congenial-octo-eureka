import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, message):
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = 'сюда жалобу'
                msg.attach(MIMEText(message, 'plain'))
                server.sendmail(sender_email, receiver_email, msg.as_string())
                server.quit()
                print("Письмо успешно отправлено!")
            except Exception as e:
                print(f"Ошибка при отправке письма: {e}")

senders = {
            'anonymous854785@gmail.com': 'wmth dinz jiek nhfy',
            'andeybirum@gmail.com': 'ouho uujv htlm rwaz',
            'faverokstandof@gmail.com': 'nrsg kchi etta uuzh',
            'faveroktt@gmail.com': 'dywo rgle jjwl hhbq',
            'mksmksergeev@gmail.com': 'ycmw rqii rcbd isfd',
            'maksimafanacefish@gmail.com': 'hdpn tbfp acwv jyro'
        }
gmail = input('Куда: ')
receivers = [f'{gmail}']
message = input('Текст: ')

for sender_email, sender_password in senders.items():
            for receiver_email in receivers:
                send_email(sender_email, sender_password, receiver_email, message)