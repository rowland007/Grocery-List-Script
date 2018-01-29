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

#Task: Create the empty data structure
grocery_item = {}

grocery_history = []

#Variable used to check if the while loop condition is met
isStopped = False

while not isStopped :

    #Accept input of the name of the grocery item purchased.
    itemName = raw_input('Item name:\n')
    #Accept input of the quantity of the grocery item purchased.
    quantity = raw_input('Quantity purchased\n')
    #Accept input of the cost of the grocery item input (this is a per-item cost).
    cost = raw_input('Price per item\n')
    #Create a dictionary entry which contains the name, number and price entered by the user.
    grocery_item.append({'name': itemName, 'number': int(quantity), 'price': float(cost)})
    #Add the grocery_item to the grocery_history list using the append function
    grocery_history.append(grocery_item)
    #Accept input from the user asking if they have finished entering grocery items.
    exit = raw_input('Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')
    if exit == 'q':
      isStopped = True

# Define variable to hold grand total called 'grand_total'
grand_total = float(0.00)
#Define a 'for' loop.  

for name in grocery_history.iteritems():
  
  #Calculate the total cost for the grocery_item.
  float(itemTotal) = int(grocery_history.number()) * float(grocery_history.price())
  #Add the item_total to the grand_total
  float(grandTotal) += float(itemTotal)
  #Output the information for the grocery item to match this example:
  #2 apple	@	$1.49	ea	$2.98
  print(str(grocery_history.number()) + ' ' + str(grocery_history.name()) + ' @ $' + str('%.2f' % grocery_history.price()) + ' ea  ' + itemTotal + '\n')
  
  #Set the item_total equal to 0
  itemTotal = 0
#Print the grand total
print(str('Grand total: $%.2f' % grandTotal))
