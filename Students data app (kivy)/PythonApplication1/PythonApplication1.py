import kivy
from kivy.app import app
from kivy.uix.gridlayout import Gridlayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix,button import button
class Grid(GridLayout):
    def __init__(self,**kwargs):
        super(Grid,self).__init__()
        self.cols=2
        self.add_widgets(Label(text="Student's Name: "))
        self.s_name=TextInput()
        self.add_widgets(self.s_name)
        self.add_widgets(Label(text="Student's Marks: "))
        self.s_marks=TextInput()
        self.add_widgets(self.s_marks)
        self.add_widgets(Label(text="Student's Gender: "))
        self.s_gender = TextInput()
        self.add_widgets(s_gender)
        self.press= Button(text="Click me")
        self.press.bind(on_press=self.click_me)
        self.add_widgets(self.press)
    def click_me(self):
        print(f"The name is {self.s_name} and his marks are {self.s_marks} and has a gender {self.s_gender}")
class First_App(app):
    def build(self):
        return Grid()
if __name__="__main__":
    First_App().run()