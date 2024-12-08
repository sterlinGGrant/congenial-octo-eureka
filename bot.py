import smtplib
from email.mime.text import MIMEText
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler, ContextTypes
import smtplib
from email.mime.text import MIMEText
from email.header import Header


smtp_settings = {
    "smtp_server": "smtp.gmail.com",
    "smtp_server": "smtp.yandex.com",
    "smtp_server": "smtp.hotmail.com",
    "smtp_server": "smtp.mail.com",
    "smtp_port": 587,          
    "smtp_port": 465,      
}
# Состояния для диалога
EMAIL, PASSWORD, MESSAGE = range(3)

# Адрес получателя
recipient_email = "abuse@telegram.org"


def send_email(from_address, password, subject, body):
    msg = MIMEText(body, _charset='utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = from_address
    msg['To'] = recipient_email  

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(from_address, password)  # Убедитесь в правильности логина и пароля
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Ошибка при отправке почты: {e}")
        return False
        
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привет! Пожалуйста, введите свою почту:")
    return EMAIL

async def set_email(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['email'] = update.message.text.strip()
    await update.message.reply_text("Вы установили свою почту. Теперь введите свой пароль:")
    return PASSWORD

async def set_password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['password'] = update.message.text.strip()
    await update.message.reply_text("Пароль успешно установлен. Теперь введите вашу заявку:")
    return MESSAGE

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_email = context.user_data.get('email')
    user_password = context.user_data.get('password')

    user_message = update.message.text

    subject = "Заявка от пользователя Telegram"
    email_body = f"Пользователь: {update.message.from_user.username}\n\nСообщение:\n{user_message}"

    if send_email(user_email, user_password, subject, email_body):
        await update.message.reply_text("Ваша заявка отправлена в поддержку!")
    else:
        await update.message.reply_text("Произошла ошибка при отправке заявки. Попробуйте еще раз.")

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Операция отменена.")
    return ConversationHandler.END

def main() -> None:
    application = ApplicationBuilder().token("8017924930:AAHGnpx-G-2ow2Z2h0nDXf3SHYVssIdPjZo").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_email)],
            PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_password)],
            MESSAGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)

    print("Бот запущен и готов к работе!\n")
    application.run_polling()
    
    
if __name__ == '__main__':
    main()
