# importar librearia que hemos instalado
from telegram.ext import Updater, CommandHandler

#definir el handler
def start(update, context):

    update.message.reply_text('hola, Humano!')

if __name__ == "__main__":
    updater = Updater(token="YOUR_TOKEN", use_context=True)
    dp = updater.dispatcher

    #agnadir un handler de comando
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
