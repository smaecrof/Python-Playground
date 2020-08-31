# Author: Spencer Mae-Croft 
# Date: 08/31/2020


def display_message():
    print("Today seems like a good day to compute")


def favorite_book(readersName, bookTitle): 
    print(readersName + "'s favorite book is " + bookTitle) 


def make_shirt(text, size="Large"):
    print("The shirt will be size: " + size + ' and will say "' + text + '"')

display_message()
favorite_book("Spencer", "Atlas Shrugged")
make_shirt("large", "Nike")
make_shirt(size="small", text="Gym Shark")













