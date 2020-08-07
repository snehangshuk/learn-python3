# Define your exception up here:
class OutOfStock(Exception):
  pass
# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] == 0:
      # If color is out of stock, raise OutOfStock and pass a custom message.
      raise OutOfStock("The {color} candles are out of stock.".format(color=color))
    else: 
      self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
try:
  candle_shop.buy('green')
# Print the custom message (e)  
except OutOfStock as e:
  print(e)
