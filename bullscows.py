#! /usr/bin/python
import random
answer = random.sample(range(0,9), 4)
guess = []
while (answer != guess):
  guess = []
  bulls = 0
  cows = 0
  raw_guess = raw_input("guess!")
  for number in raw_guess:
    guess.append(int(number))
  for i in range(len(guess)):
    if guess[i] == answer[i]:
      bulls = bulls + 1
    elif guess[i] in answer:
      cows = cows + 1
  print "BULLS: " + str(bulls)
  print "COWS: " + str(cows)  
print "You win!"
    
  
