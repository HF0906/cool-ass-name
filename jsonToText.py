# author: hayden + mr mercado
import json

# open the json file
file = open('jsonformatter.txt')

# read the json file
data = json.load(file)


# print the json file so we can see what the json looks like
print(data)

            
# read each key in the json file
    # write the key to a TXT file
    # read the corresponding value
    # write the value next to the key in the TXT file

jsonData = data["emp_details"]
for x in jsonData:
    keys = x.keys()
    print(keys)
    values = x.values()
    print(values)


# save the TXT file
