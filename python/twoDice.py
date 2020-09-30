#!/usr/bin/env python3

# Import the random package
import random

def rollTwoDice():
  # Generate two random numbers within the range 1 <= i <= 6 and add them together
  return random.randint(1,6) + random.randint(1,6)


# A list to contain the total value rolled.
# There are 12 elements, because the total value that can be rolled is 12.
counters=[0.]*12

# Roll two dice 100 times.
nRolls = 100
for i in range(nRolls):
    totalValue = rollTwoDice()  # roll the dice

    # Python list indices count from zero.  Therefore, have to remove one from
    # the totalValue to put it into the right index in the list.
    counters[totalValue-1] = counters[totalValue-1] + 1. # count this total value

# Total probability is always defined as 1.
# Therefore, have to divide by the total number of counted values.
for i in range(len(counters)):
    counters[i] = counters[i] / float(nRolls)

# Now print out the probabilities for each of the combinations
print("The probabilities of rolling a total value using two dice:")
for i in range(len(counters)):
    # Need to add one, since Python counts from zero.
    print(" P("+str(i+1)+")="+str(counters[i]))
print("where P(n) is the probability of rolling a total of n on two dice.")
