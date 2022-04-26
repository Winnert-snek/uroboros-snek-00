# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# dev branch change json lols

def get_name1():
    first_name1 = input("Enter your first name: ")
    last_name1 = input("Enter your last name: ")
    return first_name1, last_name1

def print_hi(name1, name2):
    # Use a breakpoint in the code line below to debug your script.
    # name1 = first name
    # name2 = last name
    print(f'Hi, {name1} {name2}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
# conjecture: this passes the values to the variables in print_hi
# i should simply change the values below into variables that i ask the user for input on
# x pass to y ????
if __name__ == '__main__':
    first_name1, last_name1 = get_name1()
    print_hi(first_name1, last_name1)

# above values should be something sinple
# first_name1 , last_name1 , first_name2 , last_name2


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
