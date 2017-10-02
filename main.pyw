from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import  Label
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
import helper as hlp

talk  = hlp.Talk()

Builder.load_string("""
<ScreenUI>:
    orientation: 'lr-tb'
    Button:
        text: 'get'
        on_press: root.get_touch()
        size: 200, 50
        size_hint: None, None
    Button:
        id: post_
        text: 'post'
        on_press: root.post_touch()
        size_hint: None, None
        size: 200, 50
    Button:
        id: put_
        text: 'put'
        size_hint: None, None
        size: 200, 50
    Button:
        id: login
        text: 'login'
        on_press: root.login_touch()
        size_hint: None, None
        size: 200, 50
    TextInput:
        text: '/serwisy/mapi/pacjent'
        id: met
        size_hint: None, None
        size: 800, 30
    Label:
        text: 'editor'
        size_hint: None, None
        size: 800, 30
    TextInput:
        id: input_
        text: 'put something here'
        size_hint: None, None
        size: 800, 200
    Label:
        text: 'server output'
        size_hint: None, None
        size: 800, 30
    TextInput:
        id: output_
        text: 'put something here'
        size_hint: None, None
        size: 800, 270
        """)

class ScreenUI(StackLayout):
    def post_touch(self):
        print  self.ids.input_.text
    def get_touch(self):
        m = self.ids.met.text
        r=unicode(talk.get_(m))
        self.ids.output_.text=r
    def  login_touch(self):
        r=talk.login_()
        self.ids.output_.text=r
        

class WidgetApp(App):

    def build(self):
        app = ScreenUI()
        return app
    
if __name__ == '__main__':
    WidgetApp().run()
