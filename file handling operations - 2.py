with open('Codingal.txt','w') as file:
 file.write("Hi! I am dumboy and i am not even born yet")
file.close()

with open('Codingal','r') as file:
 data = file.readlines()
 print("Words in the file are...........................................")
 for line in data:
  word = line.split()
  print (word)
file.close()
