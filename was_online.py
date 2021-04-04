import subprocess
import datetime
# import re
import telebot
import pathlib

token = open("Bot/token").read()
bot = telebot.TeleBot(token)

HELP = '''
Вот команды, которые я понимаю:
/status имя пользователя - получение статуса пользователя. Пользователь должен быть у тебя в контактах.
/stop - моя остановочка
'''
get_start = "/start"
get_stop = "/stop"
get_help = "/help"
get_status = "/status"

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == get_start:
        msg = "Привет, " + message.from_user.username + "!\n" + HELP
        bot.send_message(message.from_user.id, msg)
    elif message.text.find(get_status) != -1:
        name = message.text[8:]
        name = name.replace(' ', '_')
        path = str(pathlib.Path.cwd()) + "/Bot/tg.sh"
        subroc_result = subprocess.check_output([path, name])
        subroc_result = subroc_result.decode('utf-8')
        subroc_result = "\n" + subroc_result + "\n"

        # Removing ANSI characters using Python
        # 7-bit C1 ANSI sequences
        # ansi_escape = re.compile(r'''
        #     \x1B  # ESC
        #     (?:   # 7-bit C1 Fe (except CSI)
        #         [@-Z\\-_]
        #     |     # or [ for CSI, followed by a control sequence
        #         \[
        #         [0-?]*  # Parameter bytes
        #         [ -/]*  # Intermediate bytes
        #         [@-~]   # Final byte
        #     )
        # ''', re.VERBOSE)

        # subroc_result = ansi_escape.sub('', subroc_result)

        date_and_time = datetime.datetime.today()
        subroc_result= '\n\n\n' + date_and_time.strftime("%c") + '\n\n' + subroc_result
        bot.send_message(message.from_user.id, subroc_result)
        f = open("Bot/log", "a")
        f.write(subroc_result)
        f.close()

    elif message.text == get_help:
        bot.send_message(message.from_user.id, HELP)

bot.polling()