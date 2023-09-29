# ************************************
# **      --- Amir-AJ-PRO ---       **
# **            Echo-Bot            **
# **     Python-Telegram-Bot V:20   **
# ************************************

""" This bot was actually written for educational purposes,
but it's not bad for beginners to take a look at this project """

from telegram import Update
from telegram.ext import ContextTypes , ApplicationBuilder , CommandHandler , MessageHandler , filters

# Start function
async def start (update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text="Hi...\nWelcome to EchoBot❤️" , chat_id= update.message.chat.id )

# Echo text ...
async def echo_message(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text=update.message.text , chat_id=update.message.from_user.id)

# Echo-Forward photo ...
async def echo_photo(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.forward_message(chat_id=update.message.chat.id , from_chat_id=update.message.chat.id , message_id=update.message.message_id)

# Echo all ...
async def echo(update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.copy_message(chat_id=update.message.chat.id , from_chat_id=update.message.chat.id , message_id=update.message.message_id)


if __name__ == "__main__" :
    application = ApplicationBuilder().token("TOKEN").build()

    start_handler = CommandHandler('start' , start)
    application.add_handler(start_handler)

    """These commented codes handled two functions, each of which echoed the photo or text separately, 
    but with the last method and the use of copy_message, anything can be echoed."""
    
    #echo_message_handler = MessageHandler(filters.TEXT , echo_message)
    #application.add_handler(echo_message_handler)

    #echo_photo_handler = MessageHandler(filters.PHOTO , echo_photo)
    #application.add_handler(echo_photo_handler)

    echo_handler = MessageHandler(filters.ALL , echo)
    application.add_handler(echo_handler)

    application.run_polling()