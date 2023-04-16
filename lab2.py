import argparse
import telegram
import time

def main():
    # Отримати аргументи командного рядка
    parser = argparse.ArgumentParser()
    parser.add_argument('--bot-token', required=True, help='Telegram bot token')
    parser.add_argument('--chat-id', required=True, help='Telegram chat ID')
    args = parser.parse_args()

    # Створити об'єкт бота
    bot = telegram.Bot(token=args.bot_token)

    # Відправити повідомлення
    chat_id = args.chat_id
    message = 'Привіт, я працюю'
    bot.send_message(chat_id=chat_id, text=message)

    # Зачекати 5 секунд
    time.sleep(5)

if __name__ == '__main__':
    main()
