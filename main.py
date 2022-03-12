from aiogram import executor
from bot_instance import dp
from handers import client, callback, extra

client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
