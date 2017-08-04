#:kivy 1.6.0
<TtsDemo>:
    orientation: 'vertical'
    speek: speak
    padding: root.width * 0.02, root.height * 0.02
    spacing: 10
    canvas:
        Rectangle:
            source: 'images/background.png'
            pos: self.pos
            size: self.size
    Label:
        text: 'Kivy text to speech'
        font_size: '45sp'
        size_hint: 1, None
    TextInput:
        id: speak
        text: 'Hi! How are you?'
        multiline: True
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, None
        Button:
            text: 'Speak Up!'
            size_hint: 1, None
            on_press: root.say(speak.text)
        Button:
            text: 'Clear'
            size_hint: 1, None
            on_press: root.clear()