from config import config as cfg

apikey = cfg["githubkey"]



#reading file...
with open("Andrew.txt", "r") as file:
    content = file.read()

print(content)

#changing a word in the file
'''
content = content.replace("is", "is not")

with open("file.txt", "w") as file:
    file.write(content)

# Well that didn't work - why didn't just replace is with is not? it reads This not is not a test. try a 
#different word

content = content.replace("That", "This")

with open("file.txt", "w") as file:
    file.write(content)
'''

# change content to content 2 and words in lowercase

# https://www.geeksforgeeks.org/python/python-replace-multiple-characters-at-once/

replacements = {"Andrew": "Marcella", "teach": "learn"}

for old, new in replacements.items():
 content= content.replace(old, new) # had issues here with it only replacing the second word - i needed to keep the changes after the first word
 # changes so content = content.replace does this

print(content)

# content2 = content.replace("Andrew":"Marcella", "teach":"learn")



with open("file.txt", "w") as file:
    file.write(content)

