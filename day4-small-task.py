import random

# who gonna pay the bill? 
friends = ["John", "Luna", "Rachil", "Jack", "Smith"]

length = len(friends) - 1
#print(length)

the_losser = random.randint(0, length)
#print(the_losser)

losser = friends[the_losser]
print(losser)
