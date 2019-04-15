import random
import replacement
import telebot
from telebot import types
from telebot.types import Message
TOKEN ="smth"

START_MESSAGE = "Привет, я представляю интересы Дмитрия!\n Что-бы узнать список команд, введи /help."
HELP_MESSAGE = "Ну короче кто-то слишком ленивый что бы это заполнять!"
ERROR_MESSAGE = "Что-то пошло не так... Попробуй по другому"
LANG_MESSAGE = "Choose your language/Выберите свой язык/Виберіть свою мову:"
START_MESSAGE = "Ещё не придумал"

lang_quest = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('ua')
itembtn2 = types.KeyboardButton('ru')
itembtn3 = types.KeyboardButton('en')
lang_quest.add(itembtn1, itembtn2, itembtn3)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.reply_to(message, START_MESSAGE)#, reply_markup=lang_quest)
    
@bot.edited_message_handler(commands=['start'])
def send_welcome_edited(message: Message):
    bot.send_message(message.chat.id, START_MESSAGE) #reply_markup=lang_quest)


@bot.message_handler(commands=['help'])
def send_help(message: Message):
    global HELP_MESSAGE
    bot.reply_to(message, str(HELP_MESSAGE))
    
@bot.edited_message_handler(commands=['help'])
def send_help_edited(message: Message):
    global HELP_MESSAGE
    bot.reply_to(message, str(HELP_MESSAGE))


@bot.message_handler(commands=['replacements'])
def send_(message: Message):
    bot.reply_to(message, str(replacement.get_replacement()), parse_mode = "markdown")
    
@bot.edited_message_handler(commands=['replacements'])
def send_help_edited(message: Message):
    bot.reply_to(message, str(replacement.get_replacement()), parse_mode = "markdown")
    
@bot.message_handler(commands=['shedule'])
def send_(message: Message):
    global HELP_MESSAGE
    bot.reply_to(message, str(replacement.get_schedule()))
    
@bot.edited_message_handler(commands=['shedule'])
def send_help_edited(message: Message):
    global HELP_MESSAGE
    bot.reply_to(message, str(replacement.get_schedule()))

@bot.message_handler(commands=['shedrep'])
def send_(message: Message):
    global HELP_MESSAGE
    bot.reply_to(message, str(replacement.get_schedule_with_rep()))
    
@bot.edited_message_handler(commands=['shedrep'])
def send_help_edited(message: Message):
    global HELP_MESSAGE
    bot.reply_to(message, str(replacement.get_schedule_with_rep()))
try:
	print("Working")
	bot.polling()
finally:
	input('Press ENTER to exit')

input('Press ENTER to exit')

