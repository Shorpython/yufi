import telebot
import time
bot = telebot.TeleBot('1560128117:AAFY7IVAXOY1GeiprDjnilhTEzLF5JWoqc0')
admin_list = (62263986721, 6226398671)
msg = ('Принял','принял','ПРИНЯЛ')
idex = 0
@bot.message_handler(content_types=['text'])
def handler_test(message):
    if not message.from_user.id in admin_list:
        if not message.text in msg:
            bot.delete_message(message.chat.id, message.message_id)
            msgid = bot.send_message(message.chat.id, 'Соблюдайте правильную форму сообщения!')
            time.sleep(1)          
            bot.delete_message(message.chat.id, msgid.message_id)
        else:
            bot.send_message(message.chat.id, 'Ваша заявка принята в обработку, скоро с вами свяжется диспетчер.')
bot.polling(none_stop=True)
