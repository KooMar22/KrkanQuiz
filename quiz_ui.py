# Import required modules
import os
import sys
from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox, PhotoImage
from quiz_brain import QuizBrain
from random import shuffle


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller.
    URL: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2  # Adjust to MEIPASS2 if not working
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Colors
BG_COLOR = "blue"
FG_COLOR = "black"

# Fonts
TITLE_FONT = ("Arial", 20, "bold")
QUESTION_FONT = ("Arial", 18, "italic", "bold")
FEEDBACK_FONT = ("Arial", 15, "bold")
RADIO_BUTTONS_FONT = ("Arial", 14)
NEXT_AND_QUIT_BUTTONS_FONT = ("Arial", 16, "bold")


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Krkan Kviz")
        self.window.geometry("850x530")

        # Display Title
        self.display_title()

        # Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=850, height=530, highlightthickness=0)
        quiz_image = PhotoImage(file=resource_path("imgs\\img1.png"))
        self.canvas.create_image(850 // 2, 530 // 2, image=quiz_image)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=BG_COLOR,
                                                     font=QUESTION_FONT
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Declare a StringVar to store user's answer
        self.user_answer = StringVar()

        # Display four options with radio buttons
        self.options = self.radio_buttons()
        self.display_options()

        # Next and Quit Button
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def display_title(self):
        """Display title"""

        # Title
        title = Label(self.window, text="Jesi li pravi krkan ili kulturni momak?",
                      width=50, bg=BG_COLOR, fg=FG_COLOR, font=TITLE_FONT)

        # place of the title
        title.place(x=0, y=2)

    def display_question(self):
        """Display the question"""

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

        

    def radio_buttons(self):
        """Create four options with radio buttons"""

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 4:

            # setting the radio button properties
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=RADIO_BUTTONS_FONT)

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=200, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options(self):
        """Display four options"""

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the answer options to be displayed for the
        # text of the radio buttons.
        answer_options = [
            self.quiz.current_question.correct_answer,
            self.quiz.current_question.good_answer,
            self.quiz.current_question.decent_answer,
            self.quiz.current_question.fair_answer
        ]

        # Shuffle the answer options
        shuffle(answer_options)
        
        for option in answer_options:
            self.options[val]['text'] = option
            self.options[val]['value'] = option
            val += 1

    def advance_question(self):
        """Check answers and keep checking for more questions"""

        # Check if the answer is correct
        self.quiz.check_answer(self.user_answer.get())
         
        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()

            # destroys the self.window
            self.window.destroy()

    def buttons(self):
        """Show Next and Quit buttons"""

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self.window, text="Dalje", command=self.advance_question,
                             width=10, bg="green", fg="white", font=NEXT_AND_QUIT_BUTTONS_FONT)

        # palcing the button  on the screen
        next_button.place(x=350, y=460)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.window, text="Izađi", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=NEXT_AND_QUIT_BUTTONS_FONT)

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)

    def display_result(self):
        """Display the result using messagebox"""
        score_percent = self.quiz.get_score()


        if score_percent >= 90:
            message = "Bravo! Prava si krkančina! Uzor roda i sela svog!"
        elif score_percent >= 75:
            message = "Na dobrom si putu, ali možeš i bolje!"
        elif score_percent >= 50:
            message = "Nisi loš, ali imaš još posla da postaneš pravi krkan!"
        else:
            message = "Nisi ti nikakav krkan! Radije odi u 'Bečke dječake'!"


        # Show the message in a message box
        messagebox.showinfo("Rezultat", message)