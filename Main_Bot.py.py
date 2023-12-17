from telegram import Update, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import re  # To extract symbols from expressions

def welcome_message(update: Update, context: CallbackContext) -> None:
  keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton(" Calculator", callback_data="calculator")],
    [InlineKeyboardButton("1️⃣ Buy Crypto", callback_data="buy_crypto")],
    [InlineKeyboardButton("2️⃣ Sell Crypto", callback_data="sell_crypto")],
    [InlineKeyboardButton(" Crypto News", callback_data="crypto_news")],
  ])

  context.bot.send_message(
    chat_id=update.effective_chat.id,
    text="Welcome! Your quick and comfy assistant is here. What would you like to do?",
    reply_markup=keyboard,
  )

def button_handler(update: Update, context: CallbackContext) -> None:
  query = update.callback_query
  button_data = query.data

  if button_data == "calculator":
    process_calculation(update, context)
  elif button_data == "buy_crypto":
    buy_crypto(update, context)  # Needs further implementation
  elif button_data == "sell_crypto":
    sell_crypto(update, context)  # Needs further implementation
  elif button_data == "crypto_news":
    crypto_news(update, context)  # Needs further implementation

def process_calculation(update: Update, context: CallbackContext) -> None:
  expression = update.message.text

  # Check for cryptocurrency symbols in the expression
  crypto_symbols = re.findall(r'[A-Z]{3}', expression)
  if not crypto_symbols:
    # Handle non-crypto calculations here
    ...

  else:
    # Process expressions with crypto symbols
    result = None
    for symbol in crypto_symbols:
      # Get the current price using Coinlayer API from Coinlayer_api.py
      current_price = get_crypto_prices(symbol)
      if current_price is None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Symbol '{symbol}' not found!")
        return
      # Update expression with actual prices (replace symbol occurrences)
      expression = expression.replace(symbol, f"{current_price:.2f}")

    # Evaluate the updated expression with replaced prices
    try:
      result = eval(expression)
    except Exception as e:
      context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invalid expression: {e}")
      return

    # Send response with calculated result and used prices
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your expression: {expression}\n\n➡️  Result: {result:.2f}")


updater = Updater(6338590919:AAHfAQQIe19tMYkvWrVF8-pwGj9Fu32wYvk)
updater.dispatcher.add_handler(MessageHandler(Filters.text(" Calculator"), calculator))
updater.dispatcher.add_handler(MessageHandler(Filters.text, process_calculation))
updater.dispatcher.add_handler(CallbackQueryHandler(button_handler))
updater.start_polling()
updater.idle()
