""" Variables for Example -  start """
x = 9
y = 10
subjective = "python"
type = " language"
array = 1,2,3,4,5,6
"""  Variables for Example - end """

""" Useful Functions """
print(f"{x == y}")  # Check equality 
print(f"{x + y}") # when made with two int variables it is a common sum 
print(f"{subjective + type}") # however, when used between variables of type string, it performs a concatenation
print(f"{subjective[0]}") # Accesses the value from position i
print(f"{subjective[0:2]}") # Accesses the values from position i to j
print(f"{len(type)}") # count the size of the variable
print(f"{min(array)}") # find the minimum value of the array  
print(f"{max(array)}") # find the maximum value of the array 
print(f"{array.count(2)}") # count how many times the element inside the parenthesis appears in the array
 