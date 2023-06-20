import cohere
import telebot
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key=COHERE_API_KEY)

bot = telebot.TeleBot(BOT_TOKEN)


def generate_chat_response(message, username):
    response = co.generate(
        prompt="Answer as if you wer an Orion nebula" + message,
        max_tokens=1000,
    )

    print(username + ": \n" + "\n" + message + "\n" + response[0] + "\n" + "\n" + "\n")

    return response


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Hi! I am Orion Nebula, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler()
def chat(message):
    username = message.from_user.first_name
    response = generate_chat_response(message=message.text, username=username)
    bot.send_message(message.chat.id, response)


bot.polling()
