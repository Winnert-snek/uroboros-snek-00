# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Added get_name1() function, room for scaling up


# do i need to scrub the inputs? how does that work from a security standpoint?
import random


def get_name1():
    first_name1 = input("Enter your first name: ")
    last_name1 = input("Enter your last name: ")
    return first_name1, last_name1


# might be nice to do two sets of inputs, like hello sailor, vs hello scrub, or something.
# maybe have the user select sr. or ma'am or they or them. maybe a moniker
def random_greeting():
    greetings = ["hi", "hello", "hullo", "sup?", "suh", "what it do?", "y u alone tho?", "wat dat mouf do",
                "good day", "say", "bonjour", "salut", "buenos dias", "what up", "what up ya rat bastard",
                "how's it hanging?", "where ya been?", "hello there", "general", "commander",
                "hit me with your monday milk", "aloha"]
    #random.choice(greetings) pulls a random item from the greetings list then the return applies that value to the name
    #the return pushes the random choice back to the top for the next function to call it
    return random.choice(greetings)

def print_hi(name1, name2):
    # Use a breakpoint in the code line below to debug your script.
    # name1 = first name
    # name2 = last name
    # i don't know what the f' does
    print(f'{random_greeting()}, {name1} {name2}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# conjecture: this passes the values to the variables in print_hi
# i should simply change the values below into variables that i ask the user for input on
# x pass to y ????
if __name__ == '__main__':
    first_name1, last_name1 = get_name1()
    print_hi(first_name1, last_name1)

# above values should be something simple
# first_name1 , last_name1 , first_name2 , last_name2


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
