'''
Different ways of sorting Dictionary by Keys and Reverse sorting by keys
'''
-----------------------------------------------------------------------------------

1. Using sorted() and items(): sorted() is used to sort the keys of the dictionary.

# Initialising dictionary 
my_dict = {2: 'three', 1: 'two', 4: 'five', 3: 'four'} 

# Sorting dictionary 
sorted_dict = sorted(my_dict.items()) 

# Printing sorted dictionary 
print("Sorted dictionary using sorted() and items() is :") 
for k, v in sorted_dict: 
	print(k, v) 


-----------------------------------------------------------------------------------
2. Using a lambda function 
The lambda function returns the key(0th element) for a specific item tuple, When these are passed to the sorted() method, 
it returns a sorted sequence which is then type-casted into a dictionary.

# Initialising a dictionary 
my_dict = {'a': 23, 'g': 67, 'e': 12, 45: 90} 

# Sorting dictionary using lambda function 
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1])) 

# Printing sorted dictionary 
print("Sorted dictionary using lambda is : ", sorted_dict) 
