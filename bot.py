from aiogram import Bot, Dispatcher, types, executor
import os

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Tug‘ilgan kun tabriklariga buyurtma berish uchun tabrik matnini yozib yuboring.")

@dp.message_handler()
async def handle_order(message: types.Message):
    order_text = f"🆕 Yangi buyurtma:\n\n{message.text}\n\n👤 @{message.from_user.username} ({message.from_user.full_name})"
    await bot.send_message(CHANNEL_ID, order_text)
    await message.reply("✅ Buyurtma qabul qilindi. Tez orada administratorlar aloqaga chiqadi.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
