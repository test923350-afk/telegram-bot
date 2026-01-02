from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8541784156:AAGCahIUldF4-gYwus7LcubGNUvpJU0e4x4"

CHANNEL_IDS = [
    -1003506382995,
    -1003630407449
]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Open Channel", url="https://t.me/surruadhur")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to SurruAP Forex Signals.",
        reply_markup=reply_markup
    )

# /send command
async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage:\n/send Your message here"
        )
        return

    message_text = " ".join(context.args)

    keyboard = [
        [InlineKeyboardButton("Open Channel", url="https://t.me/surruadhur")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    for channel_id in CHANNEL_IDS:
        await context.bot.send_message(
            chat_id=channel_id,
            text=message_text,
            reply_markup=reply_markup
        )

    await update.message.reply_text("Message sent to both channels.")

# App setup
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("send", send))

print("Bot is running...")
app.run_polling()
