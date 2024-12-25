import random
import my_module

# random number from 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# how to call functions from other classes (files)
print(my_module.MyModuleNumber) 


# random numbers from 0.0 to 0.999 less than one 
random_float = random.random()
print(random_float)

random_float_more_bigger_than_one = random.random() * 10
print(random_float_more_bigger_than_one)