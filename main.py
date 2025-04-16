from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os
import time

# Слова, при которых сообщение НЕ удаляется
KEYWORDS = ["топ", "игроков", "вырос", "равен"]

# Юзернейм бота, чьи сообщения нужно удалять
TARGET_USERNAME = "pipisabot"

async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    if message and message.from_user:
        sender = message.from_user
        text = message.text.lower() if message.text else ""
        if sender.username == TARGET_USERNAME or sender.id == 5667577098:  # Можно заменить ID на нужный
            if not any(word in text for word in KEYWORDS):
                try:
                    await message.delete()
                    print("Сообщение удалено.")
                except Exception as e:
                    print(f"Ошибка удаления: {e}")

async def delete_past_messages(context: ContextTypes.DEFAULT_TYPE):
    """Удаляет старые сообщения бота"""
    chat_id = context.job.context
    messages = await context.bot.get_chat_history(chat_id=chat_id, limit=100)  # Получаем последние 100 сообщений
    for message in messages:
        if message.from_user and (message.from_user.username == TARGET_USERNAME or message.from_user.id == 5667577098):
            if not any(word in message.text.lower() for word in KEYWORDS):
                try:
                    await message.delete()
                    print(f"Старое сообщение удалено: {message.message_id}")
                except Exception as e:
                    print(f"Ошибка удаления старого сообщения: {e}")

if __name__ == "__main__":
    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    chat_id = "-1002604357013"  # Укажи сюда ID своей группы или username
    
    
    app.add_handler(MessageHandler(filters.ALL, delete_message))
    print("Бот запущен.")
    app.run_polling()
