def count_words(text):

    words = text.split()
    return len(words)


print("Welcome to the Word Counter Program!")
print("Please enter a sentence or paragraph below.")

try:

    user_input = input("Enter your text: ")

 
    if not user_input.strip():
        print("Error: You entered an empty string. Please provide valid text.")
    else:
   
        word_count = count_words(user_input)
        print(f"\nWord Count: {word_count} words")

except Exception as e:

    print(f"An unexpected error occurred: {e}")
