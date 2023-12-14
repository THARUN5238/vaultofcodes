def print_squares(numbers):
    squares = [num ** 2 for num in numbers]
    return squares
if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [float(num) for num in user_input.split()]
    result = print_squares(numbers)
    print("Squares:", result)

