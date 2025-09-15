# basic star pattern
print("Star pattern \n")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print('\n')

# Inverted Star pattern
print("Inverted Star pattern \n")
for i in range(6,1,-1):
    for j in range(i, 1, -1):
      print("*", end="\n")
      print('\n')