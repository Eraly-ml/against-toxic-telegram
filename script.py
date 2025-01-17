import logging
import csv
from detoxify import Detoxify
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import nest_asyncio
import asyncio
from pathlib import Path
from dotenv import load_dotenv
import os

"""
Это у нас переменные для работы с кодом, и если вы хотите использовать код то не забудьте сделать .env файл для токена вашего бота.
These are variables for working with the code, and if you want to use the code, don't forget to make an. env file for your bot's token.
"""
LOG_FILE = "bot_logs.csv"
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Проверяем, существует ли файл, если нет — создаем с заголовками
if not Path(LOG_FILE).exists():
    with open(LOG_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "User_ID", "Username", "Chat_ID", "Chat_Title", "Message", "Action", "Toxic_Categories"])

# Настраиваем логирование для отладки
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Устанавливаем уровень логирования для httpx и telegram
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)

"""
В функций для анализа сообщений есть переменная threshold вы можете её изменять по желанию сейчас 
она стоит 0.5 это означает что сторогость модели 50%.
In def analyze_massage you can see threshold variable, You able to change it, but 0,5 the best
"""
# Функция для анализа токсичности
def analyze_message(message, threshold=0.5): 
    results = Detoxify('multilingual').predict([message])
    toxicity_categories = [
        "toxicity", "severe_toxicity", "obscene",
        "identity_attack", "insult", "threat", "sexual_explicit"
    ]
    toxic_scores = {key: results[key][0] for key in toxicity_categories}
    toxic_flags = {key: score > threshold for key, score in toxic_scores.items()}
    is_toxic = any(toxic_flags.values())

    if is_toxic:
        toxic_details = {key: toxic_scores[key] for key, flag in toxic_flags.items() if flag}
        return True, toxic_details
    return False, {}

# Запись логов в CSV (только для токсичных сообщений)
def log_to_csv(user_id, username, chat_id, chat_title, message, action, toxic_categories):
    if toxic_categories:  # Логируем только если есть токсичные категории
        with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                logging.Formatter("%(asctime)s").format(logging.LogRecord("", 0, "", 0, "", None, None)),
                user_id,
                username,
                chat_id,
                chat_title or "Private Chat",
                message,
                action,
                ", ".join(toxic_categories)
            ])

# Обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    chat = update.effective_chat
    message = update.message.text

    if not message:  # Если это не текст, игнорируем
        return

    # Анализируем сообщение
    is_toxic, toxic_details = analyze_message(message)
    toxic_categories = toxic_details.keys() if is_toxic else []

    """
    Тут мы логируем только токсичные сообщения, но вы можете логирывать все сообщения если по работаете над кодом
    """
    if is_toxic:
        log_to_csv(
            user_id=user.id,
            username=user.username,
            chat_id=chat.id,
            chat_title=chat.title,
            message=message,
            action="Deleted",
            toxic_categories=toxic_categories
        )

        # Удаляем токсичное сообщение и отправляем предупреждение
        try:
            await update.message.delete()
            warning = (
                f"Удалено токсичное сообщение от {user.first_name}.\n"
                f"Категории токсичности: {', '.join(toxic_categories)}"
            )
            await context.bot.send_message(chat_id=chat.id, text=warning)
        except Exception as e:
            logger.error(f"Ошибка при удалении сообщения: {e}")

# Основная функция для запуска бота
async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    await application.run_polling()

if __name__ == "__main__":
    nest_asyncio.apply()  # Применяем патч для поддержки вложенных циклов asyncio
    asyncio.run(main())
""" 
As you can see this code was written as bilingual but i used russian lang many times than english
"""
