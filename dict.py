'''List Comprehensions to Dictionaries'''

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drinks:caffeine for drinks, caffeine in zipped_drinks}
print(drinks_to_caffeine)
