def count_characters(string):
    # Create a dictionary to count occurrences of each character
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Sort the dictionary keys alphabetically
    sorted_chars = sorted(char_count.keys())

    # Print the characters and their counts in the required format
    for char in sorted_chars:
        print(f"{char} = {char_count[char]}")

    # Print a blank line between test cases
    print()


# Read the number of test cases
T = int(input().strip())

# Process each test case
for _ in range(T):
    string = input().strip()
    count_characters(string)
