# Simulating Monopoly

written by W. H. Bell [ http://www.whbell.net/ ].  

This package contains a series of propability examples, building up from the probability of rolling one die, 
two dice, moving around the Monopoly board, adding the "Go To Jail" square and finally adding the two decks 
of cards.  The final simulation is not complete, but should yield a probability distribution function (PDF) close 
to the real PDF of the game.

The package contains:
  * doc/MonopolyWorksheet.pdf - a worksheet that introduces the concepts used in the simulation.
  * python/twoDice.py - a program to print the PDF for two dice.
  * python/boardOnly.py - a program that prints and plots the PDF for a board with 40 squares.
  * python/goToJail.py - a simulation of the "Go To Jail!" square.
  * python/twoDecksOfCards.py - a simulation that includes the "Go To Jail!" square and the two decks of cards.

The examples that plot the PDF use matplotlib.  This library can be installed on a debian based Linux system by typing

```
sudo apt-get install python-matplotlib 
```
