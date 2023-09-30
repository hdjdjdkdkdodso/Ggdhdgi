import requests
import telebot
import random
import time
import os
from random import choice, randint

left = [ "هاي ويييين 💔", "ضلت بس صورهم 🥲","غطو غطو 😂😂"]

welcome_messages = [
    "نورت عيني🙂",
    "نورت اغاتي 😎",
    "شمعة الگروب وصل 😋",
]

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot("5975626400:AAFSMl4fbQ_M-0zC9ve5crKkZvQuuurfQD4")






def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def main():
    while True:
        # التحقق من وجود اتصال بالإنترنت
        if check_internet_connection():
            pass
        else:
            # إيقاف التنفيذ لفترة مؤقتة
            print("انقطع الاتصال بالإنترنت. سيتم الانتظار...")
            time.sleep(60)  # انتظار لمدة دقيقة قبل إعادة التحقق









def clear_console():
    os.system('clear')

def animate_emojis(chat_id, speed=2):
    emojis = "❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️💕💖🧡💛💚💙💜🤎🖤🤍💔💞💓💗💘💝❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️"
    emojis2 = "❤️💕💖🧡💛💚💙💜🤎🖤💔💞💓💗💘💝"
    ali = 1
    while ali < 7:
        ali += 1
        gg = choice(emojis)
        gg2 = choice(emojis2)

        sent_message = bot.send_message(chat_id, gg+gg2 )
        time.sleep(speed)
        bot.delete_message(chat_id, sent_message.message_id)



@bot.message_handler(content_types=[
"new_chat_members"
])
def foo(message):
    random_welcome = random.choice(welcome_messages)
    bot.reply_to(message,random_welcome)
    print("message_new_member")



@bot.message_handler(content_types=[
"left_chat_member"
])
def foo(message):
    Left = random.choice(left)
    bot.reply_to(message,Left)



@bot.message_handler(func=lambda message: message.content_type == 'text')
def respond_to_messages(message):
    text = message.text.lower()

    # قائمة بالرسائل والردود المقترنة
    messages_and_responses = {
        "السلام عليكم": "ۆعلُيَگم آلُسلُآم آغَآتٌيَ 🤧",
        "شلونج": "آلُحٍـمدِ لُلُہ 😁",
        "دومج": "دِآمتٌ آيَآمگم حٍـيَآتٌيَ🕊️",
        "دومك": "دِآمتٌ آيَآمگ گلُبْيَ ❤️",
        "اه": "ۆجٍعآ😂",
        "شخبارك": "بْخـيَر آڏآ آنْتٌة بْخـيَر 👀",
        "شبيج": "آنْتٌة شُبْيَگ 😕",
        "مدري": "شتدرون بعد 😑ٌ",
        "بعد روحي":"حٍـيَآتٌيَ آنْتٌة😍🥰"
    }

    # البحث عن الرسالة في القائمة وإرسال الرد المناسب
    response = messages_and_responses.get(text, None)
    if response:
        #bot.reply_to(message, response)
        print("message_random")
        bot.send_message(message.chat.id, response)


@bot.message_handler(commands=['start'])
def start_animation(message):
    chat_id = message.chat.id
    animation_speed = 0.7
    animate_emojis(chat_id, animation_speed)

@bot.message_handler(commands=['stop'])
def stop_animation(message):
    global chat_id
    chat_id = None
if __name__ == "__main__":
    main()
bot.polling()
