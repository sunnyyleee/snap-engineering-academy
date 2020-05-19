# define the Waiter class in a file titled Waiter.py.
# This class will make use of Menu and Diner objects, so be sure to include the proper import statements.
# This class will represent the restaurant’s waiter.
# The waiter maintains a list of the diners it is currently taking care of, and
# progresses them through the different stages of the restaurant.
# The waiter in the simulation will repeat multiple cycles of attending to the diners.
# In each cycle, the waiter will seat a new diner, if one arrives, take any diners’ orders if needed,
# and give diners their bill, according to each diner’s status.
from Menu import Menu
from Diner import Diner


class Waiter(object):
    # The class will use the following instance attributes:
    # self.diners, self.menu:

    # § Parameter(1):a Menu object
    # § Return value: none
    # § Assign the input parameter to the corresponding attribute.
    # Initialize the list of diners to an empty list.
    def __init__(self, Menu):
        self.diners = []    # a list of Diner objects the waiter is attending to
        self.menu = Menu # a Menu object representing the restaurant’s menu

    # § Parameter(1):a Diner object
    # § Return Value: none
    # § Add the new Diner object to the waiter’s list of diners.
    def addDiner(self, Diner):
        self.diners.append(Diner) # removed name

    # § Parameters: none
    # § Return Value: an integer representing the number of diners the waiter is currently keeping track of
    def getNumDiners(self):
        dinerNums = len(self.diners)
        return dinerNums

    # § Parameters: none
    # § Return Value: none
    # § Print all the diners the waiter is keeping track of, grouped by their statuses.
    # Loop through each of the possible dining statuses a Diner might have
    # (hint: use the Diner class attribute) to group the diners.
    def printDinerStatuses(self):
        for status in Diner.STATUSES:
            print("Diners who are " + status + ":")
            for diner in self.diners:
                if diner.getStatus() == status:
                    print(str(diner) + ".")

    # § Parameters: none
    # § Return Value: none
    # § Loop through the list of diners and check if the diner’s status is
    # “ordering”.
    # § For each diner that is ordering, loop through the different menu types
    # (hint: use the class attribute from the Menu class).
    # With each menu type, print the menu items of that type,
# then ask the diner to order a menu item by selecting a number
    # (be sure to include error checking).
    # After the diner selected a menu item, add the item to the diner.
    # Once the diner orders one menu item of each type, print the diner’s order.
    # Each diner must order exactly one item of each type.
    def takeOrders(self):
        for diner in self.diners:
            if diner.getStatus() == "ordering":
                for header in Menu.MENU_ITEM_TYPES:
                    print("\n-----" + header.upper() + "S-----")
                    Menu.printMenuItemsByType(self.menu, header)
                    length = Menu.getNumMenuItemsByType(self.menu, header)
                    print(diner.getName() + ", please select a " + header + " menu item number.")

                    # ERROR CHECKING
                    x = True
                    while x:
                        userInput = input("> ")
                        if userInput.isalnum():     # if it is a number then checks if in range
                            userInput = int(userInput)
                            if userInput in range(0, length):   # if it a number in range, then stops loop
                                x = False
                                diner.addToOrder(self.menu.getMenuItem(header, userInput))
                            else:   # if it isn't a number in range, then it continues the loop
                                continue
                        else:   # if input isn't a num, then it continues the loop
                            x = True

    # Parameters: none
    # § Return Value: none
    # § Loop through the list of diners and check if the diner’s status is “paying”.
    # § For each diner that is paying, calculate the diner’s meal cost and print it
    # out in a message to the diner.
    def ringUpDiners(self):
        for diner in self.diners:
            if diner.getStatus() == "paying":
                billCost = diner.calculateMealCost()
                print("\n" + diner.getName() + ", your meal cost $" + str(billCost))

    def getDiners(self): # getDiner getter
        return self.diners

# § Parameters: none
# § Return Value: none
# § Loop through the list of diners and check if the diner’s status is
# “leaving”.
# § For each diner that is leaving, print a message thanking the diner.
# § Loop through the list of diners backwards. Hint: use a range-based for
# loop.
# § For each diner that is leaving, remove the diner from the list.
    def removeDoneDiners(self):
        for item in range(len(self.diners)-1, -1, -1):
            if self.diners[item].getStatus() == "leaving":
                print("\n" + self.diners[item].getName() + ", thank you for dining with us! Come again soon!")
                del self.diners[item]

# § Parameters: none
# § Return Value: none
# This method allows the waiter to attend to the diners at their various
# stages as well as move each diner on to the next stage.
# § First, call the printDinerStatuses() method.
# § Then, in order, call the takeOrders(), ringUpDiners(), and
# removeDiners() methods.
# § Finally, update each diner’s status.
# o You do not need to define any getters and setters for this class.
# • At this point, if your classes are all correctly implemented, you should be able to run the program in its entirety.
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        # Diner.updateStatus() # removed self
        # update the status of the individual diners
        for diner in self.getDiners():
           diner.updateStatus()




