from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    quest_text = question["text"]
    quest_answer = question["answer"]
    new_question = Question(question_text=quest_text, question_answer=quest_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you have completed the quiz")
print(f"Your final score is {quiz.score}/ {quiz.question_number}")
