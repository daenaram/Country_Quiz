from tkinter import *
from functools import partial  # To prevent unwanted windows
# error messaged changed
# has min / max
# start over button


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
    def check_rounds(self, min_value, max_value):

        has_error = "no"
        error = "Please enter a number more than {} or less than {}".format(min_value, max_value)

        response = self.quiz_entry.get()

        try:
            response = int(response)

            if response < min_value:
                has_error = "yes"

            elif response > max_value:
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
        to_play = self.check_rounds(1, 20)

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

        game_heading = "Choose - Question 1 of {}".format(how_many)
        self.choose_heading = Label(self.game_frame,
                                    text=game_heading,
                                    font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.game_frame)
        self.control_frame.grid(row=3)

        self.start_over = Button(self.control_frame,
                                 text="Start Over",
                                 command=self.close_game)
        self.start_over.grid(row=0, column=1, padx=5, pady=5)

    def close_game(self):
        root.deiconify()
        self.game_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
