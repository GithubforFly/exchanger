mport requests

def get_crypto_prices(symbol):
  """
  Fetches the current price of a cryptocurrency using Coinlayer API.

  Args:
    symbol: The cryptocurrency symbol (e.g., BTC, ETH).

  Returns:
    The current price of the specified symbol as a float.
  """
  api_key = 6c75fb83cc2bbb862554837f3cc73e30 
  api_url = f"http://api.coinlayer.com/live?access_key={api_key}&symbols={symbol}"
  raw_data = requests.get(api_url).json()
  try:
    return raw_data['rates'][symbol]
  except KeyError:
    return None  # Handle unavailable symbol gracefully

# Example usage (optional)
# current_btc_price = get_crypto_prices("BTC")
# print(f"Current Bitcoin price: ${current_btc_price}")