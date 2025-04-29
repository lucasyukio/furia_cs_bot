from telegram import Update
from telegram.ext import ContextTypes

async def comando_teste(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Funcionando! ✅")
