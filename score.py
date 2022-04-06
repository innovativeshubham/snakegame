from turtle import Turtle
from snake import Snake

ALIGNMENT = "center"
FONT = ("Courier", "16", "normal")

class Score(Turtle):

     def __init__(self):
          super().__init__()
          self.score = 0
          with open(file="score.txt", mode="r") as high_score_file:
               self.high_score = int(high_score_file.read())
          self.goto(0, 270)
          self.color("white")
          self.hideturtle()
          self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

     def update_score(self):
          self.clear()
          self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

     def reset(self):
          if self.score > self.high_score:
               self.high_score = self.score
          with open(file="score.txt", mode="w") as score_file:
               score_file.write(f"{self.high_score}")
          self.score = 0
          self.update_score()

     def increase_score(self):
          self.score += 1
          self.clear()
          self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
