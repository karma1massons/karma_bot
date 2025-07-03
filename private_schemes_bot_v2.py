import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8073483621:AAH88FAqGKBZd-mk5JeSRXFkytEaw9nsmug"

# Главное меню
def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("НАЧАЛО СМЕНЫ 👀", callback_data="start_shift")],
        [InlineKeyboardButton("ПРИВЯЗКА 😍", callback_data="hook")],
        [InlineKeyboardButton("НЕ ПРИВЯЗКА ⛔️", callback_data="no_hook")],
        [InlineKeyboardButton("РАЗЪЕБ НА НОМЕР 📲", callback_data="phone_push")],
        [InlineKeyboardButton("НЕТ КОНТАКТОВ ‼️", callback_data="no_contacts")],
        [InlineKeyboardButton("18+ 🍓", callback_data="adults")]
    ])

# Кнопка назад
def back_to_main_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="main")]])

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 Главное меню:Выбери нужный раздел 👇", reply_markup=main_menu_keyboard())

# Обработка нажатий
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main":
        await query.edit_message_text("📍 Главное меню: Выбери нужный раздел 👇", reply_markup=main_menu_keyboard())
    elif data == "start_shift":
        await query.edit_message_text("🔄 НАЧАЛО СМЕНЫ 👀(Здесь будет контент позже)", reply_markup=back_to_main_menu()) 
    elif data == "hook":
        elif data == "hook":
        await query.edit_message_text(
            "😍 Привязка — выбери ситуацию 👇",reply_markup=hook_submenu())
    elif data == "hook_1_3":
        await query.edit_message_text("🔥 Хорошее общение 1–3 дня — тут будет твой текст или контент!",reply_markup=hook_submenu())
    elif data == "hook_3_plus":
        await query.edit_message_text( "📞 Хорошее общение 3+ дней — здесь твой текст!",reply_markup=hook_submenu())
    elif data == "hook_miss":
        await query.edit_message_text("🖕 Мужчина общается, но часто пропадает — и тут твой текст!",reply_markup=hook_submenu())
        await query.edit_message_text("⛔️ НЕ ПРИВЯЗКА(Здесь будет контент позже)", reply_markup=back_to_main_menu())
    elif data == "phone_push":
        await query.edit_message_text("📲 РАЗЪЕБ НА НОМЕР(Здесь будет контент позже)", reply_markup=back_to_main_menu())
    elif data == "no_contacts":
        await query.edit_message_text("‼️ НЕТ КОНТАКТОВ(Здесь будет контент позже)", reply_markup=back_to_main_menu())
    elif data == "adults":
        await query.edit_message_text("🍓 18+(Здесь будет контент позже)", reply_markup=back_to_main_menu())

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    app.run_polling()
