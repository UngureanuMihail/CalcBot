from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5515201563:AAGgbwjUZtMSCOO518kivwbSREU9ACOPQCE").build()

app.add_handler(CommandHandler("hello", hello_command))
#app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))
#app.add_handler(CommandHandler("minus", minus_command))

print('start')


app.run_polling()