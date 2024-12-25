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
