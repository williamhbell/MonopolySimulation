#!/usr/bin/env python

# Import the random package
import random

# Import the matplotlib pyplot package
import matplotlib.pyplot as pyplot

# A function to generate two random numbers within the range 1 <= i <= 6 and add them together
def rollTwoDice():
  return random.randint(1,6) + random.randint(1,6)

#-------------------------------------------------

# A function to normalise the counters by the sum of the counts
def normalise(counters):

  # Count the total number of entries
  total = 0.
  for counter in counters:
    total = total + counter

  # Divide each counter value by the total
  for i in range(len(counters)):
    counters[i] = counters[i] / total

#-------------------------------------------------

# A function to create a histogram
def plot(x, y):
  pyplot.bar(x, y)
  pyplot.xlabel('Monopoly board square (n)')
  pyplot.ylabel('Probability of landing on square P(n)')
  pyplot.show()

#=================================================

# A class to describe a deck of cards
class Deck:
  def __init__(self, ncards, results):
    # Store the number of cards
    self.ncards = ncards

    # Initialise all cards to have no function
    self.cards = [ None ]*self.ncards

    # Check if the number of results is within range
    nresults = len(results)
    assert nresults <= self.ncards, "Error: to many card types for number of cards."

    # Set the moving cards to be at the front of the deck
    for i in range(nresults):
      self.cards[i] = results[i]

    # Set the next card to be drawn.
    self.nextCard = 0

  #-----------------------------------------------

  def shuffle(self):
    random.shuffle(self.cards)

  #-----------------------------------------------

  def draw(self):
    # Draw the current card
    card = self.cards[self.nextCard]

    # Step to the next place in the list, wrapping around if necessary.
    self.nextCard = self.nextCard + 1
    if self.nextCard >= self.ncards:
      self.nextCard = 0

    # Return the card
    return card

#=================================================

class MonopolySimulation:
  def __init__(self):

    # The position of the chance and community chest squares
    self.chance = [7, 22, 36]
    self.communityChest = [2, 17, 33]

    self.chanceDeck = None
    self.communityChestDeck = None
    self.createCardDecks()

    # The number of squares on the board
    self.nsquares = 40

    # A list to contain the total value rolled.
    self.counters=[0.]*self.nsquares

    # A variable to hold the current position
    self.currentPosition = 0

  #-----------------------------------------------

  # Build the card decks
  def createCardDecks(self):

    # Create two lists to hold possible results from picking a card
    chanceResults = []
    communityChestResults = []

    # These are all commands to go to a square
    chanceResults += [ (0, 0) ] # Advance to GO
    chanceResults += [ (0, 11) ] # Advance to Pall Mall
    chanceResults += [ (0, 10) ] # Go to Jail
    chanceResults += [ (0, 15) ] # Take a trip to Marylebone Station
    chanceResults += [ (0, 39) ] # Advance to Mayfair
    chanceResults += [ (0, 24) ] # Advance to Trafalgar square

    # This is an offset
    chanceResults += [ (1, -3) ] # Go back three spaces

    # Now create the deck of cards
    self.chanceDeck = Deck(16, chanceResults) # There are sixteen cards in the deck.
    self.chanceDeck.shuffle() # Call this once at the start of the game.

    # These are all commands to go to a square
    communityChestResults += [ (0, 0) ] # Advance to GO
    communityChestResults += [ (0, 10) ] # Go to Jail
    communityChestResults += [ (2, 0) ] # Pay 10 pounds or take a chance

    # Now create the deck of cards
    self.communityChestDeck = Deck(16, communityChestResults) # There are sixteen cards in the deck.
    self.communityChestDeck.shuffle() # Call this once at the start of the game.

  #-----------------------------------------------

  def movePlayer(self):
    # roll the dice
    totalValue = rollTwoDice()

    # Move the player to the next position
    self.currentPosition = self.currentPosition + totalValue

    # If the player has moved past the last square, wrap the board around.
    if self.currentPosition >= self.nsquares:
      self.currentPosition = self.currentPosition - self.nsquares

    # Check that the value is within range, to protect the list index limits.
    assert self.currentPosition >= 0 and self.currentPosition < self.nsquares, "Error: current position is out of range."

    # Count the current position on the board
    self.counters[self.currentPosition] = self.counters[self.currentPosition] + 1.

  #-----------------------------------------------

  def evaluateCard(self, card):
    # If the card does not move the player
    if card == None:
      return

    # The type of action and the setting that is associated with it
    (typeOfAction, setting) = card

    # A command to move to a square
    if typeOfAction == 0:
      self.currentPosition = setting
      self.counters[self.currentPosition] = self.counters[self.currentPosition] + 1.  # Count the current position
      return

    # A command to apply an offset
    elif typeOfAction == 1:
      self.currentPosition = self.currentPosition + setting
      self.counters[self.currentPosition] = self.counters[self.currentPosition] + 1.  # Count the current position
      return

    # A command to take a chance
    elif typeOfAction == 2:
      if random.random() > 0.5: # Player chooses chance 1/2 the time at random
        self.evaluateCard(self.chanceDeck.draw())
      return

    assert False, "Error: card action %d is out of range" % typeOfAction

  #-----------------------------------------------

  def checkAction(self):

    # Check if the player has landed on a chance square
    for i in self.chance:
      if i == self.currentPosition:
        self.evaluateCard(self.chanceDeck.draw())
        return

    # Check if the player has landed on a community chest square
    for i in self.communityChest:
      if i == self.currentPosition:
        self.evaluateCard(self.communityChestDeck.draw())
        return

    # Check if the player should go to jail
    if self.currentPosition == 20:
      self.currentPosition = 10 # Send them to the jail square
      self.counters[self.currentPosition] = self.counters[self.currentPosition] + 1.  # Count the current position
      return

  #-----------------------------------------------

  def play(self, nRolls):
    # Print a message
    print("Rolling two dice " + str(nRolls) + " times...")

    # Roll the dice
    for i in range(nRolls):
      # Move the player and count the square the player landed on
      self.movePlayer()

      # Check if the player has landed on an action square
      # If the player has landed on a square, then move them as necessary
      # and count the square that they land on.
      self.checkAction()

if __name__ == "__main__":
  # Set the number of rolls
  nRolls = 1000000
  m = MonopolySimulation()
  m.play(nRolls)
  counters = m.counters
  
  # Total probability is always defined as 1.
  # Therefore, have to divide by the total number of counted values.
  normalise(counters)
  
  # Now print out the probabilities for each of the combinations
  print("The probabilities of landing on a given Monopoly square after " + str(nRolls) + " rolls")
  for i in range(len(counters)):
    # Need to add one, since Python counts from zero.
    print(" P("+str(i)+")="+str(counters[i]))
  print("where P(n) is the probability of landing on the nth Monopoly board square")

  # Create a bar chart display
  plot(range(len(counters)),counters)
