# no repeated values!!
# using .format code
# with the csv
# fixed the question
# added the option buttons
# get the user's choice

from tkinter import *
import random
import csv


class Start:
    def __init__(self):
        self.to_game(3)

    def to_game(self, num_rounds):
        Game(num_rounds)

        root.withdraw()


class Game:
    def __init__(self, how_many):

        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW')

        # store the capitals for the options
        self.capitals_variable = StringVar()
        self.capitals_variable.set("")

        # Variables used to work out statistics, when game ends etc
        self.questions_wanted = IntVar()
        self.questions_wanted.set(how_many)

        self.questions_played = IntVar()
        self.questions_played.set(0)

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        number_game_question = "Question 1 of {}".format(how_many)
        self.game_heading = Label(self.game_frame,
                                  text=number_game_question,
                                  font=("Arial", "14", "bold"))
        self.game_heading.grid(row=0)

        # store the csv file for the questions and options
        self.button_options = self.get_csv_file()
        self.button_list_options = self.get_quest_ans()

        self.quiz_list = []

        self.game_question = Label(self.game_frame,
                                   text="",
                                   wraplength=260, width=60)

        self.game_question.grid(row=1)

        # option frame
        self.options_frame = Frame(self.game_frame)
        self.options_frame.grid(row=2)

        self.options_button_ref = []

        for item in range(0, 4):
            self.options_button = Button(self.options_frame,
                                         fg="#000000",
                                         bg="#A3D4FF",
                                         width=30, height=2,
                                         command=lambda i=item: self.right_wrong_ans(self.quiz_list[i][1]))

            self.options_button_ref.append(self.options_button)

            self.options_button.grid(row=item // 2,
                                     column=item % 2,
                                     padx=5, pady=5)

        # at starts, get 'new round'
        self.next_question()

        # control button frame
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
                                           text=control_buttons[item][1], width=12,
                                           font=("Arial", "12", "bold"),
                                           command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_btn.grid(row=0, column=item, padx=5, pady=5)

            # add buttons to control list
            self.control_btn_ref.append(self.make_control_btn)

            self.to_help_btn = self.control_btn_ref[0]

    # the button action lists
    def to_do(self, action):
        if action == "get help":
            print("Help")
        elif action == "get history":
            print("History")
        elif action == "start over":
            print("Start Over")
        else:
            self.next_question()

    # getting the csv file
    def get_csv_file(self):

        self.capitals_variable.get()

        file = open("country_capitals.csv", "r")
        var_all_questions = list(csv.reader(file, delimiter=","))
        file.close()

        # removes the first row in the csv file
        var_all_questions.pop(0)

        return var_all_questions

    def get_quest_ans(self):
        options = []

        while len(options) < 4:
            choose = random.choice(self.button_options)
            index_chosen = self.button_options.index(choose)

            # only adds item if it's not already in the list
            if choose not in options:
                options.append(choose)

                # remove item from master list
                self.button_options.pop(index_chosen)

        return options

    def next_question(self):

        # empty button list so we can get new capitals
        self.quiz_list.clear()

        # get new capitals for buttons
        self.quiz_list = self.get_quest_ans()

        # the question every round
        question = self.quiz_list[0][0]
        full_question = f"What is the capital of {question}"
        self.game_question.config(text=full_question)

        # to set the text
        count = 0
        for item in self.options_button_ref:
            item['text'] = self.quiz_list[count][1]
            item['state'] = NORMAL

            count += 1

        # retrieve number of questions wanted / played
        # and update heading.
        how_many = self.questions_wanted.get()
        current_round = self.questions_played.get()
        new_heading = "Question {} of {}".format(current_round + 1, how_many)
        self.game_heading.config(text=new_heading)

    def right_wrong_ans(self, user_choice):

        ans = self.quiz_list[0][1]

        print("you choose", user_choice)
        print("The right answer is", ans)

        # add one to number of question played
        current_question = self.questions_played.get()
        current_question += 1
        self.questions_played.set(current_question)

        # deactivate colour buttons!
        for item in self.options_button_ref:
            item.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
