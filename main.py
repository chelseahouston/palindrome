# PROGRAM TO CHECK IF WORD IS PALINDROME ---

def palindrome():
# WORD INPUT ---
  word = input(str("Enter a word or number to see if it's a Palindrome: "))

# IS WORD SAME BACKWARDS AS FORWARDS ---
# Make copy in reverse order ---
  if word == word[::-1]:
    print(f"{word} is a Palindrome!")
  else:
    print(f"{word} is not a Palindrome.")
  
# RUN AGAIN? ---
def run():
  while True:
    runagain = input("Run again? (Y/N): ").upper()
    if runagain not in ('Y', 'N'):
      print("Invalid Input.")
      run()
      break
    if runagain == 'Y':
      palindrome()
      run()
      break
    else:
      print("Have a good day.")
      break

palindrome()
run()
