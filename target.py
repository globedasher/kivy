# This is the downloader.py file for the matching downloader.kv file

#Module imports
import requests

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty, BooleanProperty
from kivy.vector import Vector
from kivy.clock import Clock

from random import randint


class TargetGame(Widget):
    score = NumericProperty(0)
    streak_notice = ObjectProperty(None)
    streak = NumericProperty(0)
    enemies = [(400, 700), (50, 50)]

    def __init__(self, **kwargs):
        super(TargetGame, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(None, self)
        if not self._keyboard:
            return
        self._keyboard.bind(on_key_down=self.on_keyboard_down)

    def serve_ball(self):
        #print(self.width, self.height, "~" * 50)
        #print(self.enemies[0])
        self.ball.center = self.enemies[0]
        self.crosshairs.center = self.center
        self.score = 0
        return self

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "left":
            self.crosshairs.x -= 10
        elif keycode[1] == "right":
            self.crosshairs.x += 10
        else:
            return False
        return True

    def update(self, dt):
        self.ball.move()

        #print(self.ball.x, self.ball.y)

        #if len(self.enemies) < 6:
            #self.enemies.append(self.serve_ball())

        # Target Detection
        if (    (self.ball.x <= self.crosshairs.x <= self.ball.x + 50)
            and (self.ball.y <= self.crosshairs.y <= self.ball.y + 50)):
            #print("Hit.")
            self.resetBall()
            self.score += 1
            self.streak += 1

            if not self.streak_notice.text:
                self.streak_notice.text = "Play ball!"
            if len(self.streak_notice.text) > 0:
                self.streak_notice.text = ""

        # When the ball reaches the bottom of the window, return it to the top
        # at a different column.
        if (self.ball.y < 0):
            self.resetBall()
            self.streak = 0
            self.streak_notice.text = "Whoops!"

        if self.streak >= 10:
            self.streak_notice.text = "Streak!"

    def resetBall(self):
        """
        Used to reset the ball position.
        """
        #print("Reset", self.ball.center)
        self.ball.y = self.height - 50
        self.ball.x = randint(0, self.width - 50)

class Crosshairs(Widget):
    crosshairs = ObjectProperty(None)

   #  def on_touch_down(self, touch):
   #      #print(self.pos)
   #      #print(touch.pos)
   #      self.pos = touch.pos

   #  def on_touch_move(self, touch):
   #      #print(self.pos)
   #      #print(touch.pos)
   #      self.pos = touch.pos


class TargetBall(Widget):
    # Ball properties
    ball = ObjectProperty(None)


    def move(self):
        self.pos[1] = self.pos[1] - 4
        #print(self.pos)

# DONE: This class creates the Main Application!
class TargetApp(App):
    def build(self):
        game = TargetGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


# The following lines instantiate and run the application.
if __name__ == "__main__":
    app = TargetApp()
    app.run()
