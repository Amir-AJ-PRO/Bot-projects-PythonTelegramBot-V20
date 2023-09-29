# ************************************
# **      --- Amir-AJ-PRO ---       **
# **            ChatBot             **
# **     Python-Telegram-Bot V:20   **
# ************************************


"""This bot can be an intermediary between the admin or admins of a channel and the user as a bridge of communication between them"""

from telegram import Update , ReplyKeyboardMarkup , ReplyKeyboardRemove , InlineKeyboardButton , InlineKeyboardMarkup
from telegram.ext import ContextTypes , ApplicationBuilder , CommandHandler , MessageHandler , filters , ConversationHandler , CallbackQueryHandler

se = 0 # For ConversaitionHandler
re = 0 # A trick to communicate between Quey Handled and Message handled functions
B = [] # Using the list for blocked users (it is better to use the database) 


async def start (update:Update , context:ContextTypes.DEFAULT_TYPE):
    global key_2
    key = [['Contact us📞']]
    key_2 = ReplyKeyboardMarkup(key , resize_keyboard=True)
    if update.message.chat.id != 1111111111 : #(1111111111) is admin chat-id
        await context.bot.send_message(text=f'HI {update.message.from_user.first_name}👋🏻❤️\n Welcome to your bot' , chat_id=update.message.chat.id)
        await context.bot.send_message(text='Click for contact ... :' , chat_id=update.message.chat.id , reply_markup=key_2)
    else : 
        await context.bot.send_message(text=f'HI {update.message.from_user.first_name}👋🏻❤️\n Welcome to your bot' , chat_id=update.message.chat.id)
        await context.bot.send_message(text='You are Admin ... ✅' , chat_id=update.message.chat.id)


# Conversation entry point
async def text (update:Update , context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(text='💬Send your message : ' , chat_id= update.message.chat.id , reply_markup=ReplyKeyboardRemove())
        
    return se

#Conversation status 1 (The only status)
async def send_message (update:Update , context:ContextTypes.DEFAULT_TYPE):
    global key_2 , user

    button = [[InlineKeyboardButton(text='Reply 📤' , callback_data='Reply') , InlineKeyboardButton(text='Block ❌' , callback_data='Block')] , [InlineKeyboardButton(text='Unblock 🔄', callback_data='Unblock')]]
    button_2 = InlineKeyboardMarkup(button)

    if str(update.message.chat.id) not in B :
        await context.bot.copy_message(chat_id=1111111111 , from_chat_id=update.message.chat.id , message_id=update.message.message_id)
        await context.bot.send_message(chat_id=1111111111 , text=f'💬\nUserName : @{update.message.from_user.username}\nChatID : {update.message.chat.id}' , reply_markup=button_2)
        await context.bot.send_message(text='Done ✅' , chat_id=update.message.chat.id , reply_markup=key_2)
    else :
        await context.bot.send_message(text='❌ You are blocked ❌' , chat_id=update.message.chat.id)

    return ConversationHandler.END


async def reply (update:Update , context:ContextTypes.DEFAULT_TYPE):
    global re , user

    if re != 0 :
        await context.bot.send_message(text='📩 Admin answer : ' , chat_id=user) 
        await context.bot.copy_message(chat_id= user , from_chat_id=update.message.chat.id , message_id=update.message.message_id)  
        await context.bot.send_message(text='Done ✅' , chat_id=update.message.chat.id) 
        re = 0 


async def Button_click (update:Update , context:ContextTypes.DEFAULT_TYPE):
    global re , user
    query = update.callback_query

    if query.data == 'Reply' :
        re = 1
        query_text = query.message.text
        user = query_text.split('ChatID : ' , 1)[1]
        
        await context.bot.send_message(text=f'You are replying to : {user}🆔' , chat_id= query.message.chat.id)
        
    if query.data == 'Block':
        query_text = query.message.text
        user = query_text.split('ChatID : ' , 1)[1]
        B.append(user)
        await context.bot.send_message(text=f'The target user was blocked by chat ID {user}🅱️' , chat_id= query.message.chat.id)

    if query.data == 'Unblock':
        query_text = query.message.text
        user = query_text.split('ChatID : ' , 1)[1]
        if user in B :
            B.remove(user)
            await context.bot.send_message(text=f'The target user was unblocked by chat ID {user}🔄' , chat_id= query.message.chat.id)
        else :
            await context.bot.send_message(text="This user has not been blocked.❎" , chat_id= query.message.chat.id)

    

if __name__ == '__main__':
    application = ApplicationBuilder().token("TOKEN").build()

    start_handler = CommandHandler('start' , start)
    application.add_handler(start_handler)


    se_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex('^(Contact us📞)$') , text)] ,
        states={
            se : [MessageHandler(filters.ALL , send_message)]
        },
        fallbacks=[]
    )
    application.add_handler(se_handler)

    button_handler = CallbackQueryHandler(Button_click)
    application.add_handler(button_handler)

    re_handler = MessageHandler(filters.ALL , reply)
    application.add_handler(re_handler)

    application.run_polling()