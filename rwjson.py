# Script writes and reads a JSON file
import json

# JSON data to be written
dictionary = {
    "name": "Snehangshu Karmakar",
    "email": "snehangshu@gmail.com",
    "phonenumber": "8860841841",
    "location": "Bangalore"
}
# Serailizing JSON
json_object = json.dumps(dictionary, indent = 4)

# Writing to sample.json
outfile = open("sample.json", "w")
outfile.write(json_object)
outfile.close()

# Read from sample.json
print("Reading from sample.json")
outfile = open("sample.json", "r")
json_object = json.load(outfile)
print(json_object)
outfile.close()
