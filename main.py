import telebot
import openai
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

points = [
    "Orion Nebula",
    "planet Mercury",
    "planet Venus",
    "planet Earth",
    "planet Mars",
    "planet Jupiter",
    "planet Saturn",
    "planet Uranus",
    "planet Neptune",
]

user_space_objects = {}
prev_response = ""


def generate_chat_response(message, username, space_object, prev_response):
    print(space_object)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a " + space_object + " that answers any questions.",
            },
            {
                "role": "user",
                "content": "Answer as if you were "
                + space_object
                + "; In a context of a message: "
                + prev_response
                + "; "
                + message,
            },
        ],
        temperature=1,
    )

    print()

    return completion.choices[0].message["content"]


@bot.message_handler(commands=["start"])
def start(message):
    global prev_response
    prev_response = ""
    bot.send_message(
        message.chat.id,
        "Hi! I am Nebula AI bot, chose any space object you want to speak with and feel free to ask any questions! \nI am here to help you get some knowledge in astronomy!",
    )
    bot.send_message(
        message.chat.id,
        "To start a conversation with a specific space object, type /<space_object>. \n\nList of all the commands: \nOrion Nebula: /orion\nMercury: /mercury\nVenus: /venus\nEarth: /earth\nMars: /mars\nJupiter: /jupiter\nSaturn: /saturn\nUranus: /uranus\nNeptune: /neptune",
    )


@bot.message_handler(commands=["orion"])
def orion(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[0]
    bot.send_message(
        message.chat.id,
        "Hi! I am Orion Nebula, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["mercury"])
def mercury(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[1]
    bot.send_message(
        message.chat.id,
        "Hi! I am Mercury, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["venus"])
def venus(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[2]
    bot.send_message(
        message.chat.id,
        "Hi! I am Venus, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["earth"])
def mars(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[3]
    bot.send_message(
        message.chat.id,
        "Hi! I am Earth, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["mars"])
def mars(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[4]
    bot.send_message(
        message.chat.id,
        "Hi! I am Mars, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["jupiter"])
def jupiter(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[5]
    bot.send_message(
        message.chat.id,
        "Hi! I am Jupiter, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["saturn"])
def saturn(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[6]
    bot.send_message(
        message.chat.id,
        "Hi! I am"
        + user_space_objects[message.chat.id]
        + ", ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["uranus"])
def uranus(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[7]
    bot.send_message(
        message.chat.id,
        "Hi! I am Uranus, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler(commands=["neptune"])
def neptune(message):
    global prev_response
    prev_response = ""
    user_space_objects[message.chat.id] = points[8]
    bot.send_message(
        message.chat.id,
        "Hi! I am Neptune, ask me anything! I am here to help you out with your astronomical questions!",
    )


@bot.message_handler()
def chat(message):
    global prev_response
    username = message.from_user.first_name
    if message.chat.id in user_space_objects:
        current_space_object = user_space_objects[message.chat.id]
        response = generate_chat_response(
            message=message.text,
            username=username,
            space_object=current_space_object,
            prev_response=prev_response,
        )
        prev_response = response
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(
            message.chat.id,
            "Please select a space object using the appropriate command. Enter /start for the further information.",
        )


bot.polling()
