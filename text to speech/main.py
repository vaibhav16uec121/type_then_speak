import kivy
kivy.require('1.6.0')


from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.properties import ObjectProperty


from components.initialize import InitializePlatform
from components.ttsspeak import TtsSpeak


class text2speech(BoxLayout):
    speak = ObjectProperty(None)

    def clear(self):
        self.speak.text = ""
        self.speak.focus = True
		
	def say(self, text):
        TtsSpeak(text).speak()	

class text2speechApp(App):
    def build(self):
        InitializePlatform()
        return text2speech()
    

if __name__ == '__main__':
    text2speechApp().run()