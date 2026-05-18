import asyncio
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ⚠️ ВСТАВЬ СЮДА СВОЙ ТОКЕН ОТ BOTFATHER МЕЖДУ КАВЫЧКАМИ
API_TOKEN = 8957320709:'AAFfT_ATxTfom6EVuMW9con9Yvm-1FqwwtM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Grammar & Suffixes"), KeyboardButton(text="📖 Reading & Listening")],
        [KeyboardButton(text="✍️ Writing & Use of English"), KeyboardButton(text="🗣️ Speaking Part")],
        [KeyboardButton(text="🧠 Vocabulary"), KeyboardButton(text="📝 Homework & Tests")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        f"Hi {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в бот для прокачки английского языка (B1+/B2).\n"
        "Выбери раздел в меню ниже!",
        reply_markup=main_menu
    )

@dp.message()
async def handle_menu(message: types.Message):
    if message.text == "📚 Grammar & Suffixes":
        await message.answer("Здесь будут правила (Conditional sentences, Passive Voice) и суффиксы (-ment, -tion, -ity).")
    elif message.text == "📝 Homework & Tests":
        await message.answer("Тут тебя будут ждать тесты с вариантами ответов.")
    else:
        await message.answer(f"Ты выбрал раздел: {message.text}. Скоро мы его наполним!")

async def main():
    print("Бот успешно запущен на PythonAnywhere!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем бота
    asyncio.run(main())
