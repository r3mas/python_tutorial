
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

# Add your function here
def join_strings(words):
    result = ""
    for i in words:
        #range(len(words)):
        #result += words[i]
        result += i
    return result

def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            #print i
            results.append(i)
    return results



n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
#n = ["Michael", "Lieberman"]
#n = [1, 5, 7]

#print join_strings(n)
print flatten(n)
#print total(n)
#print_list(n)
#print double_list(n)