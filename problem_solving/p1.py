# 🔹 Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.
# Example:
# 🔹 Input: "hello"
# 🔹 Output: "olleh"
# 💡 Hint: Use Python's slicing feature.

def problem_1() :
    """ Reverse a String """
    # Function to reverse a string
    def reverse_string(s) -> str:
        """ Reverse the input string """
        return s[::-1]

    # Example usage
    input_string = input("Enter a string to reverse: ") # Example input: "hello"
    reversed_string = reverse_string(input_string) # Example output: "olleh"
    print(f"Input: {input_string}") 
    print(f"Output: {reversed_string}")

if __name__ == "__main__":
    problem_1()
    # Call the function to test it
    # problem_1()