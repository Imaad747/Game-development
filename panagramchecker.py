import string

# Get user input
user_input = input("Enter a sentence: ")

# Convert to lowercase and create a set of its letters
sentence_set = set(user_input.lower())

# Create a set of all lowercase letters
alphabet_set = set(string.ascii_lowercase)

# Check if all alphabet letters are in the sentence set using a loop
is_pangram = True
for letter in alphabet_set:
    if letter not in sentence_set:
        is_pangram = False
        break

# Display result
if is_pangram:
    print("It's a pangram!")
else:
    print("It's not a pangram.")