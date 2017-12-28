# This is the downloader.py file for the matching downloader.kv file

#Module imports
import requests


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock

from random import randint


class PongGame(Widget):
    score = NumericProperty(0)
    streak_notice = ObjectProperty(None)
    streak = NumericProperty(0)

    def serve_ball(self):
        print(self.width, self.height, "~" * 50)
        self.ball.center = (self.height, 0)
        self.crosshairs.center = self.center
        self.score = 0

    def update(self, dt):
        self.ball.move()

        #print(self.ball.x, self.ball.y)

        # Target Detection
        if (    (self.ball.x <= self.crosshairs.x <= self.ball.x + 50)
            and (self.ball.y <= self.crosshairs.y <= self.ball.y + 50)):
            print("Hit.")
            self.resetBall()
            self.score += 1
            self.streak += 1

        # When the ball reaches the bottom of the window, return it to the top
        # at a different column.
        if (self.ball.y < 0):
            self.resetBall()
            self.streak = 0
            self.streak_notice = "Whoops!"

        if self.streak >= 10:
            self.streak_notice = "Streak!"

    def resetBall(self):
        """
        Used to reset the ball position.
        """
        print("Reset", self.ball.center)
        self.ball.y = self.height - 50
        self.ball.x = randint(0, self.width - 50)

class Crosshairs(Widget):
    crosshairs = ObjectProperty(None)

    def on_touch_down(self, touch):
        #print(self.pos)
        #print(touch.pos)
        self.pos = touch.pos

    def on_touch_move(self, touch):
        #print(self.pos)
        #print(touch.pos)
        self.pos = touch.pos


class PongBall(Widget):
    # Velocity of the pong ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # Ball properties
    ball = ObjectProperty(None)


    def move(self):
        self.pos[1] = self.pos[1] - 4
        #print(self.pos)


# DONE: This class creates the Main Application!
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


# The following lines instantiate and run the application.
if __name__ == "__main__":
    app = PongApp()
    app.run()
