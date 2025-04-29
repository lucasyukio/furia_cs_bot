from telegram import Update
from telegram.ext import ContextTypes
from services.hltv_service import get_proximo_jogo_furia

async def comando_prox_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = get_proximo_jogo_furia()
    await update.message.reply_text(msg)
