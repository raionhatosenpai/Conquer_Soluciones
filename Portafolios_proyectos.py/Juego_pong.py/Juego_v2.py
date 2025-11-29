# Juego Pong con OOP y récord persistente, junto con una buena estructuracion del código,
# ademas de controles para salir del juego.

import turtle
import random
import os

# --- Clase Paleta ---
class Paddle(turtle.Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)

    def move_up(self):
        if self.ycor() < 250:
            self.sety(self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -250:
            self.sety(self.ycor() - 20)


# --- Clase Pelota ---
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.dx = 0.2 * random.choice([-1, 1])
        self.dy = 0.2 * random.choice([-1, 1])
        self.speed_increment = 0.01
        self.max_speed = 0.5

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        # Aumenta velocidad progresivamente
        if abs(self.dx) < self.max_speed:
            self.dx += self.speed_increment * (1 if self.dx > 0 else -1)
            self.dy += self.speed_increment * (1 if self.dy > 0 else -1)

    def reset_position(self):
        self.goto(0, 0)
        self.dx = 0.2 * random.choice([-1, 1])
        self.dy = 0.2 * random.choice([-1, 1])


# --- Clase Marcador ---
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_a = 0
        self.score_b = 0
        # Inicializa high_score leyendo del archivo
        self.high_score = self.load_high_score()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Jugador A: {self.score_a}  Jugador B: {self.score_b}  Máximo: {self.high_score}",
                   align="center", font=("Courier", 24, "normal"))

    def load_high_score(self):
        try:
            with open("high_score_v2.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_high_score(self):
        with open("high_score_v2.txt", "w") as f:
            f.write(str(self.high_score))


# --- Clase Juego ---
class PongGame:
    def __init__(self):
        self.wn = turtle.Screen()
        self.wn.title("Pong OOP por Raionhato")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)

        self.paddle_a = Paddle(-350)
        self.paddle_b = Paddle(350)
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        # Controles
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a.move_up, "w")
        self.wn.onkeypress(self.paddle_a.move_down, "s")
        self.wn.onkeypress(self.paddle_b.move_up, "Up")
        self.wn.onkeypress(self.paddle_b.move_down, "Down")
        self.wn.onkeypress(self.quit_game, "q")

    def quit_game(self):
        """Cierra el juego y guarda el récord"""
        self.scoreboard.save_high_score()
        print("Juego terminado. Récord guardado.")
        self.wn.bye()

    def play(self):
        while True:
            self.wn.update()
            self.ball.move()

            # Colisiones con bordes
            if self.ball.ycor() > 290:
                self.ball.sety(290)
                self.ball.bounce_y()
            if self.ball.ycor() < -290:
                self.ball.sety(-290)
                self.ball.bounce_y()

            # Punto para jugador A
            if self.ball.xcor() > 390:
                self.scoreboard.score_a += 1
                if self.scoreboard.score_a > self.scoreboard.high_score:
                    self.scoreboard.high_score = self.scoreboard.score_a
                self.scoreboard.update()
                self.ball.reset_position()

            # Punto para jugador B
            if self.ball.xcor() < -390:
                self.scoreboard.score_b += 1
                if self.scoreboard.score_b > self.scoreboard.high_score:
                    self.scoreboard.high_score = self.scoreboard.score_b
                self.scoreboard.update()
                self.ball.reset_position()

            # Colisiones con paletas
            if (340 < self.ball.xcor() < 350) and (self.paddle_b.ycor() - 50 < self.ball.ycor() < self.paddle_b.ycor() + 50):
                self.ball.setx(340)
                self.ball.bounce_x()

            if (-350 < self.ball.xcor() < -340) and (self.paddle_a.ycor() - 50 < self.ball.ycor() < self.paddle_a.ycor() + 50):
                self.ball.setx(-340)
                self.ball.bounce_x()


# --- Ejecutar juego ---
if __name__ == "__main__":
    game = PongGame()
    game.play()