# hard codded version of the game gui
from tkinter import *


class Game:
    def __init__(self):
        # Game GUI frame
        self.game_frame = Frame()
        self.game_frame.grid()

        self.game_heading = Label(self.game_frame,
                                  text="Question # of #",
                                  font=("Arial", 16, "bold"))
        self.game_heading.grid(row=0)

        self.game_question = Label(self.game_frame,
                                   text="What is the capital of [Country]?",
                                   wraplength=260, width=60)
        self.game_question.grid(row=1)

        # button frame
        self.option_frame = Frame(self.game_frame)
        self.option_frame.grid(row=2)

        # button background and fg
        button_bg = "#008CFF"
        button_fg = "#FFFFFF"

        # option buttons
        self.option_button_1 = Button(self.option_frame,
                                      background=button_bg,
                                      fg=button_fg,
                                      text="[Capital] 1",
                                      padx=50, pady=5)
        self.option_button_1.grid(row=0, column=0, padx=5, pady=5)

        self.option_button_2 = Button(self.option_frame,
                                      background=button_bg,
                                      fg=button_fg,
                                      text="[Capital] 2",
                                      padx=50, pady=5)
        self.option_button_2.grid(row=0, column=1, padx=5, pady=5)

        self.option_button_3 = Button(self.option_frame,
                                      background=button_bg,
                                      fg=button_fg,
                                      text="[Capital] 3",
                                      padx=50, pady=5)
        self.option_button_3.grid(row=1, column=0, padx=5, pady=5)

        self.option_button_4 = Button(self.option_frame,
                                      background=button_bg,
                                      fg=button_fg,
                                      text="[Capital] 4",
                                      padx=50, pady=5)
        self.option_button_4.grid(row=1, column=1, padx=5, pady=5)

        # frame for next question, start over, help, and stats/history
        self.control_frame = Frame(self.game_frame)
        self.control_frame.grid(row=3)

        # buttons for next question, start over, help, and stats/history
        self.next_question = Button(self.control_frame,
                                    background="#B1DDF0",
                                    text="Next Question",
                                    width=12)
        self.next_question.grid(row=0, column=0, padx=2, pady=5)

        self.start_over = Button(self.control_frame,
                                 background="#FAD9D5",
                                 text="Start Over",
                                 width=12)
        self.start_over.grid(row=0, column=1, padx=2, pady=5)

        self.help = Button(self.control_frame,
                           background="#FFE6CC",
                           text="Help",
                           width=12)
        self.help.grid(row=0, column=2, padx=2, pady=5)

        self.history = Button(self.control_frame,
                              background="#DAE8FC",
                              text="History",
                              width=12)
        self.history.grid(row=0, column=3, padx=2, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Game()
    root.mainloop()
