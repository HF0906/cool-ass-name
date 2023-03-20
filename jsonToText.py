# author: hayden + mr mercado
import json

# open the json file
file = open('jsonLarge.json')

# read the json file
data = json.load(file)


# print the json file so we can see what the json looks like
print(data)

            
# read each key in the json file
    # write the key to a TXT file
    # read the corresponding value
    # write the value next to the key in the TXT file
text_file = open("king","w")

for x in data:
    n = text_file.write(x + " " + data[x] + f"\n" )


# save the TXT file

text_file.close()
