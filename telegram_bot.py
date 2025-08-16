import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from variavel import itoken
from func_bot import start, echo, caps, meu_dinheiro

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    app = ApplicationBuilder().token(itoken).build()

        
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    meu_dinheiro_handler = CommandHandler('meu_dinheiro', meu_dinheiro)

    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.add_handler(caps_handler)
    app.add_handler(meu_dinheiro_handler)
    
    app.run_polling()