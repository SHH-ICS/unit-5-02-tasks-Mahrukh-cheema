# String functions
# This program changes lowercase letters to uppercase
# ICS2O Unit 5, Activity 1
# Created by R. Kuzmochka
# Edited by K. Spindler

# Variables
wordsUpper = ""

# Input
wordsInput = input("Enter a line of text:  ")

# Processing
for i in range (0, len(wordsInput)):

    # User may give a mix of lower and uppercase, this variable will hold
    # 32 when the character is lowercase, and 0 when it is uppercase
    lowerToUpper = 0

    #get the ascii code for the current letter
    asciiNumber = ord(wordsInput[i])

    # If the ASCII value of the letter is greater than 96
    # but less within the range of lowercase letters (97-122)
    if asciiNumber > 96 and asciiNumber < 123:
        # then lowerToUpper will be set to the difference between
        # the value of an uppercase letter and the lowercase letter
        lowerToUpper = 32
    # Adds each letter to the string, shifting the ascii value if needed
    wordsUpper = wordsUpper + chr(asciiNumber - lowerToUpper)

# Output
print ("The inputted text in capitals is: ", wordsUpper)
