# Game Initialization
from random import choice
from time import time

# Word List
wordList = ["apple", "banana", "orange", "grape", "kiwi"]

# Hangman Drawing
hangman6 = "  _______\n |       |\nx.x      |\n/|\\      |\n |       |\n/ \\      |\n         |"
hangman5 = "  _______\n |       |\no.o      |\n/|\\      |\n |       |\n/ \\      |\n         "
hangman4 = "  _______\n |       |\nT.T      |\n/|\\      |\n |       \n/ \\      \n         "
hangman3 = "  _______\n |       |\n-.-      \n/|\\      \n |       \n/ \\      \n         "
hangman2 = "  _______\n |       \nOwO       \n/|\\      \n |       \n/ \\      \n         "
hangman1 = "  \n |       \nUwU       \n/|\\      \n |       \n/ \\      \n         "

# Chosen Word Hidden List which contains _
chosenWordHidden = []

# Random Chosen Word
chosenWord = choice(wordList)

# Fill random word with _
for wordIndex in range(1, len(chosenWord)+1):
    chosenWordHidden.append("_")

# Incorrect Attempts Up to 6
incorrectGuesses = 0
# Correct Attempts equals to chosen word length to complete the game
correctAttempt = len(chosenWord)

# For Logging
# print(chosenWord)
# print(len(chosenWord))
# print(chosenWordHidden)
# print(chosenWordHiddenStr)

# Game State
# TODO Update the displayed word after each correct letter guess. - Complete
print("Welcome to Hangman!")
print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))

# Taking User Input
# TODO Handle repeated guesses and provide appropriate feedback. - Complete
# while correctAttempt != 0:
while True:
    # Start time, restriction is 30 sec
    startTime = time()

    guess = input("Guess a letter: ").lower()

    # 30 Sec Timeout Rule
    elapsedTime = time() - startTime
    if elapsedTime > 30:
        print("Time's up! You ran out of time.")
        break

    guessList = []
    updateCounter = 1

    if guess.isalpha() and len(guess) == 1:
        # Check if guess letter is correct
        if guess in chosenWord:
            # Check letter and index in chosen word
            for index, letter in enumerate(chosenWord):

                # Get index of guess letter from chosen word
                if letter == guess:

                    # Update chosen word hidden one time per guess based on current guess letter index
                    if updateCounter == 1 and chosenWordHidden[index] == "_":
                        chosenWordHidden[index] = guess
                        updateCounter -= 1

            # Update the correct answer counter to 1
            updateCounter += 1
            correctAttempt -= 1
            # Convert chosen word list to string
            chosenWordHiddenStr = str(chosenWordHidden)
            # List all string to be replaced from chosen word list string
            chosenWordHiddenReplacement = [("[", ""), ("]", ""), ("'",""), (",", "")]

            # Iterate each string from replacement list and proceed with the replacement for chosen word list
            for char, rep in chosenWordHiddenReplacement:
                if char in chosenWordHiddenStr:
                    chosenWordHiddenStr = chosenWordHiddenStr.replace(char, rep)
                
            # In-Game Output, Check the letter guess status and display appropriate message
            if "_" in chosenWordHiddenStr:
                print(f'Guess letter is corret UwU\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters OwO')
            else:
                print(f'Guess letter is corret UwU\nThe word is: "{chosenWordHiddenStr}" <3')
        # Tracking Incorrect Attempts
        #  TODO Display the Hangman figure progressively for each incorrect guess.           
        elif guess not in chosenWord:
                incorrectGuesses += 1
                if incorrectGuesses == 1:
                    print(hangman1)
                elif incorrectGuesses == 2:
                    print(hangman2)
                elif incorrectGuesses == 3:
                    print(hangman3)
                elif incorrectGuesses == 4:
                    print(hangman4)
                elif incorrectGuesses == 5:
                    print(hangman5)
                else:
                    print(hangman6)
    else:
        print("Invalid input. Please enter a single letter.")
    
    # Win/Lose Condition
    if correctAttempt == 0:
        print("Congratulations! You guessed the word")
        # Play Again Option
        playAgain = input("Want to play this shitty game again? Yes/No: ")
        if playAgain.lower() == "yes":
            # Reset variables
            chosenWord = choice(wordList)
            chosenWordHidden = []
            for wordIndex in range(1, len(chosenWord)+1):
                chosenWordHidden.append("_")
            incorrectGuesses = 0
            correctAttempt = len(chosenWord)
            print("Welcome to Hangman!")
            print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))
        else:
            print("Thank you for playing, I hope I don't see you again")
            break
    elif incorrectGuesses >= 6:
        print(f"Sorry, you ran out of attempts. The word was:{chosenWord}")
        # Play Again Option
        playAgain = input("Want to play this shitty game again? Yes/No: ")
        if playAgain.lower() == "yes":
            # Reset variables
            chosenWord = choice(wordList)
            chosenWordHidden = []
            for wordIndex in range(1, len(chosenWord)+1):
                chosenWordHidden.append("_")
            incorrectGuesses = 0
            correctAttempt = len(chosenWord)
            print("Welcome to Hangman!")
            print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))
        else:
            print("Thank you for playing, I hope I don't see you again")
            break