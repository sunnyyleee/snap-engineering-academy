# Hyo Sun Lee, hyosunle@usc.edu
# ITP 115, Spring 2020
# Final Project
# Description: Restaurant


class MenuItem(object): # This class will represent a single item that a diner can order from the restaurant’s menu
    def __init__(self, nameParam, typeParam, priceParam, descParam):
        self.name = nameParam   # self.name: a string representing the name of the MenuItem
        self.type = typeParam   # self.type: a string representing the type of item
        self.price = float(priceParam) # self.price: a float representing the price of the item
        self.description = descParam    # self.description: a string containing a description of the item

    # 4 getters, no setters
    # Define get methods for each of the 4 attributes. Note that not all of these may be used.
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getPrice(self):
        return self.price

    def getDesc(self):
        return self.description

    # __str__
    # § Parameters: none
    # § Return value: a string
    # § Construct a message containing all 4 attributes, formatted in a readable manner.
    def __str__(self):
        msg = str(self.name) + " (" + str(self.type) + "): $" + str(self.price) + "\n\t" + str(self.description)
        return msg



