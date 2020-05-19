# Diner class represents one of the diners at the restaurant and keeps tracks of their status and meal.
# • The class will use the following instance attributes:
# o self.name: a string representing the diner’s name
# o self.order: a list of the MenuItem objects ordered by the diner
# o self.status: an integer corresponding the diner’s current dining status

from MenuItem import MenuItem
# It will make use of MenuItem objects, so added import statement


class Diner(object):

    STATUSES = ["seated", "ordering", "eating", "paying", "leaving"]
    # a list of strings containing the possible statuses a diner might have

    # § Parameter (1): a string representing the diner’s name
    # § Return value: none
    # § Set the diner’s name attribute to the input value.
    # Set the diner’s order attribute to an empty list (the diner has not ordered any menu items yet),
    # set the status attribute to 0 (corresponding to a seated status).
    def __init__(self, dinerName):
        self.name = dinerName
        self.order = []
        self.status = 0

    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return Diner.STATUSES[self.status]

    # define get methods for all the instance attributes. There is no need to define
    # set methods for the instance attributes.

    def updateStatus(self):
        # § Parameters: none
        # § Return value: none
        # § Increase the diner’s status by 1.
        self.status += 1

    def addToOrder(self, MenuItem):
        # § Parameters: a MenuItem  object
        # § Return value: none
        # Adds the menu item to the end of the list of menu items (instance attribute)
        self.order.append(MenuItem)

    def printOrder(self):   # for loop
        # § Parameters: none
        # § Return value: none
        # § Print a message containing all the menu items the diner ordered.
        # print(dinerName, "ordered:")
        for item in self.order:
            print(item)

    def calculateMealCost(self):
        # § Parameters: none
        # § Return value: a float representing the total cost of the diner’s meal
        # Total up the cost of each of the menu items the diner ordered.
        cost = float(0.00)
        for item in self.order:
            cost += item.price
        return cost

    def __str__(self):
        # § Parameters: none
        # § Return value: a string
        # § Construct a message containing the diner’s name and status, formatted in a readable manner. Examples:
        # Diner Paul is currently seated. Diner Faith is currently ordering.
        msg = "\tDiner " + self.getName() + " is currently " + self.getStatus()
        return msg
