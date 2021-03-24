from telebot import TeleBot
from telebot import types
from random import randint
from mainOOP import Reader_bot

TOKEN = "1627632669:AAEQsLcFGxo89xeH5LuhqrYVTw-Mg8Gk3cU"

# create an instance of TeleBot class
bot = TeleBot(TOKEN)
notes0 = Reader_bot()
paper_arg = 'graph'
font_arg = "Abram"
ink_arg = "blue"

def p_or_t(message):
    question = """Я стараюсь быть умным - мне можно отправить фото учебника, а я считаю информацию и перепишу на листочек.
Но если отправишь обычным текстом, проблем тоже не будет 😊"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Картинка", callback_data='picture')
    item2 = types.InlineKeyboardButton("Текст", callback_data='plain text')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, question, reply_markup=markup)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # send the sticker
    sti = open("stickerCAT.webp", 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 'Здарова. Конспект делать будем? Если что, пиши "/notes"')


@bot.message_handler(commands=["notes"])
def ask_settings(message):
    if message.chat.type == 'private':
        question = "Отлично, будем делать дополнительные настройки? Подробнее можно прочитать в моём описании (в самом 1 сообщении)"

        # inline keyboard
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Будем", callback_data='1')
        item2 = types.InlineKeyboardButton("Не будем", callback_data='0')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, question, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "бот только для личных сообщений 😥")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global notes0, paper_arg, font_arg, ink_arg
    try:
        if call.message:

            ID = call.message.chat.id

            if call.data == '1':
                """
                Settings: 
                    font, 
                    paper, 
                    ink
                """
                bot.send_message(ID, """Напиши что ты хочешь. 3 параметра:"
 1) тип разлиновки листа:
 в клетку(graph) / в линейку(lined) / пустой(A4)
 2) почерк
 (1/2/3/4)
 p.s внизу они все представлены
 3) цвет чернил:
 фиолетовый(purple)/синий(blue)/темно-синий(blueM)/черный(black)
 
 НАЧНИ СООБЩЕНИЕ С "**" и пиши без "," ☺
 Например: ** lined 1 blueM
 
 можно пропустить этот шаг и сразу прислать мне фото/текст. Тогда поставятся клечатая разлиновка, синие чернила и 1 почерк))
 """)
                bot.send_photo(ID,
                               'https://t4569419.p.clickup-attachments.com/t4569419/98a68dda-22c0-4800-afae-9428dfd87de6/inLine0.png')
                bot.send_photo(ID,
                               'https://t4569419.p.clickup-attachments.com/t4569419/e9a4efdb-e79e-4081-820a-798953ed51d6/A41.png')
                bot.send_photo(ID,
                               'https://t4569419.p.clickup-attachments.com/t4569419/f7bb1cec-7bb8-441b-a344-bdfc4e974417/Int2.png')
                bot.send_photo(ID,
                               'https://t4569419.p.clickup-attachments.com/t4569419/ada07f52-53e3-4bcf-97cf-461dfb62855c/inLine3.png')

            elif call.data == '0':
                question = bot.send_message(call.message.chat.id, 'Тогда сразу к делу.')

                p_or_t(question)

            elif call.data == 'picture':
                bot.send_message(call.message.chat.id, "Присылай 👇🏻")

            elif call.data == 'plain text':
                bot.send_message(call.message.chat.id, "Присылай 👇🏻")

    except ValueError as e:
        bot.send_message(call.message.chat.id, "Ой, что-то пошло не так")
        sad_sti = open("stickerERROR.webp", 'rb')
        bot.send_sticker(call.message.chat.id, sad_sti)


@bot.message_handler(content_types=['photo'])
def get_picture(message):
    global notes0
    try:
        chat_id = message.chat.id
        bot.send_message(chat_id, "Подожди секунду ...")
        file_info = bot.get_file(message.photo[0].file_id)
        name = file_info.file_path

        downloaded_file = bot.download_file(name)

        saved = "D:/PYTHON/fineReader_bot/received/" + name[name.index('/') + 1:];

        with open(saved, 'wb') as new_file:
            new_file.write(downloaded_file)

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

    except Exception as error:
        bot.send_message(chat_id, "Ой, что-то пошло не так")
        sad_stickers = ["stickerSURPRISED.webp", "stickerFROWN.webp", "stickerQ.webp", "stickerQ.webp",
                        "stickerQ1.webp", "stickerQ2.webp"]
        sad_sti = open(sad_stickers[randint(0, 5)], 'rb')
        bot.send_sticker(message.chat.id, sad_sti)


@bot.message_handler(content_types=['text'])
def from_text(message):
    global notes0
    try:
        if message[:2] == "**":
            options = message[3:].split()
            notes0 = Reader_bot(options[0], options[1], int(options[2]) - 1)

        chat_id = message.chat.id

        notes0.put_text(message.text)

        # to send the result
        bot.send_photo(chat_id, notes0.image)

    except Exception as error:
        bot.send_message(chat_id, "Ой, что-то пошло не так")
        sad_stickers = ["stickerSURPRISED.webp", "stickerFROWN.webp", "stickerQ.webp", "stickerQ.webp",
                        "stickerQ1.webp", "stickerQ2.webp"]
        sad_sti = open(sad_stickers[randint(0, 5)], 'rb')
        bot.send_sticker(message.chat.id, sad_sti)


bot.polling(none_stop=True, interval=0)
