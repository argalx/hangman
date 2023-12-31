# Game Initialization
from random import choice
from time import time

# Word and Hint lists
wordList = ["apple", "banana", "orange", "grape", "kiwi"]
wordHintList = {"apple": ["Name of a fruit", "Color red", "Adam & Eve ate this fruit"], "banana": ["Name of a fruit", "Color yellow", "Monkey's favorite"], "orange": ["Name of a fruit", "Color orange", "Popular juice flavor fruit"], "grape": ["Name of a fruit", "Color violet", "Can be fermented to create wine"], "kiwi": ["Name of a fruit", "Color brown", "Lemurs favorite"]}

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

# Initialize Chosen Word List Str
# Convert chosen word list to string
chosenWordHiddenStr = str(chosenWordHidden)
# List all string to be replaced from chosen word list string
chosenWordHiddenReplacement = [("[", ""), ("]", ""), ("'",""), (",", "")]

# Iterate each string from replacement list and proceed with the replacement for chosen word list
for char, rep in chosenWordHiddenReplacement:
    if char in chosenWordHiddenStr:
        chosenWordHiddenStr = chosenWordHiddenStr.replace(char, rep)

# Incorrect Attempts Up to 6
totalGameAttempt = 6
incorrectGuesses = 0
# Correct Attempts equals to chosen word length to complete the game
correctAttempt = len(chosenWord)

# For Logging
# print(chosenWord)
# print(len(chosenWord))
# print(chosenWordHidden)
# print(chosenWordHiddenStr)

# Game State
# Update the displayed word after each correct letter guess. - Complete
print("Welcome to Hangman!\nGuess the hidden word and win the game.\n6 incorrect guess attempts and you lose.")
print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))
# Word hint
print(f"Hint: {choice(wordHintList[chosenWord])}")

# Taking User Input
# Handle repeated guesses and provide appropriate feedback. - Complete
# while correctAttempt != 0:
while True:
    # Start time, restriction is 30 sec
    startTime = time()

    guess = input("Guess a letter: ").lower()

    # 30 Sec Timeout Rule
    elapsedTime = time() - startTime
    if elapsedTime > 30:
        print(f"Time's up! You ran out of time. The word was: {chosenWord}")
        # Play Again Option
        playAgain = input("Want to play again? (Y) Yes/ (N) No: ")
        if playAgain.lower() == "y":
            # Reset variables
            chosenWord = choice(wordList)
            chosenWordHidden = []
            for wordIndex in range(1, len(chosenWord)+1):
                chosenWordHidden.append("_")
            incorrectGuesses = 0
            correctAttempt = len(chosenWord)
            print("Welcome to Hangman!\nGuess the hidden word and win the game.\n6 incorrect guess attempts and you lose.")
            print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))
            # Word hint
            print(f"Hint: {choice(wordHintList[chosenWord])}")
            
        else:
            print("Thank you for playing!")
            break

    updateCounter = 1

    # Game Logic
    if guess.isalpha() and len(guess) == 1:

        # check if letter is repeated
        letterCounter = 0

        for repeatedLetterIndex, repeatedLetter in enumerate(chosenWord):
            if repeatedLetter == guess and chosenWordHidden[repeatedLetterIndex] == "_":
                letterCounter += 1

        # Check if guess letter is correct
        if guess in chosenWord and letterCounter > 0:

            # Check letter and index in chosen word
            for index, letter in enumerate(chosenWord):

                # Get index of guess letter from chosen word
                if letter == guess:

                    # Update chosen word hidden one time per guess based on current guess letter index
                    if updateCounter == 1 and chosenWordHidden[index] == "_":
                        chosenWordHidden[index] = guess
                        updateCounter -= 1
                        correctAttempt -= 1

            # Update the correct answer counter to 1
            updateCounter += 1
    
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
                print(f'Guess letter is correct.\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters.')
                # Word hint
                print(f"Hint: {choice(wordHintList[chosenWord])}")
            else:
                print(f'Guess letter is correct.\nThe word is: "{chosenWord}".')
        # Tracking Incorrect Attempts
        #  TODO Display the Hangman figure progressively for each incorrect guess.           
        else:
                incorrectGuesses += 1
                if incorrectGuesses == 1:
                    print(f'{hangman1}\n{totalGameAttempt - incorrectGuesses} attempt remaining!\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters.')
                    # Word hint
                    print(f"Hint: {choice(wordHintList[chosenWord])}")
                elif incorrectGuesses == 2:
                    print(f'{hangman2}\n{totalGameAttempt - incorrectGuesses} attempt remaining!\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters.')
                    # Word hint
                    print(f"Hint: {choice(wordHintList[chosenWord])}")
                elif incorrectGuesses == 3:
                    print(f'{hangman3}\n{totalGameAttempt - incorrectGuesses} attempt remaining!\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters.')
                    # Word hint
                    print(f"Hint: {choice(wordHintList[chosenWord])}")
                elif incorrectGuesses == 4:
                    print(f'{hangman4}\n{totalGameAttempt - incorrectGuesses} attempt remaining!\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters.')
                    # Word hint
                    print(f"Hint: {choice(wordHintList[chosenWord])}")
                elif incorrectGuesses == 5:
                    print(f'{hangman5}\n{totalGameAttempt - incorrectGuesses} attempt remaining!\nThe word has {len(chosenWord)} letters: "{chosenWordHiddenStr}" guess the remaining letters.')
                    # Word hint
                    print(f"Hint: {choice(wordHintList[chosenWord])}")
                else:
                    print(f"{hangman6}\nYou lose!")
    else:
        print("Invalid input. Please enter a single letter.")
    
    # Win/Lose Condition
    if correctAttempt == 0:
        print("Congratulations! You guessed the word.")
        # Play Again Option
        playAgain = input("Want to play again? (Y) Yes/ (N) No: ")
        if playAgain.lower() == "y":
            # Reset variables
            chosenWord = choice(wordList)
            chosenWordHidden = []
            for wordIndex in range(1, len(chosenWord)+1):
                chosenWordHidden.append("_")
            incorrectGuesses = 0
            correctAttempt = len(chosenWord)
            print("Welcome to Hangman!\nGuess the hidden word and win the game.\n6 incorrect guess attempts and you lose.")
            print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))
            # Word hint
            print(f"Hint: {choice(wordHintList[chosenWord])}")
        else:
            print("Thank you for playing!")
            break
    elif incorrectGuesses >= 6:
        print(f"Sorry, you ran out of attempts. The word was: {chosenWord}")
        # Play Again Option
        playAgain = input("Want to play again? (Y) Yes/ (N) No: ")
        if playAgain.lower() == "y":
            # Reset variables
            chosenWord = choice(wordList)
            chosenWordHidden = []
            for wordIndex in range(1, len(chosenWord)+1):
                chosenWordHidden.append("_")
            incorrectGuesses = 0
            correctAttempt = len(chosenWord)
            print("Welcome to Hangman!\nGuess the hidden word and win the game.\n6 incorrect guess attempts and you lose.")
            print("The word has", len(chosenWord), "letters: " + "_ " * len(chosenWord))
            # Word hint
            print(f"Hint: {choice(wordHintList[chosenWord])}")
        else:
            print("Thank you for playing!")
            break