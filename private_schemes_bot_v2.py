
    import logging
    from telegram import Update, ReplyKeyboardMarkup
    from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

    # Логирование
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    # Доступ только для владельца (временно — только твой Telegram ID, потом можно расширить)
    ALLOWED_USERS = [8073483621]

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if user_id not in ALLOWED_USERS:
            await update.message.reply_text("⛔ У вас нет доступа к этому боту.")
            return

        keyboard = [
            ["📌 Принципы работы", "💬 Схемы привязки"],
            ["💰 Схемы: Тянем баланс", "🎁 Сайт X и Подарки"],
            ["📞 Вывод за сайт", "❓ Помощь"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Привет! Выбери нужный раздел:", reply_markup=reply_markup)

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if user_id not in ALLOWED_USERS:
            await update.message.reply_text("⛔ У вас нет доступа к этому боту.")
            return

        text = update.message.text

        responses = {
            "📌 Принципы работы": "Мы работаем на привязку. Даём романтику, раскрываем себя, подводим к письмам и создаём баланс.",
            "💬 Схемы привязки": "Если мужчина не идёт на привязку — предлагаем уйти с сайта, обмениваемся контактами, делаем звонок и дожимаем вне сайта.",
            "💰 Схемы: Тянем баланс": "Схемы:
- Виза и приезд
- Больницы и болезни
- Сайт завис
- Подарки и медиа
- Возврат средств",
            "🎁 Сайт X и Подарки": "Сайт X — где 'можно всё'. Подарки — через сайт, как внимание, сюрприз, знак любви.",
            "📞 Вывод за сайт": "Привязываем → предлагаем обмен контактами → звонок → полное закрытие вне сайта.",
            "❓ Помощь": "Если не знаешь, что выбрать — пиши менеджеру. Или нажми /start."
        }

        reply = responses.get(text, "Пожалуйста, выбери вариант из меню.")
        await update.message.reply_text(reply)

    if __name__ == "__main__":
        app = ApplicationBuilder().token("8073483621:AAEN5hE2U0_Za2Rbfs68Bp6prWMDekzxIpA").build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        app.run_polling()
