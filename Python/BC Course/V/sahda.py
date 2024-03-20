def count_letters(string):
  """Counts the occurrences of all letters (uppercase and lowercase) in a string.

  Args:
      string: The input string (str).
  """

  # Create a dictionary to store letter counts
  letter_counts = {}
  for char in string:
    if char.isalpha():  # Check for alphabetic characters only
      letter = char.lower()  # Convert to lowercase for case-insensitive counting
      letter_counts[letter] = letter_counts.get(letter, 0) + 1  # Count occurrences

  # Print letter occurrences
  for letter, count in letter_counts.items():
    print(f"{letter.upper()} : {count}")  # Print letter in uppercase

# Count and print letter occurrences
count_letters(text)