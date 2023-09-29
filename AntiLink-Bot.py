# ************************************
# **      --- Amir-AJ-PRO ---       **
# **          AntiLink-Bot          **
# **     Python-Telegram-Bot V:20   **
# ************************************

"""This robot reliably deletes the links sent by the users of a group (must be in the admin group)"""

from telegram import Update , MessageEntity
from telegram.ext import ContextTypes , ApplicationBuilder , CommandHandler , MessageHandler , filters

# Start function
async def start (update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text="Hi...\nWelcome to Anti Link Bot❤️" , chat_id= update.message.chat.id )

# Delete messages with links ... 
async def Antilink (update:Update , context:ContextTypes.DEFAULT_TYPE):    
    links = [MessageEntity.URL]
    if update.message.chat.type != 'private':
        if update.message.parse_entities(types=links) or update.message.parse_caption_entities(types=links):
            await context.bot.delete_message(chat_id=update.message.chat.id , message_id=update.message.message_id)


if __name__ == "__main__" :
    application = ApplicationBuilder().token("TOKEN").build()

    start_handler = CommandHandler('start' , start)
    application.add_handler(start_handler)

    Antilink_Handler = MessageHandler(filters.ALL , Antilink)
    application.add_handler(Antilink_Handler)

    application.run_polling()