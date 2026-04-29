from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for a in question_data:
    question = Question(a["text"], a["answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.quiz_score}/{len(question_bank)}")
