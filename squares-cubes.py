single_digits = list(range(10))
squares = []
cubes = []
for element in single_digits:
  print(element)
squares = [element ** 2 for element in single_digits]
print(squares)
cubes = [element ** 3 for element in single_digits]
print(cubes)
