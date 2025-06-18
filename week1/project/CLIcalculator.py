
def add(numbers):
    return sum(numbers)

def substract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
       result -= num
       return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def  divide(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
        return result 
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    

def power(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result =result  **  num
    return result



def calculator():
    print("CLI Calculator - Multi-Value Version")
    print("------------------------------------")


    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice not in ('1', '2', '3', '4', '5'):
            print("Invalid choice. Try again.")
            continue

        try:
            raw_input = input("Enter numbers separated by spaces: ")
            numbers = list(map(float, raw_input.split()))
            if len(numbers) < 2:
                print("Please enter at least two numbers.")
                continue
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            continue

        if choice == '1':
            result = add(numbers)
        elif choice == '2':
            result = substract(numbers)
        elif choice == '3':
            result = multiply(numbers)
        elif choice == '4':
            result = divide(numbers)
        elif choice == '5':
            result = power(numbers)

        print(f"Result: {result}")

if __name__ == "__main__":
    calculator()