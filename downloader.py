# This is the downloader.py file for the matching downloader.kv file

#Module imports
import requests


from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.event import EventDispatcher
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import FocusBehavior


print("Welcome to Downloader!")


class HomeScreen(Screen):
    """ The HomeScreen widget is the first view loaded of the UI.
    """
    message_input = ObjectProperty(None)
    message_display = ObjectProperty(None)
    url_name = ObjectProperty(None)

    def __init__(self, **kwargs):
        """ Creates all the initial conditions for the HomeScreen.
        """
        # TODO: What does this *super* call do exactly?
        super(HomeScreen, self).__init__(**kwargs)

    def on_enter(self, data):
        self.download(data)

    def download(self, data):
        print("Get it.")
        req_url = data.text
        data.text = ""
        req = requests.get("https://" + req_url)

        content = str(req.content)

        myFile = open("save.html", "w")
        myFile.write(content)
        myFile.close()

# DONE: This class creates the Main Application!
class DownloaderApp(App):
    def build(self):
        return HomeScreen()


# The following lines instantiate and run the application.
if __name__ == "__main__":
    app = DownloaderApp()
    #print(app)
    app.run()
