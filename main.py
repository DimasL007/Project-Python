import telebot

# Введіть свій токен
TOKEN = '8050463288:AAEDYu9o3I3NCKhhbPplOlYeENudkxCWrOI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)

