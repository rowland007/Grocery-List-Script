"""
Program:		Grocery List
Author:			Randall Rowland
Class:			IT-140-Q3788 Introduction to Scripting 18EW3
Instructor:		Angel D. Cross
Date:			29 Jan 2018
Description:    The task for this project is to create a very 
                simple grocery list script. This script also 
                emphasizes the importance of using lists, dictionaries 
                and loop types within your script and how the use 
                of those functions shapes your approach in creating a 
                script.

Input:          stdin
Output:         stdout
Known bugs/missing features:
                When accessing the dicitonary values in the list it generates
                a 1 keyerror no matter the list size.  It still does the calulations.
                Caught the keyerror exception and ignored it.
    
Modifications:
Date                Comment
----    ------------------------------------------------
"""

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

# Task: Create the empty data structure
grocery_item = {}               # Rubric inject: Create a dictionary

grocery_history = grocery_item  # Rubric inject: Create a list
x = 0
# Variable used to check if the while loop condition is met
isStopped = False

while not isStopped :           # Rubric inject: a while loop

    # Accept raw_input of the name of the grocery item purchased.
    itemName = raw_input('Item name:\n')
    # Accept input of the quantity of the grocery item purchased.
    quantity = raw_input('Quantity purchased:\n')
    # Accept input of the cost of the grocery item input (this is a per-item cost).
    cost = raw_input('Price per item:\n')
    # Create a dictionary entry which contains the name, number and price entered by the user.
    grocery_item['name'] = itemName         # Rubric inject: Adding key-value pairs
    grocery_item['number'] = int(quantity)  # Rubric inject: Adding key-value pair
    grocery_item['price'] = float(cost)     # Rubric inject: Adding key-value pair
    # Add the grocery_item to the grocery_history list using the append function
    grocery_history[x] = grocery_item.copy()    # Rubric inject: Adding data to a list
    # Accept input from the user asking if they have finished entering grocery items.
    exit = raw_input('Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')
    if exit == 'q':
        isStopped = True
    else:
        x += 1

# Define variable to hold grand total
grandTotal = float(0.00)


for z in range(0, len(grocery_history) - 1):    # Rubric inject: index-based range loop
  
    # The following code generates a keyerror after calculations are complete. 
    # Caught the exception to ignore it for now and allow the script to continue to run.
    try:
        # Calculate the total cost for the grocery_item
        # Rubric inject: Accessing values in a list | accessing values using keys
        itemTotal = int(grocery_history[z].get('number')) * float(grocery_history[z].get('price'))
    except KeyError:
        ignoreThis = 10
    # Add the item_total to the grand_total
    grandTotal += float(itemTotal)
    try:
        # Rubric inject: Accessing values in a list | accessing values using keys
        print(str(grocery_history[z]['number']) + ' ' + str(grocery_history[z]['name']) + ' @ $' + str('%.2f' % grocery_history[z]['price']) + ' ea $' + str('%.2f' % itemTotal))
    except KeyError:
        ignoreThis = 10
  
    # Reset item_total 
    itemTotal = 0

# Print the grand total
print(str('Grand total: $%.2f' % grandTotal))