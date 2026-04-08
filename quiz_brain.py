class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list = q_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(u_answer, current_question.answer)

    def continuing(self):
        continuing = self.question_number
        return continuing < len(self.questions_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong!\nThe right answer was {c_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
