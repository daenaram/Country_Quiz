# no repeated values!!
# using .format code
# with the csv file

import random
import csv

file = open("country_capitals.csv", "r")
all_questions = list(csv.reader(file, delimiter=","))
file.close()

all_questions.pop(0)

options = []

while len(options) < 4:
    choose = random.choice(all_questions)

    if choose not in options:
        options.append(choose)

print(options)

question = options[0][0]
answer = options[0][1]


print("What is the capital of {}".format(question))
print(answer)

for item in options[1:]:
    print(item[1])