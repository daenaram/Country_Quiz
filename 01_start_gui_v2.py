from tkinter import *
from functools import partial


class Start:

    def __init__(self):
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

        self.start_button = Button(self.input_frame, text="Enter",
                                   bg="#a2eba2", fg="#000000",
                                   font=("Arial", "14", "bold"),
                                   command=lambda: self.to_start,
                                   padx=10, pady=1)
        self.start_button.grid(row=0, column=1, padx=5, pady=5)

        self.error_label = Label(self.quiz_frame, text="",
                                 fg="#9C0000")
        self.error_label.grid(row=3)

    def to_start(self, enter_button):
        Start(enter_button)

        root.withdraw()

class Play:
    def __init__(self):

        self.start_box = Toplevel()

        self.start_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_start))

        self.game_frame = Frame(self.start_box)
        self.game_frame.grid()

        self.question_heading = Label(self.game_frame, text="Choose - Rounds 1 of {}",
                                      font=("Arial", "16", "bold"),
                                      wraplength=260)
        self.question_heading.grid(row=0)

    def close_start(self):
        root.deiconify()
        self.start_box.destroy()






# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
