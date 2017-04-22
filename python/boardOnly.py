#!/usr/bin/env python

# Import the random package
import random

# Import the matplotlib pyplot package
import matplotlib.pyplot as pyplot

def rollTwoDice():
  # Generate two random numbers within the range 1 <= i <= 6 and add them together
  return random.randint(1,6) + random.randint(1,6)

# A function to create a histogram
def plot(x, y):
  pyplot.bar(x, y)
  pyplot.xlabel('Monopoly board square (n)')
  pyplot.ylabel('Probability of landing on square P(n)')
  pyplot.show()

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

# Total probability is always defined as 1.
# Therefore, have to divide by the total number of counted values.
for i in range(len(counters)):
  counters[i] = counters[i] / float(nRolls)

# Now print out the probabilities for each of the combinations
print("The probabilities of landing on a given Monopoly square after " + str(nRolls) + " rolls")
for i in range(len(counters)):
  # Need to add one, since Python counts from zero.
  print(" P("+str(i)+")="+str(counters[i]))
print("where P(n) is the probability of landing on the nth Monopoly board square")

# Create a bar chart display
plot(range(len(counters)),counters)
