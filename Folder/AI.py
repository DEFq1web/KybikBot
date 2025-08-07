# -*- coding: utf-8 -*-
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ВСТАВЬ СВОИ КЛЮЧИ СЮДА
TELEGRAM_TOKEN = '8197481766:AAFODC40tbsrL3nV7lhCUpWnvbMwyeRt4SU'
OPENAI_API_KEY = 'sk-proj-ob9CT043IbqG92iyKtGEO_UARYaGQyCPoYMLaP0aHG2zFADB8pjRCwJf_wa9qVkZdPmbxWR0hJT3BlbkFJHTmyMDtZzz2WxRrRlpNBYC6TiVVu2N1ax0hvo2CYPCMlcH3CFmI_BcYqafNhFYl3IlaqidM44Apip install --upgrade openai' \
'pip install --upgrade openaicd "H:\Новая папка (5)\PYTHON SCHOLL money\Folder"' \
''

# Настройка OpenAI
openai.api_key = OPENAI_API_KEY

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Получение ответа от ChatGPT
async def get_ai_response(user_message):
    try:
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Ты дружелюбный Telegram-бот."},
        {"role": "user", "content": user_message}
    ]
)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Ошибка при запросе к OpenAI: {e}"

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    chat_id = update.effective_chat.id
    ai_response = await get_ai_response(user_message)

    try:
        # Пробуем отправить ответ как есть
        await context.bot.send_message(chat_id=chat_id, text=ai_response)
    except Exception as e:
        # Если не получилось — отправляем сообщение об ошибке
        error_text = f"Ошибка при отправке сообщения: {e}"
        await context.bot.send_message(chat_id=chat_id, text=error_text)

# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я ИИ-бот. Напиши мне что-нибудь.")

# Главная функция
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logging.info("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()