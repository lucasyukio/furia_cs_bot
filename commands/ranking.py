from telegram import Update
from telegram.ext import ContextTypes
from services.hltv_service import get_ranking_furia

async def comando_ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("DEBUG: comando_ranking foi acionado")
    msg = get_ranking_furia()
    await update.message.reply_text(msg, parse_mode="Markdown")
