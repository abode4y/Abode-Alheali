import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# توكن البوت من Telegram
TOKEN = '7149873557:AAHAPFqgB380RDwUcWp6bhdTq4cUCIBAoeU'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    # إعداد السجل
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # إعداد البوت
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # إضافة أوامر
    dispatcher.add_handler(CommandHandler('start', start))

    # بدء البوت
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
