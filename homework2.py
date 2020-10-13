def new_line():

    print('*')

def three_lines():

    new_line()

    new_line()

    new_line()

def nine_lines():
    for line in range(3):
        three_lines()

def clear_screen():
    for line in range(2):
        nine_lines()
    for line in range(2):
        three_lines()
    for line in range(1):
        new_line()

clear_screen()