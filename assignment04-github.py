#reading file...
with open("test.txt", "r") as file:
    content = file.read()

print(content)

#changing a word in the file
'''
content = content.replace("is", "is not")

with open("file.txt", "w") as file:
    file.write(content)
'''
# Well that didn't work - why didn't just replace is with is not? it reads This not is not a test. try a 
#different word

content = content.replace("That", "This")

with open("file.txt", "w") as file:
    file.write(content)