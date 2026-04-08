from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

while quiz.continuing():
    quiz.next_question()
print("You have reached the end of the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

