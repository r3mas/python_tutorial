n = [1, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result = numbers[i] + result
    return result

print total(n)

#print_list(n)
#print double_list(n)