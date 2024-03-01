"""
    Welcome to 21 Blackjack! In 21 Blackjack, the goal is to get as close to '21' as possible without going over.
        Developed by Julianne McMillian
"""
import random  #Loads the random module, allowing the program to pick from the "Deck of Cards"

sweetSpot = 21  #'sweetSpot' is set to '21' as a marker when comparing deck values
deckOfCards = ['1', '2', '3', '4', '5', '6', '7', '9', '9', '10', '10', '10', '11']  #Here is the 'Deck of Cards'. Jacks, Kings, and Queens are given values of 10. Aces are values of 1 or 11.

firstCard = random.choice(deckOfCards)  #Selection of the first card for players hand
secondCard = random.choice(deckOfCards)  #Selection of the second card for players hand

initial_cards = int(firstCard) + int(secondCard)  #This is the value of both first and second cards
print("First card: ", firstCard)  #Prints value of first card
print("Second card: ", secondCard)  #Prints value of second card
print("The value of your hand is ",  initial_cards)  #Total value of the cards in the players hand
computersTurn = 0 #Computers turn is initialized to 0.
computerHandValue = 0  #The value of the computers hand is initialized to 0

###"Other Players" generation of initial_cards
while computersTurn < 3:  #Computer will have 3 turns, not seen by the player, to generate a final value.
    computersHit = random.choice(deckOfCards)  #While 'computersTurn' is less than 3, 'computersHit' will randomly choose an element from the deck of cards
    computerHandValue += int(computersHit)     #the element chosen from the deck will be converted into an integer and added to 'computerHandValue', then
    computersTurn += 1                         #'computersTurn' will increment by 1.

while True:
    print("\nWould you like to hit or stand?")  #The game will prompt the user to pick from two options
    print("[1] Hit\n[2] Stand")
    hit_or_stand = input()  #Waits for users input

    if hit_or_stand == '1':#Pressing '1' will cause the player to 'Hit' or accept another card.

        hit = random.choice(deckOfCards)  #'hit' is the variable that selects the next 'card' from the deck
        print("Your next card is ",  hit)  #Displays the value of the next 'card'

        newValue = int(hit) + initial_cards  #The new value of the players hand is created by adding the values of 'initial_cards' and 'hit'
        initial_cards = newValue  #The contents of 'initial_cards' is changed to 'newValue' in order to include the players hit.
        print("\n\nThe value of your hand is ",  newValue)  #Displays the value of the players hand, but not individual 'card' amounts

        if newValue > sweetSpot:  #If the player chooses the 'Hit' option, and the players hand surpasses '21', it is counted as an automatic loss.
            print("You Lose!")
            break  #Ends the game after outputing 'You Lose!'

    elif hit_or_stand == '2':#Pressing '2' will cause the player to 'Stand', not taking any cards, and prompting results.
        newValue = initial_cards      #'newValue' will depend on if the player hits first or not.
        print("You chose to stand.")
        print("The value of your hand is ", newValue, "\nThe value of the other players hand is", computerHandValue)  #Displays player and computer values

        if computerHandValue < newValue:  #If the if players value is greater than the computers value but less the 21, the player wins
            print("You win!")
        elif computerHandValue > sweetSpot:  #If the computers value is greater than 21 the player wins, regardless of hand value
            print("You Win!")
        elif newValue < computerHandValue:  #If the computers value is closer to 21, the computer or "Other player" wins
            print("You lose!")
        elif newValue == computerHandValue:  #If both the computer and player have the same number, its a tie
            print("Its a tie!")

        break  #Ends the game after declaring a winner
