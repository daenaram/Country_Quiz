# no repeated values!!
# using .format code

import random

my_list = [
    ["grass", "green"], ["sky", "blue"], ["sun", "yellow"], ["rose", "pink"], ["paper", "white"],
    ["chocolate", "brown"], ["carrot", "orange"], ["barney", "purple"]
]

options = []

while len(options) < 4:
    choose = random.choice(my_list)

    # only adds item if it's not already in the list
    if choose not in options:
        options.append(choose)


print(options)

question = options[0][0]
answer = options[0][1]

print("what colour is the colour of {}".format(question))
print("{} is colour {}".format(question, answer))

for item in options[1:]:
    print(item[1])
