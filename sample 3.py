file = open('Codingal.text', 'r')
Counter = 0

content = file.read()
CoList = content.split("\n")

for i in CoList:
  if i:
    Counter += 1
print("this is the number of lines in the file ")
print(Counter)