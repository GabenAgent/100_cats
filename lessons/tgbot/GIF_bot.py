import requests
import os
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7136444380:AAGrl7o5yUcLWOSR0xkrAb6P4a3USqpX7VI"
BOT_USERNAME: Final = "@GIF_FOR_PROJ_BOT"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("A GIF, here u can find")
    await update.message.reply_text("The topic u should give me")


def handle_response(content):

    url = "http://api.giphy.com/v1/gifs/search"
    api_key = "EIkGxAqymsKn4iwsrA9CbV8y7n1WDAyW"

    params = {
        "q": content,
        "api_key": api_key,
        "limit": "1"
    }

    response = requests.get(url, params=params)
    data = response.json()
    gif_url = data["data"][0]["images"]["fixed_height"]["url"]
    return gif_url


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print("Bot:", response)
    await update.message.reply_text(response)

    # gif_filename = "temp.gif"
    # with requests.get(response, stream=True) as r:
    #     with open(gif_filename, "wb") as f:
    #         for chunk in r.iter_content(chunk_size=8192):
    #             f.write(chunk)
    #
    # # Send the downloaded GIF as a file
    # with open(gif_filename, "rb") as gif_file:
    #     await update.message.reply_document(gif_file)
    #
    # # Delete temporary GIF file
    # os.remove(gif_filename)


if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    print("Polling...")
    app.run_polling(poll_interval=3)
