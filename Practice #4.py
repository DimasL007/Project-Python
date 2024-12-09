import telebot

# Токен
TOKEN = '8050463288:AAEDYu9o3I3NCKhhbPplOlYeENudkxCWrOI'  # Унікальний токен Бота
bot = telebot.TeleBot(TOKEN)  #Бот з використанням токена для обробки всіх повідомлень і іниших дій

# Обробник повідомлень
@bot.message_handler(func=lambda message: True)  # Фільтр для обробки всіх типів повідомлень
def echo_message(message):  # Функція обробника повідомлень
    bot.reply_to(message, message.text)  # Відправляє відповідь із текстом того самого повідомлення яке було відправлене користувачем
# message - текст отриманого повідомлення

# Основний блок виконання-
if __name__ == '__main__':  # Перевіряє, чи файл запущений напряму
    bot.polling(none_stop=True)  # Запускає постійне опитування сервера Telegram для отримання нових повідомлень
