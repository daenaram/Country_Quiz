# no repeated values!!
# using .format code
# with the csv
# fixed the question
# added the option buttons

from tkinter import *
import random
import csv


class Game:
    def __init__(self):

        # store the capitals
        self.trial_variable = StringVar()
        self.trial_variable.set("")

        self.game_frame = Frame()
        self.game_frame.grid()

        self.game_heading = Label(self.game_frame,
                                  text="Question 1 of #",
                                  font=("Arial", 14, "bold"))
        self.game_heading.grid(row=0)

        self.next = self.get_csv_file()
        quiz_list = self.get_quest_ans()

        self.game_question = Label(self.game_frame,
                                   text="What is the capital of {}?".format(quiz_list[0][0]),
                                   wraplength=260, width=60)
        self.game_question.grid(row=1)

        # option frame
        self.options_frame = Frame(self.game_frame)
        self.options_frame.grid(row=2)

        for item in range(0, 4):
            self.options_button = Button(self.options_frame,
                                         fg="#000000",
                                         bg="#A3D4FF",
                                         text="{}".format(quiz_list[item][1]),
                                         width=30, height=2,
                                         command=lambda i=item: self)
            self.options_button.grid(row=item // 2,
                                     column=item % 2,
                                     padx=5, pady=5)

        # button frame
        self.control_frame = Frame(self.game_frame)
        self.control_frame.grid(row=3)

        control_buttons = [
            ["#B1DDF0", "Next Question", "next question"],
            ["#FFE6CC", "Help", "get help"],
            ["#DAE8FC", "History", "get history"],
            ["#FAD9D5", "Start Over", "start over"]
        ]

        # list to hold each control button separately
        self.control_btn_ref = []

        for item in range(0, 4):
            self.make_control_btn = Button(self.control_frame,
                                           bg=control_buttons[item][0],
                                           text=control_buttons[item][1], width=12,
                                           font=("Arial", "12", "bold"),
                                           command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_btn.grid(row=0, column=item, padx=5, pady=5)

            # add buttons to control list
            self.control_btn_ref.append(self.make_control_btn)

    # the button action lists
    def to_do(self, action):
        if action == "get help":
            print("Help")
        elif action == "get history":
            print("History")
        elif action == "start over":
            print("Start Over")
        else:
            print("Next Question")

    def get_csv_file(self):

        self.trial_variable.get()

        file = open("country_capitals.csv")
        var_all_questions = list(csv.reader(file, delimiter=","))
        file.close()

        var_all_questions.pop(0)
        return var_all_questions

    def get_quest_ans(self):
        options = []

        while len(options) < 4:
            choose = random.choice(self.next)

            if choose not in options:
                options.append(choose)

        return options


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Game()
    root.mainloop()
