class QuizBrain():

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """Check if the quiz has more questions"""
        return self.question_no < len(self.questions)
    
    def next_question(self):
        """Get the next question by increasing the question number"""
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Pitanje {self.question_no}: {q_text}"
    
    def check_answer(self, user_answer):
        """Check the answer from the user and assign it the appropriate score"""
        points_awarded = 0

        # Define type of answers
        correct_answer = self.current_question.correct_answer
        good_answer = self.current_question.good_answer
        decent_answer = self.current_question.decent_answer
        fair_answer = self.current_question.fair_answer

        # Assign a score based on answer type
        if user_answer == correct_answer:
            points_awarded += 4
        elif user_answer == good_answer:
            points_awarded += 3
        elif user_answer == decent_answer:
            points_awarded += 2
        elif user_answer == fair_answer:
            points_awarded += 1

        self.score += points_awarded
        return points_awarded
        
        
    def get_score(self):
        """Get the score percentage"""
        total_questions = len(self.questions)
        max_possible_score = total_questions * 4 # Max score 4 per question
        score_percent = int((self.score / max_possible_score) * 100)
        return score_percent