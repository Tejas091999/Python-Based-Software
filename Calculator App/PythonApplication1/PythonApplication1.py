from pickle import NONE
from turtle import bgcolor, right
from kivy.app import app
from kivy.uix.Boxlayout import Boxlayout
from kivy.uix.button import Button
from kivy.uix.textInput import TextInput 
class Cal(App):
    def build(self):
        self.operators = ["/","*","+","-"]
        self.last_was_operator=None
        self.last_button=None
        cal_layout = Boxlayout(orientation="vertical")
        self.solution= TextInput(bg_color="black",fg_color="white",font_size=45,multiline=False,halign=right)
        cal_layout.add_widgets(self.solution) 
        buttons =[["7","8","9","/"]
                  ["4","5","6","*"]
                  ["1","2","3","-"]
                  [".","0","C","+"]]
        for row in buttons:
            h_layout = Boxlayout
            for label in row:
                button=Button(
                    text=label,font_szie=30,bg_color="white",
                    post_hint={"center_x=0.5","center_y:0.5"})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widgets(button)
            cal_layout.add_widgets(h_layout)
        equal_button=Button( text="=",font_szie=30,bg_color="white",
                    post_hint={"center_x=0.5","center_y:0.5"})
        equal_button.bind(on_press=self.on_solution)
        cal_layout.add_widgets(equal_button)
        return cal_layout 
    def on_button_press(self,instance):
        current = self.solution.text
        button.text= instance.text
        if button_text=="C":
            self.solution.text=""
        else:
            if current and(
                self.last_was_operator and button_text in self.operators):
                return 
            elif current == "" and buttn_text in self.operators:
                return
            else:
                new_text= current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_one_operator = self.last_button in self.operators
    def on_solution(self,instance):
        text=self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

if __name__=="__main__":
    app=Cal()
    app.run()
