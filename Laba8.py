import os
from dotenv import load_dotenv
import telebot




load_dotenv()
TOKEN = os.getenv('TOKEN')



bot=telebot.TeleBot(TOKEN)

@bot.message_handler()
def start_message(message):

    bot.send_message(message.chat.id,message.text)



def main():
    bot.polling()



if __name__ == '__main__':

    main()
