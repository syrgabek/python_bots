from aiogram import types, Dispatcher
# from bot_instance import bot

async def echo_and_ban(message: types.Message):
    ban_words = ['java', 'bitch', 'slut', 'python is bad']
    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Bot-Admin deleted bad words")
    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")
    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban, content_types=['text'])