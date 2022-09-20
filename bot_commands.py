import numbers
from telegram import CallbackQuery, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def sum_command(update: Update, context: CallbackQuery) -> str:
    numbersStr = update.message.text
    numbersLi = numbersStr.split()
    result = int(numbersLi[1]) + int(numbersLi[2]) 
    # numbersStr = update.message.text
    # number1 = update.message.text
    # number2 = update.message.text
    # result = int(number1) + int(number2)

    await update.message.reply_text(result)