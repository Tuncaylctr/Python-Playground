class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.quiz_score = 0
    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {item.text} (True/False): ")
        self.check_answer(user_answer, item.answer)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    
    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.quiz_score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.quiz_score}/{self.question_number}")