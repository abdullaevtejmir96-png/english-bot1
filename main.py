import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Poll

# ⚠️ ВСТАВЬ СЮДА СВОЙ ТОКЕН ИЗ BOTFATHER
API_TOKEN = '8957320709:AAFfT_ATxTfom6EVuMW9con9Yvm-1FqwwtM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Хранилище данных курса (Уровни B1+ / B2)
COURSE_DATA = {
    1: {
        "title": "Unit 1: Noun Suffixes & State Verbs",
        "grammar": (
            "📚 **UNIT 1: Grammar & Suffixes**\n\n"
            "🟢 **Noun Suffixes (Суффиксы существительных):**\n"
            "• `-ment`: manage (управлять) ➡️ manage*ment* (управление)\n"
            "• `-tion`: organize (организовать) ➡️ organiza*tion* (организация)\n"
            "• `-ness`: happy (счастливый) ➡️ happi*ness* (счастье)\n\n"
            "🔵 **State Verbs (Глаголы состояния):**\n"
            "Глаголы чувств и мыслей (know, believe, understand, love) не употребляются в Continuous.\n"
            "✔️ *I understand you.* (НЕ I am understanding you).\n\n"
            "💡 *B2 Сдвиг:* I *think* it's bad (мнение - Simple) vs I *am thinking* about it (процесс - Continuous)."
        ),
        "use_of_english": (
            "✍️ **UNIT 1: Use of English & Writing**\n\n"
            "**Word Formation Task:**\n"
            "В экзаменах B2 часто нужно изменить слово. Попробуй перевести в уме:\n"
            "1. The (GOVERN) _________ decided to change the law. (Ответ: government)\n"
            "2. She looked at him in (AMAZE) _________. (Ответ: amazement)\n\n"
            "📝 **Writing Tip (Essay):**\n"
            "Для выражения мнения используй: *From my perspective*, *It is widely believed that...*"
        ),
        "skills": (
            "📖 **UNIT 1: Reading & Listening**\n\n"
            "🎵 **Listening Practice:**\n"
            "Послушай любое интервью на BBC Learning English и найди глаголы состояния.\n\n"
            "📰 **Reading Text (B2):**\n"
            "*«The digital age has revolutionized communication. However, tech management remains a challenge for the older generation...»*\n"
            "❓ *Question:* What is a challenge for older people? (Tech management)."
        ),
        "vocabulary": (
            "🧠 **UNIT 1: Vocabulary & Speaking**\n\n"
            "🔥 **Phrasal Verbs (Глаголы движения/действия):**\n"
            "• *Bring up* — воспитывать детей / поднимать тему.\n"
            "• *Call off* — отменять (встречу, концерт).\n\n"
            "🗣️ **Speaking Topic:**\n"
            "Tell about a time you had to *call off* an important meeting. Use B2 words!"
        ),
        "homework": (
            "🏠 **UNIT 1: Homework**\n\n"
            "1. Раскрой скобки: *Right now I (think) ________ about moving to another country.*\n"
            "2. Образуй существительное: *Dark (темный) ➡️ _________.*\n"
            "3. Напиши 5 предложений про свое хобби, используя вводные слова: *In addition, stable, focus on*."
        ),
        "quiz_question": "Which sentence is CORRECT?",
        "quiz_options": ["I am knowing him well.", "I know him well.", "I have been knowing him."],
        "quiz_correct": 1,
        "quiz_expl": "'Know' — глагол состояния, Continuous использовать нельзя."
    },
    2: {
        "title": "Unit 2: Narrative Tenses & Adjective Suffixes",
        "grammar": (
            "📚 **UNIT 2: Grammar & Suffixes**\n\n"
            "🟢 **Adjective Suffixes (Суффиксы прилагательных):**\n"
            "• `-ive`: create ➡️ creat*ive* (творческий)\n"
            "• `-able/-ible`: rely ➡️ reli*able* (надежный), sense ➡️ sens*ible* (разумный)\n\n"
            "🔵 **Narrative Tenses (Времена для историй):**\n"
            "Когда рассказываем о прошлом, мы сочетаем Past Simple, Past Continuous и Past Perfect:\n"
            "• *Past Simple* (последовательные действия): He stood up and left.\n"
            "• *Past Continuous* (фоновое действие): It was raining heavily...\n"
            "• *Past Perfect* (действие случилось ДО другого действия): When I arrived, the train *had already left*."
        ),
        "use_of_english": (
            "✍️ **UNIT 2: Use of English & Writing**\n\n"
            "**Key Word Transformations (B2 Exam style):**\n"
            "Перепиши предложение, не меняя смысл:\n"
            "«James arrived after the movie started.» ➡️ Use **ALREADY**\n"
            "Answer: *When James arrived, the movie had ALREADY started.*"
        ),
        "skills": (
            "📖 **UNIT 2: Reading & Listening**\n\n"
            "📰 **Reading B2:**\n"
            "*«By the time the rescue team arrived, the hikers had built a temporary shelter. They were shivering despite the fire...»*\n"
            "❓ *Question:* What had the hikers done before help arrived? (Built a shelter)."
        ),
        "vocabulary": (
            "🧠 **UNIT 2: Vocabulary & Speaking**\n\n"
            "🔥 **B2 Idioms (Идиомы):**\n"
            "• *See eye to eye* — соглашаться, иметь одинаковые взгляды.\n"
            "• *Once in a blue moon* — очень редко.\n\n"
            "🗣️ **Speaking:**\n"
            "Do you and your best friend *see eye to eye* on everything? Speak for 1 minute."
        ),
        "homework": (
            "🏠 **UNIT 2: Homework**\n\n"
            "1. Поставь глагол в Past Perfect: *By 10 PM yesterday, I (finish) _________ my work.*\n"
            "2. Сделай прилагательное от глагога *attract* ➡️ _________.\n"
            "3. Составь историю из 4 предложений, используя Past Simple, Continuous и Perfect одновременно."
        ),
        "quiz_question": "When I woke up, I realized that someone ___ my bike.",
        "quiz_options": ["stole", "was stealing", "had stolen"],
        "quiz_correct": 2,
        "quiz_expl": "Велосипед украли ДО того, как я проснулся, поэтому нужен Past Perfect (had stolen)."
    },
    3: {
        "title": "Unit 3: Passive Voice & Verb Suffixes",
        "grammar": (
            "📚 **UNIT 3: Grammar & Suffixes**\n\n"
            "🟢 **Verb Suffixes (Суффиксы глаголов):**\n"
            "• `-ify`: clear ➡️ clar*ify* (прояснить), pure ➡️ pur*ify* (очистить)\n"
            "• `-ize / -ise`: memory ➡️ memor*ize* (запоминать)\n\n"
            "🔵 **Passive Voice (Пассивный залог):**\n"
            "Используем, когда действие важнее того, кто его совершил. Формула: **BE + V3**\n"
            "• Present Simple Passive: *The house is cleaned every day.*\n"
            "• Past Simple Passive: *The letter was written yesterday.*\n"
            "• Present Perfect Passive: *The rules have been changed.*"
        ),
        "use_of_english": (
            "✍️ **UNIT 3: Use of English & Writing**\n\n"
            "**Sentence Transformation:**\n"
            "«They are building a new school near my house.» ➡️ Измени в пассив:\n"
            "Answer: *A new school is being built near my house.* (Present Continuous Passive)"
        ),
        "skills": (
            "📖 **UNIT 3: Reading & Listening**\n\n"
            "📰 **Reading (B2 Passive):**\n"
            "*«A unique historical artifact has been discovered in Egypt. It is currently being examined by scientists...»*\n"
            "❓ *Question:* Is the artifact fully studied? (No, it is still being examined)."
        ),
        "vocabulary": (
            "🧠 **UNIT 3: Vocabulary & Speaking**\n\n"
            "🔥 **Collocations (Устойчивые выражения):**\n"
            "• *Make an effort* (приложить усилие)\n"
            "• *Take advantage of* (воспользоваться преимуществом / использовать в своих целях)\n\n"
            "🗣️ **Speaking:**\n"
            "How can you *take advantage of* learning English with this bot?"
        ),
        "homework": (
            "🏠 **UNIT 3: Homework**\n\n"
            "1. Переделай в Пассив: *They have postponed the exam.* ➡️ The exam _________.\n"
            "2. Сделай глагол от существительного *Apology* (Извинение) ➡️ _________.\n"
            "3. Переведи: *Этот текст сейчас переводят.*"
        ),
        "quiz_question": "Active: 'Shakespeare wrote Hamlet.' -> Passive: 'Hamlet ___ by Shakespeare.'",
        "quiz_options": ["is written", "was written", "has been written"],
        "quiz_correct": 1,
        "quiz_expl": "Так как оригинал в Past Simple (wrote), в пассиве будет 'was written'."
    }
}

