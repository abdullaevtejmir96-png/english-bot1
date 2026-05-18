import asyncio
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ⚠️ Вставь свой токен прямо между кавычками ниже:
API_TOKEN = '8957320709:AAFfT_ATxTfom6EVuMW9con9Yvm-1FqwwtM'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Создаем главное меню с кнопками
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Grammar & Suffixes"), KeyboardButton(text="📖 Reading & Listening")],
        [KeyboardButton(text="✍️ Writing & Use of English"), KeyboardButton(text="🗣️ Speaking Part")],
        [KeyboardButton(text="🧠 Vocabulary"), KeyboardButton(text="📝 Homework & Tests")]
    ],
    resize_keyboard=True
)

# Обработка команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        f"Hi {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в бот для прокачки английского языка (B1+/B2).\n"
        "Выбери раздел в меню ниже, чтобы начать!",
        reply_markup=main_menu
    )

# Обработка нажатий на кнопки
@dp.message()
async def handle_menu(message: types.Message):
    if message.text == "📚 Grammar & Suffixes":
        await message.answer("Здесь будут правила грамматики (Conditional sentences, Passive Voice) и разбор суффиксов (-ment, -tion, -ity).")
    elif message.text == "📖 Reading & Listening":
        await message.answer("В этом разделе будут тексты уровня B2, аудиоматериалы и задания к ним.")
    elif message.text == "✍️ Writing & Use of English":
        await message.answer("Тут мы будем тренировать написание эссе, писем и задания из Use of English (Phrasal verbs, Idioms).")
    elif message.text == "🗣️ Speaking Part":
        await message.answer("Раздел для практики говорения: темы для обсуждения, карточки и полезные фразы.")
    elif message.text == "🧠 Vocabulary":
        await message.answer("Учим продвинутые слова и словосочетания для уровней B1+/B2.")
    elif message.text == "📝 Homework & Tests":
        await message.answer("Тут тебя ждут тесты для закрепления материала и домашние задания.")
    else:
        await message.answer("Пожалуйста, выбери пункт из меню 👇")

async def main():
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
