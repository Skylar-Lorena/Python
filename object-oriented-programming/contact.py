# Classes
# A class is a blueprint to create objects. It allows us to group data and functions 
# logically and in an easy to use manner.
# When creating a blueprint, we will include all features (read attributes) and behaviors (read methods).
# This will be our template to creating objects
# Objects are instances of a class. Objects can have different properties but implement same attributes and methods
# Feature project: Contact List App
#    class Contact:
    # """
    # Class that generates new instances of contacts
    # """
        # def __init__(self,first_name,last_name,phone_number,email):

        # '''
        # __init__ method that helps us define properties for our objects.

        # Args:
            # first_name: New contact first name.
            # last_name : New contact last name.
            # number: New contact phone number.
            # email : New contact email address.
        # self is a variable that represents the instance of the object itself. The self variable can be likened to the this keyword,
    # 
class Contact:
    contact_list = [] # Empty contact list
    def __init__(self,first_name,last_name,phone_number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        
    