# Пользовательские сессии (чтобы бот помнил, на каком юните сейчас ученик)
# В реальной жизни нужна БД, но для старта храним в оперативной памяти бота
user_units = {}

def get_user_unit(user_id):
    return user_units.get(user_id, 1) # По умолчанию 1 юнит

# Главное меню (кнопки внизу экрана)
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📖 Изучать Теорию (Grammar & Suffixes)")],
        [KeyboardButton(text="🧠 Use of English & Vocabulary"), KeyboardButton(text="🎧 Reading & Listening")],
        [KeyboardButton(text="📝 Пройти Тест урока"), KeyboardButton(text="🏠 Домашнее Задание")],
        [KeyboardButton(text="🔄 Сменить / Выбрать Урок")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    user_units[message.from_user.id] = 1
    await message.answer(
        f"Hi {message.from_user.first_name}! 👋\n"
        "Добро пожаловать в полноценный курс английского языка уровня B1+/B2.\n\n"
        "Здесь тебя ждут правила, разборы суффиксов, Use of English, тексты и тесты к каждому уроку.\n"
        "Сейчас ты находишься на **Unit 1**.",
        reply_markup=main_menu
    )

# Выбор юнита вручную
@dp.message(lambda message: message.text == "🔄 Сменить / Выбрать Урок")
async def choose_unit(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Unit 1: Noun Suffixes & States", callback_data="set_unit_1")],
        [InlineKeyboardButton(text="Unit 2: Narrative & Adjectives", callback_data="set_unit_2")],
        [InlineKeyboardButton(text="Unit 3: Passive Voice & Verbs", callback_data="set_unit_3")]
    ])
    await message.answer("Выбери интересующий тебя урок из списка ниже:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data.startswith('set_unit_'))
async def process_unit_change(callback_query: types.CallbackQuery):
    unit_num = int(callback_query.data.split('_')[-1])
    user_units[callback_query.from_user.id] = unit_num
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        f"✅ Успешно переключено на **{COURSE_DATA[unit_num]['title']}**!\n"
        "Нажимай на кнопки меню, чтобы изучать материалы этого урока.",
        reply_markup=main_menu,
        parse_mode="Markdown"
    )

