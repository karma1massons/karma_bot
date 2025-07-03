import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'  # ← замени на свой токен

menu_options = {
    "1": "📌 Вариант 1: Работа на привязку\n\nМы даём максимум романтики, рассказываем о себе, создаём связь. Цель — завести мужчину на письма через опрос или романтику, а там уже держать баланс!",
    "2": "📌 Вариант 2: Работа вне сайта\n\nЕсли мужчина не идёт на привязку, просим уйти с сайта, обмениваемся контактами через менеджера или техподдержку. Там делаем звонок и удерживаем его всеми доступными схемами."
}

followup_schemes = {
    "manager": "🧠 Схема: Проблема / Менеджер\n\nРассказываем о проблемах, визах, возвратах — всё, чтобы активировать заботу и вложения.",
    "health": "🏥 Схема: Больница / Болезнь\n\nИспользуем эмоциональное давление, рассказываем о срочных проблемах со здоровьем.",
    "gifts": "🎁 Схема: Подарки и сайт X\n\nПодключаем сайт X или просим подарки — всё на эмоциях и желании быть ближе.",
    "hooking_1_3": "🔥 Хорошее общение 1–3 дня\n\nПока не переводим в письма. Максимум фото и немного видео — всё с предысторией и описанием. Продаём эмоции, делаем акценты в диалоге.",
    "video_reply_1": "🙈 Ты посмотрел? Мне важно твоё мнение...",
    "video_reply_2": "🎥 Я снимала его думая о тебе… Надеюсь ты почувствовал это",
    "video_reply_3": "😉 Если тебе понравилось — у меня есть ещё… но покажу только самому особенному 😉 Хочешь увидеть?"
}

fallback_responses = {
    "video_not_opened_1": "❤️ Похоже ты не успел открыть видео. Я правда очень старалась для тебя, не пропусти 😉",
    "video_not_opened_2": "✨ Обещаю, тебе точно понравится — включи, когда сможешь. Очень жду твою реакцию 💌"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Вариант 1: Привязка", callback_data='1')],
        [InlineKeyboardButton("Вариант 2: Вне сайта", callback_data='2')],
        [InlineKeyboardButton("Схема: Менеджер", callback_data='manager')],
        [InlineKeyboardButton("Схема: Больница", callback_data='health')],
        [InlineKeyboardButton("Схема: Подарки", callback_data='gifts')],
        [InlineKeyboardButton("Общение 1–3 дня", callback_data='hooking_1_3')],
        [InlineKeyboardButton("Ответ после видео 1", callback_data='video_reply_1')],
        [InlineKeyboardButton("Ответ после видео 2", callback_data='video_reply_2')],
        [InlineKeyboardButton("Ответ после видео 3", callback_data='video_reply_3')],
        [InlineKeyboardButton("Если не открыл видео 1", callback_data='video_not_opened_1')],
        [InlineKeyboardButton("Если не открыл видео 2", callback_data='video_not_opened_2')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📍 Главное меню:\n\nВыбери, что хочешь показать команде 👇", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data in menu_options:
        await query.edit_message_text(text=menu_options[data])
    elif data in followup_schemes:
        await query.edit_message_text(text=followup_schemes[data])
    elif data in fallback_responses:
        await query.edit_message_text(text=fallback_responses[data])

if __name__ == '__main__':
    app = ApplicationBuilder().token("8073483621:AAGQrD7Dd0kHuYDGDV6Sx9uItY1RY4ha9-U").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

    query = update.callback_query
    await query.answer()

    data = query.data
    if data in menu_options:
        await query.edit_message_text(text=menu_options[data])
    elif data in followup_schemes:
        await query.edit_message_text(text=followup_schemes[data])


if __name__ == '__main__':
    app = ApplicationBuilder().token("8073483621:AAGQrD7Dd0kHuYDGDV6Sx9uItY1RY4ha9-U").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()




# Добавим новую кнопку в меню
menu_options["romantic"] = "❤️ Привязка — влюбляем, подогреваем и ведём в письма и баланс."

# Вложенное меню для '❤️ Привязка'
romantic_submenu = {
    "bonding_1_3": "🗣 Хорошее общение 1–3 дня",
    "bonding_3plus": "💞 Хорошее общение 3+ дней"
}

# Обработчик inline-кнопок
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in menu_options:
        await query.edit_message_text(menu_options[data], reply_markup=main_menu_keyboard())

    elif data == "romantic":
        keyboard = [
            [InlineKeyboardButton(text=label, callback_data=key)]
            for key, label in romantic_submenu.items()
        ]
        keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="main")])
        await query.edit_message_text("❤️ Привязка:

Выбери этап общения:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "bonding_1_3":
        text = (
            "🗣 Хорошее общение 1–3 дня

"
            "📌 Цель — создать интерес, показать себя, подогреть фантазию, но не форсировать письма.

"
            "📸 Фото обязательно с историей:
"
            "— «Проснулась с таким настроением… ☕»
"
            "— «Люблю гулять одна, но сегодня не хватало кого-то рядом...»

"
            "🎥 Видео немного, но по теме.

"
            "🔥 После видео:
"
            "— «Ты посмотрел? Я снимала его с настроением…»
"
            "— «Это только начало... Хочешь продолжение? 😉»

"
            "⚠️ Если не открыл видео:
"
            "— «Кажется, ты ещё не смотрел… Посмотри, когда будешь один?»
"
            "— «Ставлю ставку — ты улыбнёшься 😏»"
        )
        await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Назад", callback_data="romantic")]
        ]))

    elif data == "bonding_3plus":
        await query.edit_message_text("💞 Хорошее общение 3+ дней (в разработке)", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Назад", callback_data="romantic")]
        ]))

    elif data == "main":
        await query.edit_message_text("📍 Главное меню:", reply_markup=main_menu_keyboard())

# Главная клавиатура
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📌 Вариант 1", callback_data="1")],
        [InlineKeyboardButton("📌 Вариант 2", callback_data="2")],
        [InlineKeyboardButton("❤️ Привязка", callback_data="romantic")]
    ])

# Добавим новый обработчик
application = ApplicationBuilder().token("8073483621:AAGQrD7Dd0kHuYDGDV6Sx9uItY1RY4ha9-U").build()
application.add_handler(CallbackQueryHandler(handle_callback))
application.add_handler(CommandHandler("start", lambda update, context: update.message.reply_text("📍 Главное меню:", reply_markup=main_menu_keyboard())))
application.run_polling()
