# Hyo Sun Lee, hyosunle@usc.edu
# ITP 115, Spring 2020

from MenuItem import MenuItem


# Next, define the Menu class in a file titled Menu.py.
# represents the restaurant’s menu which contains four different categories of menu items diners can order from
class Menu(object): # instance attribute:
    # The class will have a single class (or static) variable:
    # MENU_ITEM_TYPES: a list containing 4 strings, representing the 4 possible
    # types of menu items: "Drink", "Appetizer", "Entree", "Dessert".
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

# Define the following methods:
    # __init__
    # Parameter (1): a string representing the name of the csv file that
    # contains information about the menu items for the restaurant’s menu
    # Return value: none
    # Initialize the single instance attribute to an empty dictionary.
    # Open and read the csv file and create a MenuItem object from each line
    # in the file. Add the new object to the dictionary by using its type as the key.
    # Note that each line in the file contains the 4 pieces of information needed to create a MenuItem object.
    # Close the file object.
    def __init__(self, fileName):
        menuItemDictionary = {}
        for foodType in Menu.MENU_ITEM_TYPES:
            menuItemDictionary[foodType] = []
        fileIn = open(fileName, "r")
        for line in fileIn:
            line = line.strip()
            dataList = line.split(",")
            menuItem = MenuItem(dataList[0], dataList[1], dataList[2], dataList[3])
            menuItemDictionary[dataList[1]].append(menuItem)
        fileIn.close()

        self.menuItemDictionary = menuItemDictionary
    # a dictionary containing all the menu items from the menu
    # The keys are 3 strings representing the types of the menu item, and the values are a list of MenuItem objects.

    # Parameters (2): a string representing a type of menu item
    # (will be one of the four types listed in MENU_ITEM_TYPES)
    # and an integer representing the index position of a certain menu item
    # § Return value: a MenuItem object from the dictionary
    # Get the correct MenuItem from the dictionary using its type and index position in the list of items.
    def getMenuItem(self, menuItemType, index):
        menuItemList = self.menuItemDictionary[menuItemType]
        menuItem = menuItemList[index]
        return menuItem

    # Parameter (1): a string representing a type of menu item (will be one of
    # the four types listed in MENU_ITEM_TYPES)
    # Return value: None
    # Print a header with the type of menu items, followed by a numbered list of all the menu items of that type.
    def printMenuItemsByType(self, menuItemType):
        menuItemList = self.menuItemDictionary[menuItemType]
        counter = 0
        for line in menuItemList:
            print(str(counter) + ") " + str(line))
            counter += 1

    # Parameter (1): a string representing a type of menu item (will be one of the four types listed in MENU_ITEM_TYPES)
    # Return value: an integer representing the number of MenuItems of the input type
    # You do not need to define any getters and setters for this class.
    # At this point, you should be able to test the methods in the Menu class.
    def getNumMenuItemsByType(self, menuItemType):
        menuItemList = self.menuItemDictionary[menuItemType]
        count = len(menuItemList)
        # menuItemType will be either drink, entree, etc. this line tells us how many drinks there are
        return count
