from telegram import Update
from telegram.ext import ContextTypes

FURIA_LINEUP = [
    "🎯 KSCERATO",
    "💥 yuurih",
    "⚔️ YEKINDAR",
    "🧠 FalleN",
    "🔥 molodoy"
]

async def comando_lineup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = "**Line-up atual da FURIA CS2:**\n\n"
    mensagem += "\n".join(FURIA_LINEUP)
    await update.message.reply_text(mensagem, parse_mode="Markdown")
