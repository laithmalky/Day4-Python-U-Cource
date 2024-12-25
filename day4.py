import random
import my_module

# random number from 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# how to call functions from other classes (files)
print(my_module.MyModuleNumber) 


# random numbers from 0.0 to 0.999 less than one but never be one
random_float = random.random()
print(random_float)

random_float_more_bigger_than_one = random.random() * 10
print(random_float_more_bigger_than_one)

random_float_range = random.uniform(1, 10) # random number could be 20 
print(random_float_range)


########################################################################

# small task to get random face for a coin

random_coin = random.randint(1,2)
print(random_coin)

if random_coin == 1:
    print("Head")
else:
    print("Tail")



#########################################

# The list

list_of_fruits = ["Apple", "Tomato", "What else?", "didnt finish yet?"]
print(list_of_fruits[2]) # for print just spicefic item from the list

list_of_fruits[2] = "What else ? !" # for change any item in the list
print(list_of_fruits[2])

list_of_fruits.append("Hello") # to add any item to the list
print(list_of_fruits)

list_of_fruits.extend(["yo wasap", "How u doing"]) # to add list to the list
print(list_of_fruits)

friends = ["John", "Luna", "Rachil", "Jack", "Smith"]
print(random.choice(friends)) # to get a random item from any list 

# List on the list 
fruits = ["hello", "welcome"]
non_fruits = ["wasap", "how u doin"]

the_big_list = [fruits, non_fruits]
print(the_big_list)
