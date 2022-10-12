# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import telebot
import random

bot = telebot.TeleBot(');
adminId = '988577610';
testerID = '44055775';


@bot.message_handler(commands=["start"])
def start(m, res=False):
    if str(m.chat.id) == adminId:
        bot.send_message(m.chat.id, 'Приветствую, мой создатель! Хорошего времени суток!');

    bot.send_message(m.chat.id,
                     'Привет привет! В этом боте можно узнать информацию про вечеринку ДСО в эту субботу (15.10) и выйграть супер призы!\n(Иногда бот может не отвечать, это нормально, он обязательно ответит через какое-то небольшое время)')

    keyboard = telebot.types.InlineKeyboardMarkup();  # наша клавиатура
    key_yes = telebot.types.InlineKeyboardButton(text='УЗНАТЬ ПРО ДСО', callback_data='info');  # кнопка «Да»
    keyboard.add(key_yes);  # добавляем кнопку в клавиатуру
    key_no = telebot.types.InlineKeyboardButton(text='УЧАСТВОВАТЬ В РОЗЫГРЫШЕ', callback_data='roll');
    keyboard.add(key_no);
    question = 'Жми на кнопки!'
    bot.send_message(m.chat.id, text=question, reply_markup=keyboard)


@bot.message_handler(commands=["help"])
def help(mes, res=False):
    bot.send_message(mes.chat.id, 'Запусти команду /start и жми на кнопки :)');


@bot.message_handler(commands=["info"])
def help(mes, res=False):
    bot.send_message(mes.chat.id, 'Клубный-техно-инфо-бот РМЦ\nЗапусти команду /start и жми на кнопки :)');


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id,
                     'Не, ну я так ничего не понимаю. Лучше жми на кнопки! /start ' + str(message.chat.id))


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "info":
        bot.send_message(call.message.chat.id,
                         'Узнать про вечеринку в инсте: https://www.instagram.com/p/CjctXp8oVQ2/\nУзнать в телеге: https://t.me/rmcclub/6258');
    elif call.data == "roll":
        if str(call.from_user.id) == adminId:
            bot.send_message(call.message.chat.id,
                             'Не можешь натестироваться? :))))))')
            return;

        if str(call.from_user.id) == testerID:
            bot.send_message(call.message.chat.id,
                             'Саня, ты и так можешь позволить себе все, оставь другим :)))))))))')
            return;

        rFile = open('list.txt', 'r');
        idList = [str(line.replace('\n', '')) for line in rFile];
        rFile.close();

        if (str(call.from_user.id) in idList):
            bot.send_message(call.message.chat.id,
                             'Ага, кажется кто-то уже участвовал в розыгрыше. Лучше приходи к нам на ДСО! (Остановка бота, удаление диалога и т.п. увы не прокатят :))')
            return;

        answer = roll();
        wFile = open('list.txt', 'a');
        wFile.write(str(call.from_user.id) + '\n');
        wFile.close();

        if answer == 0:
            winFile = open('winners.txt', 'a');
            winFile.write(str(call.from_user.id) + ' Депозит \n');
            wFile.close();

            photo = open('deposit.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                             'Ты выйграл депозит* 1500 (!!!) на баре! Поздравляем, покажи это сообщение на баре на вечеринке ДСО в эту субботу.');
            bot.send_message(call.message.chat.id,
                             '*депозит действует только на вечеринке ДСО (15.10)');
        elif answer == 2:
            winFile = open('winners.txt', 'a');
            winFile.write(str(call.from_user.id) + ' Джин \n');
            wFile.close();

            photo = open('lavandosik.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                             'УАУАУ!  Ты выйграл бесплатный джин-тоник на вечеринке ДСО (15.10)\nПриходи тусить и покажи это сообщение на баре!');
        elif answer == 1:
            winFile = open('winners.txt', 'a');
            winFile.write(str(call.from_user.id) + ' Настойки \n');
            wFile.close();

            photo = open('shot.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                             'УАУАУ!  Ты выйграл бесплатный сет из трёх настоек на вечеринке ДСО (15.10).\nПриходи тусить и покажи это сообщение на баре!');
        else:
            winFile = open('winners.txt', 'a');
            winFile.write(str(call.from_user.id) + ' Скидка \n');
            wFile.close();

            photo = open('ticket.jpg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id,
                             'Ты выйграл скидку 100 рублей на вход на вечеринку ДСО в эту субботу!.\nПокажи это сообщение на входе!');


def roll():
    chance = random.randint(0, 100);

    gFile = open('gifts.txt', 'r');
    giftsList = [int(str(line.replace('\n', ''))) for line in gFile];

    if chance == 77:
        if giftsList[2] != 0:
            giftsList[2] = giftsList[2] - 1;
            gFile.close()
            gFile = open('gifts.txt', 'w');

            for gift in giftsList:
                gFile.write(str(gift) + '\n');

            gFile.close();
            return 0

        gFile.close();
        return 3

    if chance % 10 == 1:
        if giftsList[0] != 0:
            giftsList[0] = giftsList[0] - 1;
            gFile.close()
            gFile = open('gifts.txt', 'w');

            for gift in giftsList:
                gFile.write(str(gift) + '\n');

            gFile.close();
            return 1

        gFile.close();
        return 3

    if chance % 10 == 2:
        if giftsList[1] != 0:
            giftsList[1] = giftsList[1] - 1;
            gFile.close()
            gFile = open('gifts.txt', 'w');

            for gift in giftsList:
                gFile.write(str(gift) + '\n');

            gFile.close();
            return 2

        gFile.close();
        return 3

    gFile.close();
    return 3


bot.polling(none_stop=True, interval=0)
