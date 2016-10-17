#!/usr/bin/env python

# Import the random package
import random

# Import the matplotlib pyplot package
import matplotlib.pyplot as pyplot

# A function to generate two random numbers within the range 1 <= i <= 6 and add them together
def rollTwoDice():
  return random.randint(1,6) + random.randint(1,6)

#---------------------------

# A function to create a histogram
def plot(x, y):
  pyplot.bar(x, y)
  pyplot.show()

#---------------------------

# A function to normalise the counters by the sum of the counts
def normalise(counters):

  # Count the total number of entries
  total = 0.
  for counter in counters:
    total = total + counter

  # Divide each counter value by the total
  for i in range(len(counters)):
    counters[i] = counters[i] / total

#---------------------------

# The number of squares on the board
nsquares = 40

# A list to contain the total value rolled.
counters=[0.]*nsquares

# A variable to hold the current position
currentPosition = 0

# Set the number of rolls
nRolls = 1000000

# Print a message
print("Rolling two dice " + str(nRolls) + " times...")

# Roll the dice
for i in range(nRolls):
  # roll the dice
  totalValue = rollTwoDice()

  # Move the player to the next position
  currentPosition = currentPosition + totalValue

  # If the player has moved past the last square, wrap the board around.
  if currentPosition >= nsquares:
    currentPosition = currentPosition - nsquares

  # Count the current position on the board
  counters[currentPosition] = counters[currentPosition] + 1.

  # Check if the player should go to jail
  if currentPosition == 30:

    # Send them to the jail square
    currentPosition = 10

    # Count landing on the jail square
    counters[currentPosition] = counters[currentPosition] + 1.

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
