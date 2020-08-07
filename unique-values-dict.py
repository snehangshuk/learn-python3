'''Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.'''
# Write your unique_values function here:
def unique_values(my_dictionary):
  #value_lst = []
  unique_lst = []
  '''This use a loop to add value from the dict 
  to new list if they are not present in the list'''
  for value in my_dictionary.values():
    if value not in unique_lst:
      unique_lst.append(value)
  '''Below uses set() function to get only unique vakues from the list'''    
  #for value in my_dictionary.values():
  #  value_lst.append(value)
  #unique_lst = set(value_lst)
  return len(unique_lst)
  

    
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
