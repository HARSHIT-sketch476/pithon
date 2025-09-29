file = open('Codingal.text','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Codingal.txt','a')
file.write(" Hi! Iam an innocent kid and i am infinity yr old ")
file.close()