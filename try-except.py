caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
key = "matcha"
try:
  caffeine_level[key] = 30
  print(caffeine_level[key])
except KeyError:
  print("Unknown Caffeine Level")
