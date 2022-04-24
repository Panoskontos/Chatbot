from chatterbot import ChatBot
import time
from chatterbot.trainers import ListTrainer

# time error
time.clock = time.time

chatbot = ChatBot("Panagiotis")


trainer = ListTrainer(chatbot)

trainer.train([
    "Geia",
    "Pos eisai re seira",
    "Mia xara esu",
    "kai egw kala",
    "fantastic",
    "spectacular",
])


trainer.train([
    "i want to learn more",
    "You can learn more about as in www.....etc",
])


print('Type something to begin...')

# first test
# response = chatbot.get_response("Hey")
# print(response)

# links
# https://chatterbot.readthedocs.io/en/stable/examples.html

# begin testing
while True:
    try:
        user_input = input()

        bot_response = chatbot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
