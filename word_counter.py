# Simple Python program to count the number of words in a given sentence or paragraph

def count_words(text):
    """
    Function to count the number of words in the given text.
    A word is defined as any sequence of characters separated by whitespace.
    """
    # Split the text into words using whitespace and return the length of the list
    words = text.split()
    return len(words)

# User-friendly interface
print("Welcome to the Word Counter Program!")
print("Please enter a sentence or paragraph below.")

try:
    # Prompt user for input
    user_input = input("Enter your text: ")

    # Check if the input is empty
    if not user_input.strip():
        print("Error: You entered an empty string. Please provide valid text.")
    else:
        # Count the words and display the result
        word_count = count_words(user_input)
        print(f"\nWord Count: {word_count} words")

except Exception as e:
    # Handle unexpected errors
    print(f"An unexpected error occurred: {e}")