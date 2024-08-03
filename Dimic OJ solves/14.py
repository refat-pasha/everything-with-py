

# Function to count the occurrences of a character in a sentence
def count_character_occurrences(sentence, char):
    count = sentence.count(char)
    return count


# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    sentence = input().strip()
    char = input().strip()

    count = count_character_occurrences(sentence, char)

    if count > 0:
        print(f"Occurrence of '{char}' in '{sentence}' = {count}")
    else:
        print(f"'{char}' is not present")

