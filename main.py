from aiogram import Bot, Dispatcher, F
from aiogram.types import Message,FSInputFile
from aiogram.filters import CommandStart
import asyncio
from generator import make_picture
from googletrans import Translator
from asgiref.sync import sync_to_async

bot = Bot("8042462482:AAHZmmj2RD6mTUicdFyMJwoIxf2W2K2DBJY")
dp = Dispatcher()

async def translate_text(text):
    async with Translator() as translator:
        result= await translator.translate(text=text,src="uz",dest="en")
    return result.text

@dp.message(CommandStart())
async def start_handler(message:Message):
    await message.answer(f"Iltimos, bir ajoyib prompt yozing ✍️ ! \nPlease write your prompt here ✍️ !")

@dp.message()
async def text_translator(message:Message):
     prompt=message.text
     await message.answer(f"Rasm tayyorlanmoqda🔄")
     en =  await translate_text(prompt)
     fildname=f"{message.from_user.first_name}.jpg"
     await sync_to_async(make_picture)(en,fildname)

     full_path=f"images/{fildname}"
     await message.answer_photo(photo=FSInputFile(full_path),caption=f"✅ Rasm tayyor")
    
async def main():
 print("bot ishga tushdi")
 await dp.start_polling(bot)

asyncio.run(main())
