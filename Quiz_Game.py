
import tkinter as tk
from tkinter import messagebox

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Rome", "Berlin"],
        "answer": "Paris",
        "hint": "It's the city of love."
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter",
        "hint": "This planet is known for its large storms, like the Great Red Spot."
    },
    {
        "question": "Which language is used for web development?",
        "choices": ["Python", "Java", "HTML", "C++"],
        "answer": "HTML",
        "hint": "This language is used to structure web pages."
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "choices": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "Suzanne Collins"],
        "answer": "J.K. Rowling",
        "hint": "This author is from the UK and became famous for the wizarding world."
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific",
        "hint": "This ocean touches the west coast of the United States."
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x400")

        self.question_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.choice_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.choice_buttons.append(btn)

        self.hint_button = tk.Button(root, text="Show Hint", font=("Arial", 12), command=self.show_hint)
        self.hint_button.pack(pady=10)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.load_question()

    def load_question(self):
        """Loads the current question and its answer choices."""
        question_data = questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        for i, choice in enumerate(question_data["choices"]):
            self.choice_buttons[i].config(text=choice)

    def check_answer(self, choice_index):
        """Checks if the selected answer is correct."""
        question_data = questions[self.question_index]
        selected_answer = question_data["choices"][choice_index]

        if selected_answer == question_data["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Good job! That's the right answer.")
        else:
            messagebox.showerror("Incorrect", f"Wrong! The correct answer was {question_data['answer']}.")

        self.score_label.config(text=f"Score: {self.score}")

        self.question_index += 1
        if self.question_index < len(questions):
            self.load_question()
        else:
            self.end_quiz()

    def show_hint(self):
        """Displays the hint for the current question."""
        question_data = questions[self.question_index]
        messagebox.showinfo("Hint", question_data["hint"])

    def end_quiz(self):
        """Ends the quiz and shows the final score."""
        messagebox.showinfo("Quiz Finished", f"Your final score is {self.score} out of {len(questions)}")
        self.root.quit()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
