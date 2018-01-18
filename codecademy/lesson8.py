



grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def grades_sum(x):
    scores = 0
    for i in x:
        scores = scores + i
    return scores

def grades_average(grades_input):
    return grades_sum(grades_input) / float(len(grades_input))


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

def grades_std_deviation(variance):
    return variance ** 0.5

print grades_variance(grades)




def print_grades(grades_input):
    for i in grades_input:
        print i

def median(x):
    b = sorted(x)
    if len(b) % 2 == 0:
        print (b[(len(b) / 2) - 1] + b[(len(b) / 2)]) / 2.0
    else:
        print b[(len(x) / 2)]



median([4, 5, 5, 4])



def remove_duplicates(list):
    a = []
    for i in list:
        if i not in a:
            a.append(i)
    return a


def product(list):
    total = 1
    for num in list:
        total = total * num
    return total

def purify(x):
    a = []
    for i in x:
        if i % 2 == 0:
            a.append(i)
    return a

print purify([1,2,3,4,5,6,8,10,12])



def count(sequence,item):
    c = 0
    for i in sequence:
        if i == item:
            c += 1
    print c



def censor(x,y):
    b = '*' * len(y)
    for i in x.split():
        if i != y:
            print i,
        else:
            print b,



score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(x):
    a = 0
    for i in x:
        a += score[i.lower()]
    return a

def scrabble_score2(word):
    word = word.lower()
    total = 0
    for letter in word:
        for leter in score:
            if letter == leter:
                total = total + score[leter]
    return total


def anti_vowel(x):
    a = "aeiouAEIOU"
    for i in a:
        x = x.replace(i,"")
    print x

anti_vowel("aettebssd")

def reverse(x):
    a = len(x) - 1
    b = ''
    while a >= 0:
        b += x[a]
        a -= 1
    print b


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

def is_even(x):

    if (x % 2) == 0:
        return True
    else:
        return False

def is_int(x):
    print float(x)
    if float(x) == int(x):
        return True
    else:
        return False

def digit_sum(n):
    c = 0
    for i in str(n):
        c += int(i)
    return c

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


#8.18
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomatoj':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
    
#8.17
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

#8.16

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print max(a,b)

#8.15
choices = ['pizza', 'pasta', 'salad', 'nachos']


print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item

#8.14

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key, d[key]


#8.13
numbers  = [7, 9, 12, 54, 99]

print "This list contains: "

for num in numbers:
    print num

for i in numbers:
    print i ** 2


#8.12

phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print "X",
    else:
        print char,

print

#8.11

thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for i in word:
    print i

#8.10

hobbies = []

for i in range(3):
    hobby = raw_input("Input hoby: ")
    hobbies.append(hobby)
print hobbies


#8.9

print "Counting..."

for i in range(20):
    print i

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
