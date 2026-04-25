import time
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1/num2


def is_number_ok(text):
    try:
        float(text)
        return True
    except ValueError:
        return False


def check_if_arg2_is_zero():
        num2 = numbers[1]
        if num2 == 0:
            proper_number = input("Cannot divide by zero. Please enter a non-zero number:")
            while not is_number_ok(proper_number) or float(proper_number) == 0:
                proper_number = input("Cannot divide by zero. Please enter a non-zero number:")
            numbers[1] = float(proper_number)


def get_numbers_from_user(index):
    while True:
        num = input(f"Please enter number {index + 1}: ")
        if is_number_ok(num):
            return round(float(num), 2)
        else:
            print("That's not a valid number. Please try again.")


def get_operation_from_user():
    while True:
        choice = input("Pick an operation (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return operations[int(choice) - 1]
        else:
            print("Invalid choice. Please try again.")


def print_operations():    
    print("Available operations:")
    print("\n")
    for i, operation in enumerate(operations):
        print(f"{i +1}. {operation.__name__.capitalize()}")


def how_many_numbers():   
    while True:
        choice = input("How many numbers do you want to use? (2 or more): ")
        if choice.isdigit() and int(choice) >= 2:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number 2 or greater.")


operations = [
    add,
    subtract,
    multiply,
    divide,
]


numbers = []


def provide_anwser(operation, custom_amount):

    for i in range(custom_amount):
        num = get_numbers_from_user(i)
        numbers.append(num)

    if operation == divide:
        check_if_arg2_is_zero()

    answer = operation(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        answer = operation(answer, numbers[i])
    return answer


def show_user_summary(operation, answer):
    logging.info(f"{operation.__name__.capitalize()}ing Numbers: {' and '.join([f'{num:.2f}' for num in numbers])}")
    time.sleep(.5)
    print("\n")
    print(f"Result = {answer:.2f}")
    print("\n")


def calculator():
    should_repeat = True
    while should_repeat:

        print_operations()
        print("\n")

        operation = get_operation_from_user()

        if operation == add or operation == multiply:
            custom_amount = how_many_numbers()
            answer = provide_anwser(operation, custom_amount)

        elif operation == subtract or operation == divide:
            answer = provide_anwser(operation, 2)
            
        print("\n")
        show_user_summary(operation, answer)
        numbers.clear()
        
        choice = input("Continiue y/n:")

        if choice == "y":
            calculator()
        else:
             exit()


calculator()