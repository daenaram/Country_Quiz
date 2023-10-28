from tkinter import *


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

    # only have the error message
    def check_rounds(self, min_value):

        has_error = "no"
        error = "Please enter a number more than {}".format(min_value)

        try:
            response = self.quiz_entry.get()
            response = float(response)

            if response < min_value:
                has_error = "yes"

        except ValueError:
            has_error = "yes"

        if has_error == "yes":
            self.error_label.config(text=error, fg="#9C0000")
        else:
            self.error_label.config(text="The quiz will now start", fg="blue")

    def to_enter(self):

        self.check_rounds(1)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
