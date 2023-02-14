from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(
    "lucy",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
    ],
    )

trainer = ListTrainer(bot)
train = ChatterBotCorpusTrainer(bot)

train.train(
     "chatterbot.corpus.english",
)
while True:
    try:
        bot_input = bot.get_response(input("you: "))
        print(f"bot: {bot_input} ==> {bot_input.confidence}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break