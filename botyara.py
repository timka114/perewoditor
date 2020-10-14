import telebot

token = "1244942422:AAH38te-N-4Wn5LBMPcX30bs-B09FMg2Udc"
data = ["бит", "б", "кб", "мб", "гб", "тб"]

bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def inputText(msg):
    chatId = msg.chat.id
    inputText = msg.text.lower()
    print(inputText)

    input_data = inputText.split()
    from_var = data.index(input_data[1])
    to = data.index(input_data[3])
    num = int(input_data[0])
    minus = from_var - to - 1


    if input_data[1] == "бит":
        minus = from_var - to + 1
        result = num / 8
        new_result = result / 1024 ** abs(minus)
        bot.send_message(chatId, f"Ответ: {new_result} {input_data[3]}")
    elif input_data[3] == "бит":
        minus = from_var - to - 1
        result = num * 1024 ** abs(minus)
        new_result = result * 8
        bot.send_message(chatId, f"Ответ: {new_result} {input_data[3]}")
    else:
        step = from_var - to
        result = num * 1024 ** step
        bot.send_message(chatId, f"Ответ: {result} {input_data[3]}")


bot.polling(none_stop=True)
