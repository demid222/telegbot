from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

# Слова, при которых сообщение НЕ удаляется
KEYWORDS = ["топ", "игроков", "вырос", "равен"]

# Юзернейм бота, чьи сообщения нужно удалять
TARGET_USERNAME = "pipisabot"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    if message and message.from_user:
        sender = message.from_user
        text = message.text.lower() if message.text else ""
        if sender.username == TARGET_USERNAME or sender.id == 5667577098:  # можно заменить ID на нужный
            if not any(word in text for word in KEYWORDS):
                try:
                    await message.delete()
                    print("Сообщение удалено.")
                except Exception as e:
                    print(f"Ошибка удаления: {e}")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    print("Бот запущен.")
    app.run_polling()
