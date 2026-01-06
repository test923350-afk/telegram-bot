import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

CHANNEL_IDS = [
    -1003630407449,
    -1003506382995,
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("Open Channel", url="https://t.me/surruadhur")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to SurruAP Bot",
        reply_markup=reply_markup
    )

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /send your message")
        return

    message_text = " ".join(context.args)

    keyboard = [[InlineKeyboardButton("Connect Support", url="https://t.me/surruadhur")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    for channel_id in CHANNEL_IDS:
        await context.bot.send_message(
            chat_id=channel_id,
            text=message_text,
            reply_markup=reply_markup
        )

    await update.message.reply_text("Message sent to both channels.")

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
