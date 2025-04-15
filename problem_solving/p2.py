# 🔹 Problem 2: Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
# Example:
# 🔹 Input: "Apple"
# 🔹 Output: 2
# 💡 Hint: Use a loop and check if each character is in a set of vowels.

def problem_2():
    """ Count Vowels in a String """
    def count_string(s):
        """ Count the number of vowels in a string"""
        vowels = 'aeiouaeiou'  # Define the vowels to check for
        # count = 0
        # for char in s:
        #     if char in set(vowels):  # Check if each character is in a set of vowels.
        #         count += 1
        # return count
        return sum(1 for char in s if char in set(vowels)) # Using a generator expression to count vowels
    
    # Example usage
    input_string = input("Enter a string to count vowels: ").lower()  # Example input: "Apple"
    vowel_count = count_string(input_string) # Example output: 2
    print(f"Input: {input_string}") # Example input: "apple"
    print(f"Output: {vowel_count}") # Example output: 2

if __name__ == "__main__": 
    problem_2()
    # Call the function to test it
    # problem_2()


 # (expression for item in iterable if condition)