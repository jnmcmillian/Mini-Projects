"""Welcome to Hangman! Enjoy the game!
    Developed by Julianne McMillian"""

import random  #allows the program to randomly select a word from the list

print("Welcome to Hangman, can you guess my word?")  #Introduction of the Game

#A list of words is created, feel free to add more words if you want!
words = ['Challenge', 'Awesome', 'Red', 'Orange', 'Fish', 'Blue', 'Cat', 'Pink', 'Dog', 'Whale', 'Shoe',
        'Television', 'Anteater', 'Worm', 'Cool', 'Python', 'Game', 'Entertainment', 'Skill', 'Friend',
        'Learning', 'Improvement', 'Skate', 'Baseball', 'Cookie', 'Cake', 'Mall', 'House', 'Rabbit',
        'America', 'President', 'Coding', 'Sleep', 'Computer', 'Midnight', 'Jazz', 'Bed', 'Mirror']

word = random.choice(words)  #A word from the list "words" is chosen at random, 'import random' is needed in order to complete this task.
word = word.casefold()  #The word chosen from the list has it's captialization ignored, therefore the player does not have to guess upper and lowercase letters.

guesses = ''  #Stores players guesses
attempts = 6  #Number of attempts the player has, attempts are only used and displayed if the player guesses incorrectly.

while attempts > 0:  #While the number of attempts are greater than 0, the game will continue to run, and the player can keep guessing.
    failed_guess = 0 #The number of times the player guesses incorrectly will be kept by this variable.

    for char in word:  #All characters in the chosen word will be represented by '_' unless correctly guessedby the player.
        if char in guesses:  #If player guesses a letter correctly, all '_' containing that letter will be replaced by said letter.
            print(char, end=' ')

        else:
            print("_", end=' ')  #If player incorrectly guesses a letter from the chosen word, failed_guess will increase by one, and
            failed_guess += 1   #attempts will decrease by 1. Any unguessed letters will remain as '_' unless the game is over.

    if failed_guess == 0:  #The player will win the game is failure is 0, and all characters are guessed correctly within allowed attempts
        print("\n\nGreat job! You guessed my word! My word was \"" + word.capitalize() + "\".")
        break

    print()
    guess = input("Guess a character: ")  #Prompts a user to guess a character
    guess = guess.casefold()  #Ignore any capitalization from the players input

    guesses += guess  #Input characters will be stored in 'guesses'

    if guess not in word:
        attempts -= 1  #If players guess was not found in the chosen word, attempts will decrement by 1.

        print("\nOops, thats wrong, try again. You have ", attempts, " tries left.")  #Outputs that the player guessed incorrectly, and displays how many attempts are left

        if attempts == 0:  #If the player runs out of attempts, the game is over and the word is displayed.
            print("GAME OVER! My word was \"" + word.capitalize() + "\". Let's play again.")