# Кнопка: Теория (Грамматика и суффиксы)
@dp.message(lambda message: message.text == "📖 Изучать Теорию (Grammar & Suffixes)")
async def show_grammar(message: types.Message):
    unit = get_user_unit(message.from_user.id)
    text = COURSE_DATA[unit]["grammar"]
    
    # Кнопка для быстрого перехода к следующему шагу урока
    next_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти к Use of English ➡️", callback_data="go_use_of_english")]
    ])
    await message.answer(text, parse_mode="Markdown", reply_markup=next_btn)

# Кнопка: Use of English & Vocabulary
@dp.message(lambda message: message.text == "🧠 Use of English & Vocabulary")
async def show_vocab(message: types.Message):
    unit = get_user_unit(message.from_user.id)
    text = f"{COURSE_DATA[unit]['use_of_english']}\n\n---\n\n{COURSE_DATA[unit]['vocabulary']}"
    
    next_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Перейти к Reading & Listening ➡️", callback_data="go_skills")]
    ])
    await message.answer(text, parse_mode="Markdown", reply_markup=next_btn)

# Кнопка: Reading & Listening
@dp.message(lambda message: message.text == "🎧 Reading & Listening")
async def show_skills(message: types.Message):
    unit = get_user_unit(message.from_user.id)
    text = COURSE_DATA[unit]["skills"]
    
    next_btn = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎯 Начать тест урока ➡️", callback_data="go_test")]
    ])
    await message.answer(text, parse_mode="Markdown", reply_markup=next_btn)

# Кнопка: Пройти тест
@dp.message(lambda message: message.text == "📝 Пройти Тест урока")
async def show_test(message: types.Message):
    unit = get_user_unit(message.from_user.id)
    data = COURSE_DATA[unit]
    
    await message.answer(f"📊 Тест по материалам **Unit {unit}**:")
    await bot.send_poll(
        chat_id=message.chat.id,
        question=data["quiz_question"],
        options=data["quiz_options"],
        type="quiz",
        correct_option_id=data["quiz_correct"],
        explanation=data["quiz_expl"],
        is_anonymous=False
    )

# Кнопка: Домашнее Задание
@dp.message(lambda message: message.text == "🏠 Домашнее Задание")
async def show_homework(message: types.Message):
    unit = get_user_unit(message.from_user.id)
    text = COURSE_DATA[unit]["homework"]
    
    # Кнопка переключения на следующий юнит
    if unit < 3:
        next_unit_btn = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"Открыть Unit {unit+1} 🔓", callback_data=f"set_unit_{unit+1}")]
        ])
    else:
        next_unit_btn = None
        
    await message.answer(text, parse_mode="Markdown", reply_markup=next_unit_btn)

# Обработка переходов по встроенным кнопкам (Inlines)
@dp.callback_query(lambda c: c.data.startswith('go_'))
async def process_navigation(callback_query: types.CallbackQuery):
    action = callback_query.data
    user_id = callback_query.from_user.id
    await bot.answer_callback_query(callback_query.id)
    
    if action == "go_use_of_english":
        await show_vocab(callback_query.message)
    elif action == "go_skills":
        await show_skills(callback_query.message)
    elif action == "go_test":
        await show_test(callback_query.message)

async def main():
    print("Курс успешно запущен на Railway!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
