def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"

print check_bit4(4)

print "-----"
for i in range(2,15):
    print "sm"+str(i)+".mgmt.uld",
#10.16
threes_and_fives = [i for i in range(1,16) if i % 3 == 0 or i % 5 == 0]
print threes_and_fives

#10.14
squares = [x ** 2 for x in range(1,11)]
print filter(lambda x: x >=30 and x <= 70,squares)

#10.11
to_21 = [i for i in range(1,22)]
odds = to_21[::2]
middle_third = to_21[7:14]

#10.10
to_one_hundred = range(101)
# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens


#10.8
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]


#10.6
cubes_by_four = [i ** 3 for i in range(1,11) if (i ** 3) % 4 == 0]
print cubes_by_four


even_squares = [x ** 2 for x in range(1,12) if x % 2 == 0]

print even_squares


evens_to_50 = [i for i in range(51) if i % 2 == 0]
#print evens_to_50


#10.3
my_dict = {
    "Name": "Guido",
    "Age": 56,
    "BDFL": True,
    "Lazy": True
}

#print my_dict.keys()
#print my_dict.values()

#for key in my_dict:
#    print key,my_dict[key]