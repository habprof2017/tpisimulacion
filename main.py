from telegram.ext import Updater, CommandHandler
from lotes import lote1, lote2
import random

miToken = '516240962:AAHexC09397nI_QTtlQbG5-SDjCfJbaQ2lM'
# token_japo = '516240962:AAHexC09397nI_QTtlQbG5-SDjCfJbaQ2lM'
# token_simulacion = '523275871:AAF-k2MiPzgiIwCL_vt539C3T0pi-RBILMM'


def start(bot, update):
    live = 'bienvenido!\nSoy el bot del Grupo nº 3.\n\n\
El comando /menu muestras las opciones'
    msj = 'Hola {} {}'.format(update.message.from_user.first_name, live)
    bot.send_message(chat_id=update.message.chat_id, text=msj)


def funcionSaludar(bot, update):
    va = 'estoy vivo!'
    msj = 'Hola {} {}'.format(update.message.from_user.first_name, va)
    bot.send_message(chat_id=update.message.chat_id, text=msj)


def generador(lote):
    minLote = min(lote)
    maxLote = max(lote)
    r = round(random.random(), 6)

    valor = round(round(maxLote - minLote, 6) * r + minLote, 6)

    return valor


def generarLote1(bot, update, args):  # /generar lote1
    if args[0] == 'lote1':
        titulo = "Generador de variable para lote 1"
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        valor = generador(lote1)
        msj = "Xi: {}".format(valor)
        bot.send_message(chat_id=update.message.chat_id, text=msj)
    elif args[0] == 'lote2':
        titulo = "Generador de variable para lote 2"
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        valor = generador(lote2)
        msj = "Xi: {}".format(valor)
        bot.send_message(chat_id=update.message.chat_id, text=msj)
    elif args[0] == " ":
        error = "Error: falta el lote"
        formato = "formato /generar lote1"
        bot.send_message(chat_id=update.message.chat_id, text=error)
        bot.send_message(chat_id=update.message.chat_id, text=formato)
    else:
        error = "error en el comando"
        formato = "formato /generar lote1"
        bot.send_message(chat_id=update.message.chat_id, text=error)
        bot.send_message(chat_id=update.message.chat_id, text=formato)


def generarLote2(bot, update, args):  # /generar lote1
    if args[0] == 'lote1':
        titulo = "Generador de variable para lote 1"
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        valor = generador(lote1)
        msj = "Xi: {}".format(valor)
        bot.send_message(chat_id=update.message.chat_id, text=msj)
    elif args[0] == 'lote2':
        titulo = "Generador de variable para lote 2"
        bot.send_message(chat_id=update.message.chat_id, text=titulo)
        valor = generador(lote2)
        msj = "Xi: {}".format(valor)
        bot.send_message(chat_id=update.message.chat_id, text=msj)
    elif args[0] == " ":
        error = "Error: falta el lote"
        formato = "formato /generar lote1"
        bot.send_message(chat_id=update.message.chat_id, text=error)
        bot.send_message(chat_id=update.message.chat_id, text=formato)
    else:
        error = "error en el comando"
        formato = "formato /generar lote1"
        bot.send_message(chat_id=update.message.chat_id, text=error)
        bot.send_message(chat_id=update.message.chat_id, text=formato)


def main():
    updater = Updater(token=miToken)
    dispatcher = updater.dispatcher

    handlers = [
        CommandHandler('start', start),
        CommandHandler('saluda', funcionSaludar),
        CommandHandler('lote1', generarLote1, pass_args=True),
        CommandHandler('lote2', generarLote2, pass_args=True),
        # generarLote es la funcion de python
        # /generar es el comando en telegram
    ]

    for handler in handlers:
        dispatcher.add_handler(handler)

    # dispatcher.add_handler(conv_handler) echarle un ojo tu debes xD

    updater.start_polling()  # Start the bot

    updater.idle()  # Run the bot until you press Ctrl-C


if __name__ == '__main__':
    main()
