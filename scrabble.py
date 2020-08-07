'''In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.'''

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

#Test Function with word lists by each player
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

'''Define a function called score_word that takes in a parameter word. You should get the point value from the letter_to_points dictionary. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.'''
'''make your letter_to_points dictionary able to handle lowercase inputs as well'''
def score_word(word):
  point_total = 0
  for letter in word:
    for key, value in letter_to_points.items():
      if letter == key or letter.lower() == key.lower():
        point_total += value
  return point_total

#Test Functions
#brownie_points = score_word("BROWNIE")  
#print(brownie_points)

'''a function that would take in a player and a word, and add that word to the list of words they’ve played'''
def play_word(player, word):
  key_exists = player_to_words.get(player, "False")
  if key_exists != "False":
    player_to_words[player].append(word)
  return update_point_totals()

'''turn your nested loops into a function that you can call any time a word is played'''
def update_point_totals():
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

print(play_word("player1", "Snehangshu"))
