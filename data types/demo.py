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
