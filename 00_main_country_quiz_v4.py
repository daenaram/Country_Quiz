from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import csv


class Start:

    def __init__(self):

        # string variable for the feedback when entering the number
        # of questions wanted
        self.feedback = StringVar()
        self.feedback.set("")

        # string variable for the feedback when entering the number
        # of questions wanted
        self.feedback_error = StringVar()
        self.feedback_error.set("no")

        # start GUI frame
        self.quiz_frame = Frame()
        self.quiz_frame.grid()

        # heading of the interface
        self.quiz_heading = Label(self.quiz_frame,
                                  text="Country Capitals",
                                  font=("Arial", "16", "bold"))
        self.quiz_heading.grid(row=0)

        # entering the number of wanted questions instruction
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

        self.error_label = Label(self.quiz_frame, text="",
                                 font=("Arial", "10"),
                                 fg="#9C0000")
        self.error_label.grid(row=3)

    # error message and the text box turns red
    # only accepts whole numbers
    def check_rounds(self, min_value, max_value):

        has_error = "no"
        error = "Please enter a number more than {} to {}".format(min_value, max_value)

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

    # checks if the number of question entered is
    # from 1 to 20
    def to_enter(self):
        to_play = self.check_rounds(1, 20)

        if to_play != "invalid":
            self.feedback.set("".format(to_play))

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


# Quiz GUI
class Game:

    def __init__(self, how_many):
        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_game))

        # store the capitals for the options
        self.capitals_variable = StringVar()
        self.capitals_variable.set("")

        # Variables used to work out statistics, when game ends etc
        self.questions_wanted = IntVar()
        self.questions_wanted.set(how_many)

        self.questions_played = IntVar()
        self.questions_played.set(0)

        # list to hold the question, user answer, right answer,
        # and the results (Right or Wrong) for history
        self.country_question = []
        self.user_ans = []
        self.right_ans = []
        self.results_question = []

        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        number_game_question = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.game_frame,
                                    text=number_game_question,
                                    font=("Arial", "14", "bold"))
        self.choose_heading.grid(row=0)

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
                                         command=lambda item=item: self.right_wrong_ans(self.quiz_list[item][1]))

            self.options_button_ref.append(self.options_button)

            self.options_button.grid(row=item // 2,
                                     column=item % 2,
                                     padx=5, pady=5)

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

        # to enable and disabled next question button
        self.to_next_question = self.control_btn_ref[0]
        self.to_help_btn = self.control_btn_ref[1]
        self.to_history_btn = self.control_btn_ref[2]

        # at starts, get 'new round'
        self.next_question()

    # the button action lists
    def to_do(self, action):
        if action == "get help":
            Help(self)
        elif action == "get history":
            History(self, self.country_question, self.user_ans, self.right_ans)
        elif action == "start over":
            self.close_game()
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
        # Reset the backgrounds of all option buttons to #A3D4FF
        for item in self.options_button_ref:
            item.config(bg="#A3D4FF")

        # disables next question every round
        # before the user chooses an option
        self.to_next_question.config(state=DISABLED)
        self.to_history_btn.config(state=DISABLED)

        # empty button list so we can get new capitals
        self.quiz_list.clear()

        # get new capitals for buttons
        self.quiz_list = self.get_quest_ans()

        # the question every round
        # retrieve correct answer!!
        question = self.quiz_list[0][0]
        self.correct_answer = self.quiz_list[0][1]  # Store the correct answer
        # print("correct answer is", self.correct_answer)

        self.right_ans.append(self.correct_answer)

        # shuffle list here
        random.shuffle(self.quiz_list)

        # Construct the full question text
        full_question = f"What is the capital of {question}"
        self.game_question.config(text=full_question)

        self.country_question.append(question)

        # Set the text and state for each button
        for idx, item in enumerate(self.options_button_ref):
            item['text'] = self.quiz_list[idx][1]
            item['state'] = NORMAL

        # retrieve number of questions wanted / played
        # and update heading.
        how_many = self.questions_wanted.get()
        current_round = self.questions_played.get()
        new_heading = "Question {} of {}".format(current_round + 1, how_many)
        self.choose_heading.config(text=new_heading)

    def right_wrong_ans(self, selected_option_text):
        selected_option_index = ""
        # print("you choose", selected_option_text)

        how_many = self.questions_wanted.get()

        # add one to number of question played
        current_question = self.questions_played.get()
        current_question += 1
        self.questions_played.set(current_question)

        # deactivate option buttons to prevent the user
        # to choose another option
        for item in self.options_button_ref:
            item.config(state=DISABLED)

        current_result = str(selected_option_text)
        self.user_ans.append(current_result)

        # disable the next button once they finished all the
        # questions wanted
        if current_question < how_many:
            self.to_next_question.config(state=NORMAL)

        if current_question == how_many or current_question < how_many:
            self.to_history_btn.config(state=NORMAL)

        right = "#D5E8D4"
        wrong = "#F8CECC"

        if selected_option_text == self.correct_answer:  # Compare with the correct answer
            for idx, option in enumerate(self.quiz_list):
                if option[1] == selected_option_text:
                    selected_option_index = idx
                    break
            # print("selected button index", selected_option_index)
            self.options_button_ref[selected_option_index].config(bg=right)
        else:
            for idx, option in enumerate(self.quiz_list):
                if option[1] == selected_option_text:
                    selected_option_index = idx
                    break
            # print("selected button index", selected_option_index)
            self.options_button_ref[selected_option_index].config(bg=wrong)

    # starts the game over
    def close_game(self):
        root.deiconify()
        self.game_box.destroy()


