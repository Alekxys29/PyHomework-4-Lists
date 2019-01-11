"""
Homework Assignment #4: Lists

This program accepts a value and will be stored in a list. Then it 
matches the value if it's already in the list. If the value doesn't
exist in the list, it will be added to the list and returns True, 
otherwise it returns False and store the value in another list.
"""
# Declaring empty list
myUniqueList = []
myLeftovers = []

def addToList(param1):
    # executes if the value doesn't exist in myUniqueList
    if param1 not in myUniqueList:
        myUniqueList.append(param1)
        print("Unique List: %s " % myUniqueList)
        return True

    # executes if the values does exist in myUniqueList
    myLeftovers.append(param1)
    print("Leftover List: %s " % myLeftovers)
    return False

print(addToList(1))
print('')
print(addToList(2.1))
print('')
print(addToList(2))
print('')
print(addToList(3))
print('')
print(addToList(1))
print('')
print(addToList("1"))
print('')
print(addToList(3))
print('')
print(addToList("1"))
print('')
print(addToList("2.1"))
