from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text Here',
            fill=THEME_COLOR, font=('Arial', 16, 'italic')
        )

        check_img = PhotoImage(file='images/true.png')
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.check_button_check)
        self.check_button.grid(column=0, row=2)

        cross_img = PhotoImage(file='images/false.png')
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.cross_button_check)
        self.cross_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You've reached the end of the quiz.")
            self.check_button.config(state='disabled')
            self.cross_button.config(state='disabled')

    def check_button_check(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def cross_button_check(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
