from telebot import TeleBot
from telebot import types
from random import randint
from mainOOP import Reader_bot

TOKEN = "1627632669:AAEQsLcFGxo89xeH5LuhqrYVTw-Mg8Gk3cU"

# create an instance of TeleBot class
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # send the sticker
    sti = open("stickerCAT.webp", 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 'Здарова. Конспект делать будем? Если что, пиши "/notes"')


@bot.message_handler(commands=["notes"])
def ask_settings(message):
    if message.chat.type == 'private':
        question = """Я стараюсь быть умным - мне можно отправить фото учебника, а я считаю информацию и перепишу на листочек.
Но если отправишь обычным текстом, проблем тоже не будет 😊"""
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Картинка", callback_data='picture')
        item2 = types.InlineKeyboardButton("Текст", callback_data='plain text')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, question, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "бот только для личных сообщений 😥")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
            if call.data == 'picture':
                bot.send_message(call.message.chat.id, "Присылай 👇🏻")

            elif call.data == 'plain text':
                bot.send_message(call.message.chat.id, "Присылай 👇🏻")

    except ValueError as e:
        bot.send_message(call.message.chat.id, "Ой, что-то пошло не так")
        sad_sti = open("stickerERROR.webp", 'rb')
        bot.send_sticker(call.message.chat.id, sad_sti)


@bot.message_handler(content_types=['photo'])
def get_picture(message):
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, "Подождите секунду ...")
        file_info = bot.get_file(message.photo[0].file_id)
        name = file_info.file_path

        downloaded_file = bot.download_file(name)

        saved = "D:/PYTHON/fineReader_bot/received/" + name[name.index('/') + 1:];

        with open(saved, 'wb') as new_file:
            new_file.write(downloaded_file)
        notes0 = Reader_bot()

        notes0.get_text(saved)
        notes0.prepare_text()
        notes0.put_text()

        # to send the result
        bot.send_photo(chat_id, notes0.image)

    except ValueError:

        bot.send_message(chat_id, """Не могу считать текст. Попробуйте
    1. Сфотографировать под прямым углом
    2. Разгладьте бумагу
    3. Убедитесь, что текст состоит из русских слов""")
        sad_sti = open("stickerQ1.webp", 'rb')
        bot.send_sticker(chat_id, sad_sti)

    except IndexError:
        bot.send_message(chat_id, "Слишком много текста. Пропробуйте прислать по фрагментам")
        sad_stickers = ["stickerSURPRISED.webp", "stickerFROWN.webp", "stickerQ.webp", "stickerQ.webp",
                             "stickerQ1.webp", "stickerQ2.webp"]
        sad_sti = open(sad_stickers[randint(0, 5)], 'rb')
        bot.send_sticker(message.chat.id, sad_sti)

    except Exception as error:
        bot.send_message(chat_id, "Ой, что-то пошло не так")
        sad_stickers = ["stickerSURPRISED.webp", "stickerFROWN.webp", "stickerQ.webp", "stickerQ.webp",
                        "stickerQ1.webp", "stickerQ2.webp"]
        sad_sti = open(sad_stickers[randint(0, 5)], 'rb')
        bot.send_sticker(message.chat.id, sad_sti)


@bot.message_handler(content_types=['text'])
def from_text(message):
    try:
        notes0 = Reader_bot()
        chat_id = message.chat.id

        notes0.prepare_text(message.text)
        notes0.put_text()

        # to send the result
        bot.send_photo(chat_id, notes0.image)

    except Exception as error:
        bot.send_message(chat_id, "Ой, что-то пошло не так")
        sad_stickers = ["stickerSURPRISED.webp", "stickerFROWN.webp", "stickerQ.webp", "stickerQ.webp",
                        "stickerQ1.webp", "stickerQ2.webp"]
        sad_sti = open(sad_stickers[randint(0, 5)], 'rb')
        bot.send_sticker(message.chat.id, sad_sti)


bot.polling()
