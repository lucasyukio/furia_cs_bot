from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN
from commands.prox_jogo import comando_prox_jogo
from commands.lineup import comando_lineup
from commands.ranking import comando_ranking
from commands.teste import comando_teste
from commands.help import comando_help

print("DEBUG: comando_help foi importado")


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("proximojogo", comando_prox_jogo))
app.add_handler(CommandHandler("lineup", comando_lineup))
app.add_handler(CommandHandler("ranking", comando_ranking))
app.add_handler(CommandHandler("teste", comando_teste))
app.add_handler(CommandHandler("comandos", comando_help))

print("Bot is running...")
app.run_polling()  
