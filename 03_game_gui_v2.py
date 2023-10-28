from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


class Start:

    def __init__(self):

        self.feedback = StringVar()
        self.feedback.set("")

        self.feedback_error = StringVar()
        self.feedback_error.set("no")

        # start GUI frame
        self.quiz_frame = Frame()
        self.quiz_frame.grid()

        self.quiz_heading = Label(self.quiz_frame,
                                  text="Country Capitals",
                                  font=("Arial", "16", "bold"))
        self.quiz_heading.grid(row=0)

        instruction = "Please enter how many questions you would like to answer and press enter."
        self.quiz_instruction = Label(self.quiz_frame,
                                      text=instruction,
                                      wraplength=260, width=60)
        self.quiz_instruction.grid(row=1)

        # Frame for the textbox and enter button
        self.input_frame = Frame(self.quiz_frame)
        self.input_frame.grid(row=2)

        self.quiz_entry = Entry(self.input_frame,
                                font=("Arial", "14"))
        self.quiz_entry.grid(row=0, column=0, padx=5, pady=5)

        self.enter_button = Button(self.input_frame, text="Enter",
                                   bg="#a2eba2", fg="#000000",
                                   font=("Arial", "14", "bold"),
                                   padx=10, pady=1,
                                   command=self.to_enter)
        self.enter_button.grid(row=0, column=1, padx=5, pady=5)

        error = "Please enter a valid number"
        self.error_label = Label(self.quiz_frame, text="",
                                 font=("Arial", "10"),
                                 fg="#9C0000")
        self.error_label.grid(row=3)

    # error message and the text box turns red
    def check_rounds(self, min_value):

        has_error = "no"
        error = "Please enter a number more than {} and/or a whole number".format(min_value)

        response = self.quiz_entry.get()

        try:
            response = int(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.feedback_error.set("yes")
            self.feedback.set(error)
            return "invalid"

        else:
            self.feedback_error.set("no")
            self.to_game(response)

    def to_enter(self):
        to_play = self.check_rounds(1)

        if to_play != "invalid":
            self.feedback.set("{} number of rounds will now start".format(to_play))

        self.output_outcome()

    def output_outcome(self):
        output = self.feedback.get()
        has_error = self.feedback_error.get()

        if has_error == "yes":
            self.error_label.config(fg="#9C0000")
            self.quiz_entry.config(bg="#F8CECC")

        else:
            self.error_label.config(fg="#004C00")
            self.quiz_entry.config(bg="#FFFFFF")

        self.error_label.config(text=output)

    def to_game(self, num_rounds):
        Game(num_rounds)

        root.withdraw()


class Game:

    def __init__(self, how_many):

        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_game))

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        game_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.game_frame,
                                    text=game_heading,
                                    font=("Arial", "18", "bold"))
        self.choose_heading.grid(row=0)

        game_question = "What is the capital of [Country]"
        self.game_question_label = Label(self.game_frame, text=game_question,
                                         font=("Arial", "14"))
        self.game_question_label.grid(row=1)

        self.control_frame = Frame(self.game_frame)
        self.control_frame.grid(row=3)

        control_buttons = [
            ["#B1DDF0", "Next Question", "next question"],
            ["#FFE6CC", "Help", "get help"],
            ["#DAE8FC", "History", "get history"],
            ["#FAD9D5", "Start Over", "start over"]
        ]

        self.control_btn_ref = []

        # commands for control buttons
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
            Help(self)
        elif action == "get history":
            self.get_history()
        elif action == "start over":
            self.close_game()
        else:
            self.get_next_question()

    def get_history(self):
        print("history")

    def get_next_question(self):
        print("next question")

    def close_game(self):
        root.deiconify()
        self.game_box.destroy()


class Help:
    def __init__(self, partner):
        # dialogue box
        self.help_box = Toplevel()

        # display help button
        partner.to_help_btn.config(state=DISABLED)

        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200, bg="#FFE6CC")
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg="#FFE6CC",
                                        text="Help",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_instruction = "This quiz will test your knowledge of countries and their capitals. " \
                           "You'll be presented with a series of questions about different countries. " \
                           "Choose the correct capital for each country from the provided options. \n\n" \
                           "Good luck and enjoy the quiz!"

        self.help_text_label = Label(self.help_frame, bg="#FFE6CC",
                                     text=help_instruction, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        partner.to_help_btn.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
