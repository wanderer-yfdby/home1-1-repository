import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('Здесь будет ваш токен')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Мир вам! Господь ждет встречи с вами всеГда!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

now = datetime.datetime.now().strftime('%H:%M')
print(now)


@bot.message_handler(commands=['quote'])
def quote_message(message):
    list = ["Матфея 21:22\n - И все, чего ни попросите в молитве с верою, получите.",
            "Матфея 6:6\n — Но ты, когда молишься, войди в свою комнату и, заперев дверь свою,"
            "помолись Отцу твоему, Который втайне; и Отец твой, видящий втайне, воздаст тебе явно.",
            "Марка 11:24\n — Посему говорю вам: всё, чего ни попросите в молитве, веруйте, что получите, и будет вам.",
            "Луки 11:9\n — И Я говорю вам: просите, и дано будет вам; ищите, и найдете; стучите, и отворят вам.",
            "Иоанна 16:24\n — Доселе вы не просили ничего во имя Мое; просите, и получите,"
            "чтобы радость ваша была совершенна.",
            "Матфея 6:7\n — А когда молитесь, не умножайте пустословия, как язычники,"
            "ибо они думают, что во многословии своем будут услышаны.",
            "Матфея 26:41\n — Бодрствуйте и молитесь, чтобы не впасть в искушение: дух бодр, но плоть немощна.",]
    random_quote = random.choice(list)
    bot.reply_to(message, f'Библия напоминает в евангелии от \n{random_quote}')

def send_reminders(chat_id):
    morning_rem = "05:00"
    midday_rem = "12:30"
    afternoon_rem = "16:30"
    evening_rem = "20:30"
    end_rem = "00:00"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == morning_rem:
            bot.send_message(chat_id, "Время утренней молитвы")
            time.sleep(61)
        time.sleep(1)
        if now == midday_rem:
            bot.send_message(chat_id, "Время полуденной молитвы")
            time.sleep(61)
        time.sleep(1)
        if now == afternoon_rem:
            bot.send_message(chat_id, "Время послеполуденной молитвы")
            time.sleep(61)
        time.sleep(1)
        if now == evening_rem:
            bot.send_message(chat_id, "Время вечерней молитвы")
            time.sleep(61)
        time.sleep(1)
        if now == end_rem:
            bot.send_message(chat_id, "Время ночной молитвы")
            time.sleep(61)
        time.sleep(1)



bot.polling(none_stop=True)
