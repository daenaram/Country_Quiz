# no repeated values!!
# using .format code
# with the csv

from tkinter import *
import random
import csv


class Game:
    def __init__(self):

        # getting the options capitals
        self.trial_variable = StringVar()
        self.trial_variable.set("")

        self.game_frame = Frame()
        self.game_frame.grid()

        self.game_heading = Label(self.game_frame,
                                  text="Question 1 of #",
                                  font=("Arial", 16, "bold"))
        self.game_heading.grid(row=0)

        self.game_question = Label(self.game_frame,
                                   text="What is the capital of [Country]?",
                                   wraplength=260, width=60)
        self.game_question.grid(row=1)

        # option frame
        self.options_frame = Frame(self.game_frame)
        self.options_frame.grid(row=2)

        # button frame
        self.control_frame = Frame(self.game_frame)
        self.control_frame.grid(row=3)

        control_buttons = [
            ["#B1DDF0", "Next Question", "next question"],
            ["#FFE6CC", "Help", "get help"],
            ["#DAE8FC", "History", "get history"],
            ["#FAD9D5", "Start Over", "start over"]
        ]

        self.control_btn_ref = []

        for item in range(0, 4):
            self.make_control_btn = Button(self.control_frame,
                                           bg=control_buttons[item][0],
                                           text=control_buttons[item][1],
                                           width=12, font=("Arial", "12", "bold"),
                                           command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_btn.grid(row=0, column=item, padx=5, pady=5)

            # add buttons to control list
            self.control_btn_ref.append(self.make_control_btn)

            self.to_help_btn = self.control_btn_ref[0]

    def to_do(self, action):
        if action == "get help":
            print("Help")
        elif action == "get history":
            print("History")
        elif action == "start over":
            print("Start Over")
        else:
            self.get_next_question()

    def get_next_question(self):
        self.trial_variable.get()
        file = open("country_capitals.csv")
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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Game()
    root.mainloop()
