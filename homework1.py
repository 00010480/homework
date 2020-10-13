def example1(name, isStudent=True):
    print("Hello", name, "nice to meet you!")


def example2():
    example1('Student')

    example1(10480)

    example1(True, True)


# So when we declare like global variable we can get value from anywhere in your script file
id = 10480


def example3():
    print('Your', id)

name = 'WIUT'
# But when we declare like local variable you can get it only from your function.
def example4(name):
    print(name)


# When we use the same name for global variable and local, global variable will be ovveride with local

def example5():
    example4(name=name)

def main():

    example1('BIS', True)

    example2()

    example3()

    example4('WIUT')

    example5()

main()