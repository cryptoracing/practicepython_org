# Ask the user for input
user_input = input("Enter a string: ")

# Check if the input string is a palindrome
if user_input == user_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")