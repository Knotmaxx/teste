import telebot
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton

bot = telebot.TeleBot("2114572410:AAHye0lktWC3fVCeL8e0fkjOf91V_rMlxJI")

def veric(mensagem):
	if len(pedidos) == 3:
		return False
	else:
		return True

def quat(mensagem):
	@bot.message_handler(func=veric)
	def tqua(message):
		while True:
			try:
				if type(int(message.text))  == int:
					pass
			except:
				bot.send_message(message.chat.id,"digite apenas números! Quantas pizzas irá querer?")
				break
			else:
				bot.send_message(message.chat.id,"pedido confirmado.digite /start para voltar para o menu ou clique.")
				pedidos["quantidade"] = message.text
				bot.send_message(mensagem.chat.id,f"Cliente {mensagem.from_user.username} pediu:\n pizza de {pedidos['pizza']}\n tipo: {pedidos['tipo']}\n pediu {pedidos['quantidade']} pizza")
				break

def botao2(mensagem):
		markup = InlineKeyboardMarkup()
		markup.row_width = 1
		markup.add(InlineKeyboardButton("pizza pequena",callback_data = "pequena"),InlineKeyboardButton("pizza media",callback_data = "media"))
		bot.edit_message_text(text ="pizza pequena- + R$ 5,00\n pizza media - +R$10,00",chat_id = mensagem.chat.id,message_id= mensagem.message_id,reply_markup = markup)

def botao(mensagem):
	markup = InlineKeyboardMarkup()
	markup.row_width = 1
	markup.add(InlineKeyboardButton("pizza de calabresa",callback_data = "calabresa"),InlineKeyboardButton("pizza de mussarela",callback_data = "mussarela"))
	bot.edit_message_text(text ="pizza  de calabresa R$ 15,00\npizza de mussarela R$ 12,00",chat_id = mensagem.chat.id,message_id= mensagem.message_id,reply_markup = markup)
	
	


@bot.callback_query_handler(func= lambda m: True)
def Gerenciando_Inline(call):
	if call.data == "Selecionar":
		botao(call.message)
	if call.data in ("calabresa","mussarela"):
		pedidos["pizza"] = call.data
		botao2(call.message)
	if call.data in ("pequena","media"):
		pedidos["tipo"] = call.data
		bot.edit_message_text(text=f"Quantas pizzas de {pedidos['pizza']} vai querer?",chat_id = call.message.chat.id,message_id=call.message.message_id)
		quat(call.message)
	



@bot.message_handler(commands=["start"])
def menu_inicial(mensagem):
	print(mensagem.chat.id)
	markup = InlineKeyboardMarkup()
	markup.add(InlineKeyboardButton("Escolher Pedido", callback_data = "Selecionar"))
	bot.send_message(mensagem.chat.id,f"Olá {mensagem.from_user.username}! seja bem vindo ao bot.teste_pizza. ",reply_markup = markup)
	
pedido = []
pedidos = {}
id = 2081853661

bot.polling()