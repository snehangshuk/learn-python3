from sys import argv

script, filename = argv
my_name = "Snehangshu"
# old style
print("Hello and welcome %s!" %(my_name))
# new style
print("Hello and welcome {}!".format(my_name))
# another style
print(f"Hello and welcome {my_name}!")
'''Reading from a file'''
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
