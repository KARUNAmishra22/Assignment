user_input=input ("Enter a string:")
#Initializing counters
letter_count=0
digit_count=0
for char in user_input:
    if char. isalpha(): #check if the character is letter
      letter_count+= 1
    elif char. isdigit (): #check if the character is digit
      digit_count+= 1
      print (f"Number of letters: {letter_count}")
      print (f"Number of digits: {digit_count}")