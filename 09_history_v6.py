from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random
import re


# users choose 3, 5, or 10 rounds
class Start:

    def __init__(self):
        # invoke play class with three rounds for testing purposes
        self.to_game(5)

    def to_game(self, num_rounds):
        Game(num_rounds)

        # hide root window (ie: hide rounds choice window).
        root.withdraw()


class Game:

    def __init__(self, how_many):

        self.game_box = Toplevel()

        # list to hold user score/s and computer score/s
        # used to work out statistics

        self.country_question = ["Myanmar", "Central African Republic", "Uganda",
                                 "United Kingdom", "Singapore"]
        self.user_ans = ["Pretoria", "Bangui", "Kampala", "Helsinki", "Podgorica"]
        self.right_ans = ["Naypyidaw", "Bangui", "Roseau", "London", "Singapore"]

        self.game_frame = Frame(self.game_box, padx=10, pady=10)
        self.game_frame.grid()

        self.control_frame = Frame(self.game_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#B1DDF0", "Next Question", "next question"],
            ["#FFE6CC", "Help", "get help"],
            ["#DAE8FC", "History", "get history"],
            ["#FAD9D5", "Start Over", "start over"]
        ]

        # list to hold references for control buttons
        # so tha the text of the 'start over' button
        # can easily be configured when the game is over
        self.control_btn_ref = []

        for item in range(0, 4):
            self.make_control_btn = Button(self.control_frame,
                                           bg=control_buttons[item][0],
                                           text=control_buttons[item][1], width=12,
                                           font=("Arial", "12", "bold"),
                                           command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_btn.grid(row=0, column=item, padx=5, pady=5)

            # add buttons tp control list
            self.control_btn_ref.append(self.make_control_btn)

        self.to_history_btn = self.control_btn_ref[2]

    def to_do(self, action):
        if action == "get help":
            pass
        elif action == "get history":
            History(self, self.country_question, self.user_ans, self.right_ans)
        else:
            self.close_game()

    # DO NOT USE THIS FUNCTION IN BASE, IT KILLS THE ROOT
    def close_game(self):
        root.destroy()


# Show users help / game tips
class History:
    def __init__(self, partner, country_question, user_cap, right_ans):

        self.history_box = Toplevel()

        question_no = 1
        quiz_question = ""
        for item in country_question:
            quiz_question += f"Q{question_no}: {item}"
            quiz_question += "\n"
            question_no += 1

        user_history = ""
        for item in user_cap:
            user_history += f"Your Answer {item}"
            user_history += "\n"

        right_answer = ""
        for item in right_ans:
            right_answer += f"Right answer {item}"
            right_answer += "\n"

        # display stats button
        partner.to_history_btn.config(state=DISABLED)

        # If users press cross at top, clos help and
        # 'release' help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box,
                                   height=300)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame,
                                           text="History",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        self.his_label_frame = Frame(self.history_frame)
        self.his_label_frame.grid(row=1)

        self.country_question_label = Label(self.his_label_frame, font=("Arial", "12"),
                                            text=quiz_question,
                                            wraplength=250)
        self.country_question_label.grid(row=0, column=0, padx=10, pady=10)

        self.user_cap_label = Label(self.his_label_frame, font=("Arial", "12"),
                                    text=user_history,
                                    wraplength=250)
        self.user_cap_label.grid(row=0, column=1, padx=10, pady=10)

        self.right_ans_label = Label(self.his_label_frame, font=("Arial", "12"),
                                     text=right_answer,
                                     wraplength=250)
        self.right_ans_label.grid(row=0, column=2, padx=10, pady=10)

        self.right_wrong_ans = Label(self.his_label_frame, font=("Arial", "12"),
                                     text="",
                                     wraplength=250)
        self.right_wrong_ans.grid(row=0, column=3, padx=10, pady=10)

        if user_history == right_answer:
            result = "Correct"
            self.right_wrong_ans.config(text=result)
        else:
            result = "Wrong"
            self.right_wrong_ans.config(text=result)

        # dismiss button
        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#2644A6",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_history(self, partner):
        partner.to_history_btn.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
