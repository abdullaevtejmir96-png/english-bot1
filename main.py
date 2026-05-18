import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Poll

# ⚠️ ВСТАВЬ СЮДА СВОЙ ТОКЕН ИЗ BOTFATHER
API_TOKEN = '8957320709:AAFfT_ATxTfom6EVuMW9con9Yvm-1FqwwtM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Grammar & Suffixes"), KeyboardButton(text="📝 Take a Test")],
        [KeyboardButton(text="📖 Reading & Listening"), KeyboardButton(text="🗣️ Speaking & Writing")],
        [KeyboardButton(text="🧠 Vocabulary"), KeyboardButton(text="🏠 Homework")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        f"Welcome back, {message.from_user.first_name}! 👋\n"
        "Твой бот-преподаватель готов к работе. Выбирай раздел в меню, чтобы начать учиться на уровень B1+/B2!",
        reply_markup=main_menu
    )

# Раздел: Грамматика и Суффиксы (Объяснение правил)
@dp.message(lambda message: message.text == "📚 Grammar & Suffixes")
async def show_grammar(message: types.Message):
    grammar_text = (
        "📖 **UNIT 1: Noun Suffixes & State Verbs (B1+/B2)**\n\n"
        "🟢 **Часть 1: Словообразование (Suffixes)**\n"
        "На уровне B2 важно уметь переделывать глаголы и прилагательные в существительные:\n"
        "• `-ment`: govern (управлять) ➡️ govern*ment* (правительство)\n"
        "• `-tion / -sion`: inspire (вдохновлять) ➡️ inspira*tion* (вдохновение)\n"
        "• `-ness` (от прилагательных): Kind (добрый) ➡️ kind*ness* (доброта)\n"
        "• `-ity`: Able (способный) ➡️ abil*ity* (способность)\n\n"
        "🔵 **Часть 2: Глаголы состояния (State Verbs)**\n"
        "Глаголы, которые описывают мысли, чувства или состояние (know, remember, love, belong, understand), **НЕ используются в Continuous**, даже если действие происходит прямо сейчас!\n"
        "❌ *I am knowing the answer.* (Неверно)\n"
        "✔️ *I know the answer.* (Верно)\n\n"
        "💡 *Исключение уровня B2:* Некоторые глаголы меняют значение. \n"
        "• I *think* it's a good idea (Я считаю/это мое мнение — State).\n"
        "• Shh! I *am thinking* about my exam (Я размышляю/процесс в голове — Dynamic)."
    )
    await message.answer(grammar_text, parse_mode="Markdown")

# Раздел: Тесты (Интерактивная викторина)
@dp.message(lambda message: message.text == "📝 Take a Test")
async def send_test(message: types.Message):
    await message.answer("Давай проверим, как ты усвоил правила! Ответь на вопрос ниже 👇")
    
    # Отправляем встроенный тест Telegram (викторину)
    await bot.send_poll(
        chat_id=message.chat.id,
        question="Which sentence is grammatically CORRECT for B2 level?",
        options=[
            "I am remembering our first English lesson.",
            "I remember our first English lesson.",
            "I am remember our first English lesson.",
            "I have been remembering our first lesson."
        ],
        type="quiz",
        correct_option_id=1, # Индекс правильного ответа (считается с 0, то есть второй вариант)
        explanation="Глагол 'remember' — это State Verb (глагол состояния), он не употребляется во временах Continuous.",
        is_anonymous=False
    )

# Раздел: Домашнее задание
@dp.message(lambda message: message.text == "🏠 Homework")
async def show_homework(message: types.Message):
    homework_text = (
        "🏠 **HOMEWORK (Уровень B2)**\n\n"
        "**Задание 1: Раскрой скобки в правильном времени (Present Simple или Continuous):**\n"
        "1. I _________ (think) of buying a new car, what do you think?\n"
        "2. This soup _________ (taste) delicious!\n"
        "3. Look! She _________ (taste) the sauce to see if it needs salt.\n\n"
        "**Задание 2: Образуй существительные от слов:**\n"
        "• Develop ➡️ ...\n"
        "• Happy ➡️ ...\n"
        "• Creative ➡️ ...\n\n"
        "📝 *Запиши свои ответы на листочке или в заметках, а на следующем уроке мы их проверим!*"
    )
    await message.answer(homework_text, parse_mode="Markdown")

# Заглушки для остальных разделов, чтобы бот не молчал
@dp.message()
async def handle_other(message: types.Message):
    if message.text == "📖 Reading & Listening":
        await message.answer("🔊 Здесь будут тексты уровня B2 и аудиофайлы с заданиями на Use of English.")
    elif message.text == "🗣️ Speaking & Writing":
        await message.answer("✍️ Тут будут шаблоны для написания эссе (Essay) и официальных писем, а также темы для Speaking.")
    elif message.text == "🧠 Vocabulary":
        await message.answer("💡 Раздел для изучения продвинутых фразовых глаголов (Phrasal verbs) и идиом уровня B2.")
    else:
        await message.answer("Пожалуйста, используй кнопки меню для навигации.")

async def main():
    print("Бот успешно обновлен на Railway!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
