"""
Welcome to Mini Games! Enjoy playing (or reviewing) my code below, showcasing 4 lightweight and simple coded games.
Developed by Julianne McMillian
"""

###Introduction. Here the player will enter their name, once entered it cannot be changed unless you restart the program.
print("Welcome to Mini Games! What's your name? ")
playerName = input()



"""Functions are used to keep the main code short and easy to read."""

###Creation of the Main Menu. This welcomes the player and provides game options.
def mainMenu():
    print("\nHello, " + playerName + "! What would you like to do today?")
    print("1.) Years to 100\n2.) Odd or Even\n3.) Guessing Game\n4.) Max of 3\n5.) Exit")

###This function creates the Years to 100 game.
def yearsTo100Game():
    print("How old are you " + playerName + "? ", end="") ###The prompt asks the player to provide their age.

    playerAge = int(input()) ###The players age is converted into type int so it can be subtracted by 100 to give results.
    yearsTo100 = 100 - playerAge
    print("Wow, " + playerName + "! In", yearsTo100, "years you will be 100!\n")###Output of calculated number of years until the player turns 100.

    print("Press any letter to continue playing \'Years to 100\' or press Q to quit.")###Player can press any button, besides q or Q to continue playing. Pressing returns the player to the Main Menu.
    global playAgain
    playAgain = input()
    if playAgain == 'q':
        return

###This function creats the Odd or Even game.
def oddOrEvenGame():
    playerNumber = int(input(str("Enter any number 1-10:")))###Player inputs any number as long as the value is between 1 and 10, and is a whole number.

    print(playerNumber)###Outputs playerNumber

    if playerNumber in range(2, 11, 2):###2, 4, 6, 8, 10
        print('Even')###If playerNumber is within 2-11 (non-inclusize), skipping every other number, it is even.
    elif playerNumber in range(1, 10, 2):###1, 3, 5, 7, 9
        print('Odd')###Starting with 1 and skipping every other number, if playersNumber is equal to a number in this range it is odd.

    print("Press any letter to continue playing \'Odd or Even\' or press Q to quit.")###Player can press any button, besides q or Q to continue playing. Pressing returns the player to the Main Menu.
    global playAgain
    playAgain = input()
    if playAgain == 'q':
        return

###Creation of Guessing Game
def guessingGameGAME():
    import random
    randomNumber = random.randint(1, 10)###Imports random numbers 1-10, randomNumber chooses generated number.

    playersNumber = int(input("Pick a number 1-10: "))###Player inputs a number 1-10, which is converted into an integer.
    print("Your number is:", playersNumber)

    if playersNumber == randomNumber:###If playersNumber is equal to randomNumber, message is displayed.
        print("We got a match! My number was ", randomNumber, " too!")

    elif playersNumber != randomNumber:###If playersNumber is not equal to randomNumber, a different message is displayed.
        print("I guessed incorrectly, my number was ", randomNumber)

    print("Press any letter to continue playing \'Guessing Game\' or press Q to quit.")###Player can press any button, besides q or Q to continue playing. Pressing returns the player to the Main Menu.
    global playAgain
    playAgain = input()
    if playAgain == 'q':
        return

###Created function of Max of 3 game
def maxOf3():
    print("Give me 3 Numbers ")###Program prompts the user to input 3 numbers, on 3 separate lines.
    x = int(input("First Number: "))
    y = int(input("Second Number: "))
    z = int(input("Third Number: "))

    if x > (y or z):###If the value in x is greater than the values in y or z, x will be printed as the highest number.
        print("\nThe 1st number was the highest")
    elif y > (z or x):###If the value in y is greater than the values in x or z, y will be printed as the highest number.
        print("\nThe 2nd number was the highest")
    else:###If the value in z is greater than the values in y or x, z will be printed as the highest number.
        print("\nThe 3rd number was the highest")

    print("Press any letter to continue playing \'Max of 3\' or press Q to quit.")###Player can press any button, besides q or Q to continue playing. Pressing returns the player to the Main Menu.
    global playAgain
    playAgain = input()
    if playAgain == 'q':
        return


""""######        MAIN CODE        ######"""

while True:
    mainMenu()###Trigger Main Menu function
    userInput = input()###Wait for users input

    if userInput == '1':###If users input is '1', it will prompt the Years to 100 game to start.
        #Years to 100
        yearsTo100Game()
        while playAgain != 'q': ###If user has not pressed 'q' or 'Q', the current game will continue playing
            yearsTo100Game()

            if playAgain == 'q':###If user has entered 'q' or 'Q', and will be taken back to the Main Menu
                continue


    elif userInput == '2':###If users input is '2', it will prompt the Odd or Even game to start.
        #Odd or Even
        oddOrEvenGame()
        while playAgain != 'q':###If user has not pressed 'q' or 'Q', the current game will continue playing
            oddOrEvenGame()

            if playAgain == 'q':###If user has entered 'q' or 'Q', and will be taken back to the Main Menu
                continue


    elif userInput == '3':###If users input is '3', it will prompt the Guessing game to start.
        #Guessing Game
        guessingGameGAME()
        while playAgain != 'q':###If user has not pressed 'q' or 'Q', the current game will continue playing
            guessingGameGAME()

            if playAgain == 'q':###If user has entered 'q' or 'Q', and will be taken back to the Main Menu
                continue

    elif userInput == '4':###If users input is '4', it will prompt the Max of 3 game to start.
        #MaxOf3
        maxOf3()
        while playAgain != 'q':###If user has not pressed 'q' or 'Q', the current game will continue playing
            maxOf3()

            if playAgain == 'q':###If user has entered 'q' or 'Q', and will be taken back to the Main Menu
                continue


    elif userInput == '5':###If users input is '5', it will quit the program
        exit()
