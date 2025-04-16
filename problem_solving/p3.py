# 🔹 Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns the sum of its digits.
# Example:
# 🔹 Input: 1234
# 🔹 Output: 10
# 💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.

def problem_3():
    """ Sum of Digits """
    def sum_of_digits(n) -> int:
        """ Convert the number to a string and iterate over each digit """
        if n == 0:
            return 0
        else:
            # return n % 10 + sum_of_digits(n // 10) # Using recursion
            # Using string conversion and sum function
            return sum(int(d) for d in str(n)) # Using a generator expression to sum the digits

    n = int(input("Enter a non-negative integer: "))
    digit_sum = sum_of_digits(n)
    print(f"Input: {n}")
    print(f"Output: {digit_sum}")

if __name__ == "__main__":
    problem_3()
    # Call the function to test it
    # problem_3()

#   d = 0
#   for digit in str(n):
#       d += int(digit) # Convert each character back to an integer and sum them up
#     return d
