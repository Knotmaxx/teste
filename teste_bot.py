import telebot

bot = telebot.TeleBot("token")

@bot.message_handler(func= lambda m : True)
def responder(mensagem):
      bot.send_message(mensagem.chat.id, "Olá, o bot está funcionando!")

bot.polling()
