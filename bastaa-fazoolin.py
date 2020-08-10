#from datetime import *
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    #return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time.strftime("%I:%M %p"), end_time=self.end_time.strftime("%I:%M %p"))
    return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

  def calculate_bill(self, purchased_items):
    total_bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        total_bill += self.items[purchased_item]
    return total_bill    

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, avltime):
    avlmenus = []
    for menu in self.menus:
      #avlmenus.append(menu.start_time)
      if menu.end_time <= avltime and menu.start_time >= avltime:
          avlmenus.append(menu)
    return avlmenus     

class Business:
   def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


   
  
#start = time(11, 00)
#end = time(16, 00)
brunch_menu = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 1100, 1600)

#start = time(15, 00)
#end = time(18, 00)
early_bird_menu = Menu("early_bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1500, 1800)

#start = time(17, 00)
#end = time(23, 00)
dinner_menu = Menu("dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300)

#start = time(12, 00)
#end = time(21, 00)
kids_menu = Menu("kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1200, 2100)

print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))  

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store.menus)
print(flagship_store.available_menus(1200))

arepas_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50} 
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
new_business = Business("Take a' Arepa", arepas_place)