# help button
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
                                        text="Help / Hints",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0, pady=5)

        help_instruction = "This quiz will test your knowledge of countries and their capitals. " \
                           "You'll be presented with a series of questions about different countries. " \
                           "Choose the correct capital for each country from the provided options. \n\n" \
                           "Good luck and enjoy the quiz!"

        self.help_text_label = Label(self.help_frame, bg="#FFE6CC",
                                     text=help_instruction, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10, pady=5)

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


class History:
    def __init__(self, partner, country_question, user_cap, right_ans):

        # setup dialogue box
        self.history_box = Toplevel()

        # number of question
        question_no = 1
        quiz_question = ""
        for item in country_question:
            quiz_question += f"{question_no}: {item}"
            quiz_question += "\n"
            question_no += 1

        # user's answer
        user_history = ""
        for item in user_cap:
            user_history += f"{item}"
            user_history += "\n"

        # right answer
        right_answer = ""
        for item in right_ans:
            right_answer += f"{item}"
            right_answer += "\n"

        # display history button
        partner.to_history_btn.config(state=DISABLED)

        # If users press cross at top, close help and
        # 'release' help button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        # frame for the history heading
        self.history_frame = Frame(self.history_box,
                                   height=300)
        self.history_frame.grid()

        # history heading
        self.history_heading_label = Label(self.history_frame,
                                           text="History",
                                           font=("Arial", "16", "bold"))
        self.history_heading_label.grid(row=0)

        # frame for the labels and contents
        self.his_label_frame = Frame(self.history_frame)
        self.his_label_frame.grid(row=1)

        # question frame (the first column)
        self.question_frame = Frame(self.his_label_frame)
        self.question_frame.grid(row=0, column=0)

        # user answer frame (the second column)
        self.your_answer_frame = Frame(self.his_label_frame)
        self.your_answer_frame.grid(row=0, column=1)

        # right capital frame (the third column)
        self.right_answer_frame = Frame(self.his_label_frame)
        self.right_answer_frame.grid(row=0, column=2)

        # the labels and content font
        label_font = ("Arial", "14", "bold")
        content_font = ("Arial", "12")

        self.question_label = Label(self.question_frame, text="Question",
                                    font=label_font)
        self.question_label.grid(row=0, column=0, padx=10, pady=10)

        self.country_question_label = Label(self.question_frame, font=content_font,
                                            text=quiz_question)
        self.country_question_label.grid(row=1, column=0, padx=30, pady=10)

        self.user_answer_label = Label(self.your_answer_frame, text="Your Answer",
                                       font=label_font)
        self.user_answer_label.grid(row=0, column=0, padx=10, pady=10)

        self.user_cap_label = Label(self.your_answer_frame, font=content_font,
                                    text=user_history)
        self.user_cap_label.grid(row=1, column=0, padx=30, pady=10)

        self.correct_cap = Label(self.right_answer_frame, text="Right Answer",
                                 font=label_font)
        self.correct_cap.grid(row=0, column=0, padx=10, pady=10)

        self.right_ans_label = Label(self.right_answer_frame, font=content_font,
                                     text=right_answer)
        self.right_ans_label.grid(row=1, column=0, padx=30, pady=10)

        # dismiss button
        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#2644A6",
                                     fg="#FFFFFF",
                                     command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=3, padx=10, pady=10)

    def close_history(self, partner):
        partner.to_history_btn.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Country Quiz")
    Start()
    root.mainloop()
