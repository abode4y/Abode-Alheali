import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = '7149873557:AAHAPFqgB380RDwUcWp6bhdTq4cUCIBAoeU'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبا! أرسل لي /star لدعمي بنجمة.')

def star(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("User %s sent a star.", user.first_name)
    with open("stars.txt", "a") as file:
        file.write(f"{user.first_name} {user.last_name} ({user.username})\n")
    update.message.reply_text('شكراً لدعمك!')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("star", star))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
