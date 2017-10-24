#8.6

count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break



"""
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