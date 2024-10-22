# Dưới đây là một ví dụ đơn giản về cách một hệ thống dạy học thông minh (Intelligent Tutoring System - ITS) có thể được triển khai bằng Python. Hệ thống này sẽ đưa ra câu hỏi toán học và điều chỉnh độ khó dựa trên câu trả lời của người học.
import random


class IntelligentTutoringSystem:
    def __init__(self):
        self.difficulty = 1

    def generate_question(self):
        if self.difficulty == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"What is {a} + {b}?", a + b
        elif self.difficulty == 2:
            a, b = random.randint(1, 20), random.randint(1, 20)
            return f"What is {a} - {b}?", a - b
        elif self.difficulty == 3:
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"What is {a} * {b}?", a * b

    def adjust_difficulty(self, correct):
        if correct:
            self.difficulty = min(self.difficulty + 1, 3)
        else:
            self.difficulty = max(self.difficulty - 1, 1)

    def start(self):
        print("Welcome to the Intelligent Tutoring System!")
        while True:
            question, answer = self.generate_question()
            user_answer = input(question + " ")

            if user_answer.lower() == "exit":
                print("Thank you for using the Intelligent Tutoring System!")
                break

            try:
                if int(user_answer) == answer:
                    print("Correct!")
                    self.adjust_difficulty(True)
                else:
                    print(f"Incorrect. The correct answer was {answer}.")
                    self.adjust_difficulty(False)
            except ValueError:
                print("Please enter a valid number or type 'exit' to quit.")


# Run the tutoring system
its = IntelligentTutoringSystem()
its.start()
