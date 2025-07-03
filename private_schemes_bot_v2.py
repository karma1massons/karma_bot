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
    "gifts": "🎁 Схема: Подарки и сайт X\n\nПодключаем сайт X или просим подарки — всё на эмоциях и желании быть ближе."
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Вариант 1: Привязка", callback_data='1')],
        [InlineKeyboardButton("Вариант 2: Вне сайта", callback_data='2')],
        [InlineKeyboardButton("Схема: Менеджер", callback_data='manager')],
        [InlineKeyboardButton("Схема: Больница", callback_data='health')],
        [InlineKeyboardButton("Схема: Подарки", callback_data='gifts')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери, что хочешь показать команде 👇", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data in menu_options:
        await query.edit_message_text(text=menu_options[data])
    elif data in followup_schemes:
        await query.edit_message_text(text=followup_schemes[data])


if __name__ == '__main__':
    app = ApplicationBuilder().token("8073483621:AAEN5hE2U0_Za2Rbfs68Bp6prWMDekzxIpA").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

