from textwrap import dedent
def intro():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
""")


def order():
    print(dedent("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """))
    order_dict = {}
    ask_again= True
    while ask_again:
        choice = input("> ")
        if choice in order_dict:
            order_dict[choice] += 1
        else:
            order_dict[choice] = 1
        for key in order_dict:
            if choice != "quit":
                print(f"*{order_dict[key]} orders of {key}*")
        if choice == "quit":
                print("Thanks for checking us out, come back soon!")
                break
if __name__=="__main__":
    intro()
    order()