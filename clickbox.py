from math import *
first_side = int(input("Enter first side length:"))
second_side = int(input("Enter second side length:"))
hypo_side = int(sqrt((first_side*first_side) + (second_side*second_side)))
print(hypo_side)