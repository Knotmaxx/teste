import telebot

bot = telebot.TeleBot("5120413625:AAGmo0oeON97mHd_oZhmM9LrzlMm_Ch_h84")

@bot.message_handler(func= lambda m : True)
def responder(mensagem):
	bot.send_message(mensagem.chat.id, "olá, o bot está funcionando!")


bot.polling()
