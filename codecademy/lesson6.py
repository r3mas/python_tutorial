'''1.

Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.

    Define a function called get_average that takes one argument called student.
    Make a variable homework that stores the average() of student["homework"].
    Repeat the above step for "quizzes" and "tests".
    Multiply the 3 averages by their weights and return the sum of those three. Homework is 10%, quizzes are 30% and tests are 60%.

'''

lloyd = {
    "name": "Lloyd",
    "homework": [0.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(numbers):
    return float(sum(numbers)) / len(numbers)


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])

    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(class_list):
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)



print average(alice["homework"])
print get_average(lloyd)
print get_letter_grade(get_average(lloyd))
a = [lloyd,alice]
print get_class_average(a)