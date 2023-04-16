import telebot
import time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bot-token', required=True, help='Telegram bot token')
    parser.add_argument('--chat-id', required=True, help='Telegram chat ID')
    args = parser.parse_args()

    bot = telebot.TeleBot(args.bot_token)

    chat_id = args.chat_id
    message = 'Привіт, я працюю'
    bot.send_message(chat_id, message)

    time.sleep(5)

if __name__ == '__main__':
    main()
