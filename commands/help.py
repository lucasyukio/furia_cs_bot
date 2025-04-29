from telegram import Update
from telegram.ext import ContextTypes

async def comando_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("DEBUG: comando /help acionado")
    mensagem = (
        "Comandos disponíveis no FURIA CS Bot:\n\n"
        "/proximojogo - Mostra o próximo jogo da FURIA\n"
        "/lineup - Mostra a escalação atual do time\n"
        "/ranking - Mostra a posição no ranking mundial\n"
        "/comandos - Exibe esta mensagem"
    )
    await update.message.reply_text(mensagem)
