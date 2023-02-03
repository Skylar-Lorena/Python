# lists are the equivalent of arrays in other languages
# we can create a list with square brackets 

list= () 
# "parentheses" tuple object that only contains unique values
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