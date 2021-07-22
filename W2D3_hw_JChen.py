'''
Building a Shopping Cart
You can use either lists or dictionaries. The program should have the following capabilities:

1) Takes in input
2) Stores user input into a dictionary or list
3) The User can add or delete items
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quiting the program, print out all items in the user's list
'''

def shoppingCart():
    groceryList = {}
    while True:
        answer = input("Would you like to add, remove, or view items from the shopping cart? [add/remove/view/quit] \n").lower()

        # check if user wants to add/remove/view/quit or invalid
        if answer == 'add':
            grocery = input("What would you like to add? Enter singular name. Not case sensitive. \n").title()
            if grocery in groceryList:  # if input grocery exists, then +1 quantity. Otherwise, create a new key for that grocery.
                groceryList[grocery] += 1
            else:
                groceryList[grocery] = 1
        elif answer == 'remove':
            print(f'current grocery list is: {groceryList}')
            grocery = input("What would you like to remove? Enter singular name. Not case sensitive. \n").title()
            if (grocery in groceryList) and (groceryList[grocery] > 1):  #if input grocery exists, then -1 quantity. Otherwise, delete grocery key.
                groceryList[grocery] -= 1
            else:
                del groceryList[grocery]
        elif answer == 'view':
            print(f'current grocery list is: {groceryList}')
        elif answer == 'quit':
            print(f'current grocery list is: {groceryList}')
            break
        else:
            print("Invalid input, please type in add/remove/view/quit. \n")


shoppingCart()




'''
Create a Module in VS Code and import it into Jupyter Notebook
Module should have the following capabilities:

1) Has a function to calculate the square footage of a house
Reminder of Formula: Length X Width == Area

2) Has a function to calculate the circumference of a circle

Program in Jupyter Notebook should take in user input and use imported functions
to calculate a circle's circumference or a houses square footage
'''

import W2D3_hw_module_JChen

l = 10
w = 10
print(W2D3_hw_module_JChen.sqr_ft(l,w))

r = 5
print(W2D3_hw_module_JChen.circumference(r))