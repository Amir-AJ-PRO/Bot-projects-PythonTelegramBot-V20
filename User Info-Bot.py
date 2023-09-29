# ************************************
# **      --- Amir-AJ-PRO ---       **
# **         User-Info-Bot          **
# **     Python-Telegram-Bot V:20   **
# ************************************

from telegram import Update
from telegram.ext import ContextTypes , ApplicationBuilder , CommandHandler


# Sending Welcome message (optional) , UserInformation
async def start (update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text="Hi...\nWelcome to InfoBot❤️" , chat_id= update.message.chat.id )   
    await context.bot.send_message(text=f"@{update.message.chat.username}\nid : {update.message.chat.id}\nfirst : {update.message.chat.first_name}\nlang : {update.message.from_user.language_code}" , chat_id=update.message.chat.id)


if __name__ == "__main__" :
    application = ApplicationBuilder().token("TOKEN").build()

    # Handling start command 
    start_handler = CommandHandler('start' , start) #(command --> function)
    application.add_handler(start_handler)

    application.run_polling()