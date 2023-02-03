# lists are the equivalent of arrays in other languages
# we can create a list with square brackets 

list= () 
# "parentheses" tuple object that only contains unique values
# Tuples values cannot be changed once created. They are immutable
# We can create tuples using parentheses or the tuple() function

list_a = []
list_b = [1,2,3,4,5]
list_c = ["Emily",2,3,4,"windows"]
#we can join lists using the extend method
list_b.extend(list_c)
print(list_b)

# we can also append values to the list using the append method
list_b.append("Wakanyi")
print(list_b)
list_a.append("Wakanyi")
print(list_a)

# we can use the reverse method to reverse the list and use sort to arrange items in ascending order
list_b.reverse()
print(list_b)
list_d = [99,28, 22, 768, 100]
list_d.sort()
print(list_d)

#dictionary
# dictionaries store collections of many values of different types. 
# we can create a dictionary using parentheses or the dictionary() function
dict = {}
dict["name"] = "Emily"
dict["age"] = 28
dict["height"] = 1.75
dict["weight"] = 70
print(dict)
# Indexes in the dictionary are called keys while the values are called values
# we can use the keys() method to get the keys of the dictionary
print(dict.keys())
# we can use the values() method to get the values of the dictionary
print(dict.values())

# String Formatting
# This is a way of embedding variables into strings. 
name = "Emily"
age = 28
print(f"My name is {name} and my age is {age}")

# Typecasting 
# Type casting is a way of converting one datatype to another
print("My name is" +" " + name + " "+ "and my age is " + str(age))

# Slicing
# Slicing is the act of getting subsets or parts of strings, lists or tuples.
# we can use the slice() method to get the first 5 characters of a string
print(name[0:3])
numbers= [11,12,13,14,15,16,17,18,19,20,21]
print(numbers[0:5])
# A slice statement is enclosed with [] square brackets and has two parts first is the 
# position where to start slicing and second is the position to stop but not including that position.

