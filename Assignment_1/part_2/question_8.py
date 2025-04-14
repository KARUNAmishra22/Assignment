import random 
 # Generate a random number between 1 and 100
answer = random. randint (1, 100)
print ("Welcome to the Number Guessing Game!")
print ("You have 5 attempts to guess the correct number between 1 and 100.")
# Allow the user to guess up to 5 times
attempts = 5
for i in range(attempts):
# Prompt the user for a number input
  guess= int (input(f"Attempt {i+1}: Enter your guess: "))
 # Check if the guess is correct, too high, or too low
  if guess == answer:
     print (" Congratulations! You guessed the correct number!")
     break # Exit the loop since the correct number is guessed
  elif guess < answer:
     print("Too low! Try again.")
else:
    print("Too high! Try again.")

# If it's the last attempt and the user hasn't guessed correctly
if i == attempts - 1:
    print(f"Game Over! The correct number was {answer}.")