from tkinter import *
from functools import partial  # To prevent unwanted windows
from datetime import date
import re


class Game:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "14", "bold")

        self.country_question = ['Myanmar', 'Central African Republic', 'Uganda', 'United Kingdom', 'Singapore']
        self.user_cap = ['Pretoria', 'Bangui', 'Kampala', 'Helsinki', 'Podgorica']
        self.capital = ['Naypyidaw', 'Bangui', 'Roseau', 'London', 'Singapore']

        # start GUI frame
        self.game_frame = Frame()
        self.game_frame.grid()

        self.his_btn_frame = Frame(padx=30, pady=30)
        self.his_btn_frame.grid(row=0)

        self.to_history_button = Button(self.his_btn_frame,
                                        text="History",
                                        bg="#DAE8FC",
                                        font=button_font, width=12,
                                        command=lambda: History(self, self.country_question, self.user_cap,
                                                                self.capital))
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


class History:
    def __init__(self, partner, country_question, user_cap, capital):

        self.history_box = Toplevel()

        partner.to_history_button.config(state=DISABLED)

        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300,
                                   height=300)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame,
                                           text="History",
                                           font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        self.data_frame = Frame(self.history_frame, borderwidth=1,
                                relief="solid")
        self.data_frame.grid(row=1, padx=10, pady=10)

        self.country_quest = self.get_history(country_question, "Question")
        self.capital_answer = self.get_history(user_cap, "User Answer")

        row_names = ["", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5"]

        all_labels = []

        count = 0
        for item in range(0, len(self.country_quest)):
            all_labels.append([row_names[item]])
            all_labels.append([self.country_quest[item]])
            all_labels.append([self.capital_answer[item]])
            count += 1

        for item in range(0, len(all_labels)):
            self.data_label = Label(self.data_frame, text=all_labels[item][0],
                                    width=10, height=2, padx=5)
            self.data_label.grid(row=item // 3,
                                 column=item % 3,
                                 padx=0, pady=0)

        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#2644A6",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=3, padx=10, pady=10)

    @staticmethod
    def get_history(answers_list, entity):

        return [entity]

    def close_history(self, partner):
        partner.to_history_button.cofig(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Game()
    root.mainloop()
