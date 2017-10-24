#8.8
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!


while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    else:
        print "You lose."
        guesses_left -= 1

"""
#8.7

import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

#8.6

count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

#8.5

count = 0

while count < 10: # Add a colon
    print count
    count += 1

#8.4

choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")


#8.3

num = 1

while num <=10:
    print num ** 2
    num += 1

#8.2
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

#8.1
count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count

while count <= 9:
    print "Hello, I am a while and count is", count
    count += 1

"""