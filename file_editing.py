# Sample and choices method from random module
# Sample method from the random module is used to generate a random element from a list without replacement

from random import sample

my_list = ["Ice-Cream", "Chocolate", "Vanilla", "Mint"]

print(sample(population=my_list, k=3))

# Choices method from the random module is used to generate a random element from a list with replacement
from random import choices

print(choices(population=my_list, k=8))

# Install the Wikipedia module
!pip install wikipedia

import wikipedia

# In-built module
import os

# Get the current working directory
os.getcwd()

# CWD - Current Working Directory (Folder)
# File operations
path = r"C:\Users\Lakshni\Documents\Arush\IT_material\halp.txt"

file = open(path, "r")
print(file.read())
file.close()

# "r" implies read mode

path = r"C:\Users\Lakshni\Documents\Arush\IT_material\halp.txt"

file = open(path, "a")
file.write("\nPython is an Object-Oriented Programming Language named by its creator after famous British comedy show Monty Python's Flying Circus?")
file.close()

path = r"C:\Users\Lakshni\Documents\Arush\IT_material\halp.txt"

file = open(path, "r")
print(file.read())
file.close()
