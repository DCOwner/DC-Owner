from telegram import *
from telegram.ext import *

bot = Bot("1994050378:AAGB7GdWBB8XNc-UJjydOzkXkfSmj0fp_DI")
#print(bot.get_me())

updater=Updater("1994050378:AAGB7GdWBB8XNc-UJjydOzkXkfSmj0fp_DI"),use_context=True
dispatcher=updater.dispatcher

def test_function(update:update, context:CallbackContext):
    bot.send_message(
        
        chat_id:=update.efective.chat_id,
        text="My Owner ID : @DreamerNo1",
        )

start_value=CommandHandler('motion_detection',test_function)

dispatcher.add_handler(start_value)

updater.startpolling()
