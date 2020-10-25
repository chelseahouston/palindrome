# PROGRAM TO CHECK IF WORD IS PALINDROME

# WORD INPUT
word = input(str("Enter a word or number to see if it's a Palindrome: "))

# IS WORD SAME BACKWARDS AS FORWARDS:
# Make copy in reverse order
if word == word[::-1]:
  print(f"{word} is a Palindrome!")
else:
  print(f"{word} is not a Palindrome.")
