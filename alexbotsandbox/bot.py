#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'сюда ставить токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('AnimatedSticker.tgs', 'rb',)
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("📁 My GitHub")
	item2 = types.KeyboardButton("💬 Send Me Message")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать!, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '📁 My GitHub':
			bot.send_message(message.chat.id, 'https://github.com/AlexSol0d')
		elif message.text == '💬 Send Me Message':
			bot.send_message(message.chat.id, 'https://t.me/Alexey_Solodovnikov')
		else:
			bot.send_message(message.chat.id, 'это бот, а не чат 😢')


bot.polling(none_stop=True)