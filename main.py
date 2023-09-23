# Import required modules
import sys
import os
import json
from question_model import Question
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface


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


def read_question_data_from_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        question_data = json.load(json_file)
    return question_data

def quiz_game():
    question_bank = []
    question_data = read_question_data_from_json(resource_path("question_data.json"))
    for question in question_data:
        question_text = question["question_text"]
        correct_answer = question["correct_answer"]
        good_answer = question["good_answer"]
        decent_answer = question["decent_answer"]
        fair_answer = question["fair_answer"]
        answer_choices = [correct_answer, good_answer, decent_answer, fair_answer]
        new_question = Question(question_text, *answer_choices)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)


def main():
    quiz_game()


if __name__ == "__main__":
    main()