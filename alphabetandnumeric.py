def inputAlphaOnly(name):
    while True:
        user_input = input(name)
        if user_input.isalpha():
            return user_input
        else:
            print("Ivalid input. please enter name only")
name = inputAlphaOnly("enter your name: ")
print(f"HEllo, {name}!")


def inputNumericOnly(number):
    while True:
        user_input = input(number)
        if user_input.isnumeric():
            return user_input
        else:
            print("Ivalid input. please enter number only")
number = inputNumericOnly("enter your number: ")
print(f"HEllo, {number}!")