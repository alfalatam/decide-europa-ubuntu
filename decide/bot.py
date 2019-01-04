# Importamos las librerías necesarias
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler

# Método que imprimirá por pantalla la información que reciba
def listener(bot, update):
    id = update.message.chat_id
    mensaje = update.message.text

    print("ID: " + str(id) + " MENSAJE: " + mensaje)


# Método que utilizaremos para cuando se mande el comando de "start"
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Bienvenido al bot de Alfonso sobre la plataforma de voto Decide!')


# Método que mandará el mensaje "¡Hola, usuario!"
def hola_mundo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='¡Hola, usuario de Decide!')


# Método que mandará el logo de la página
def logo(bot, update):
    # Enviamos de vuelta una foto. Primero indicamos el ID del chat a donde
    # enviarla y después llamamos al método open() indicando la dónde se encuentra
    # el archivo y la forma en que queremos abrirlo (rb = read binary)
    bot.sendPhoto(chat_id=update.message.chat_id, photo=open('Icono.png', 'rb'))


def main():
    # Creamos el Updater, objeto que se encargará de mandarnos las peticiones del bot
    # Por supuesto no os olvidéis de cambiar donde pone "TOKEN" por el token que os ha dado BotFather
    updater = Updater("753679513:AAHwHg8zTSP6DnXdyQ9GEmLWabY71Y-zW2Y")

    # Cogemos el Dispatcher, en el cual registraremos los comandos del bot y su funcionalidad
    dispatcher = updater.dispatcher

    # Registramos el método que hemos definido antes como listener para que muestre la información de cada mensaje
    listener_handler = MessageHandler(Filters.text, listener)
    dispatcher.add_handler(listener_handler)

    # Ahora registramos cada método a los comandos necesarios
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("holamundo", hola_mundo))
    dispatcher.add_handler(CommandHandler("logo", logo))

    # Y comenzamos la ejecución del bot a las peticiones
    updater.start_polling()
    updater.idle()


# Llamamos al método main para ejecutar lo anterior
if __name__ == '__main__':
    main()