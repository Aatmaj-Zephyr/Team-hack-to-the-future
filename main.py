#import necessary imports
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput

from kivy.config import Config

Config.set('graphics', 'resizable', True)
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
def press(instance, touch):
    print("pressed")
def initiate_Normal_layout(float_layout):
    #create a float layout
    person_float_layout = FloatLayout()
    background_image = AsyncImage(source='wallpaper.jpeg', allow_stretch=True, keep_ratio=False)
    person_float_layout.add_widget(background_image)
    background_image = Image(source ='Unknown wallpaper.jpeg',on_touch_down=press,allow_stretch=True, keep_ratio=False,opacity = 0.3,size_hint=(.8, .5),pos_hint={'center_x':0.5, 'center_y':0.6})
    person_float_layout.add_widget(background_image)
    person_label = Label(text="Unidentified Access!!",font_size=55,color="blue", size_hint=(.2, .2), pos_hint={'center_x':0.5, 'center_y':0.5})
    person_float_layout.add_widget(person_label)
   # accept_Button= Button(text="accept",size_hint=(.1,.1),pos_hint={'center_x':0.8, 'center_y':0.30},background_color=(0,1,0,1))
    accept_Button=Image(source ='icons8-login-64.png',on_touch_down=press,pos_hint={'center_x':0.8, 'center_y':0.30})
    person_float_layout.add_widget(accept_Button)
    accept_label=Label(text="accept",font_size=35,bold=True,color="green",size_hint=(.1,.1),pos_hint={'center_x':0.8, 'center_y':0.25})
    person_float_layout.add_widget(accept_label)


    decline_Button = Image(source='icons8-close-64.png', on_touch_down=press,
                          pos_hint={'center_x': 0.2, 'center_y': 0.30})
    person_float_layout.add_widget(decline_Button)
    decline_label = Label(text="decline",font_size=35,bold=True, color="red", size_hint=(.1, .1), pos_hint={'center_x': 0.2, 'center_y': 0.25})
    person_float_layout.add_widget(decline_label)

    decline_Button = Image(source='icons8-warning-64.png', on_touch_down=press,
                           pos_hint={'center_x': 0.5, 'center_y': 0.70})
    person_float_layout.add_widget(decline_Button)
    decline_label = Label(text="Warning!!", bold=True,font_size=35,color="red", size_hint=(.1, .1), pos_hint={'center_x': 0.5, 'center_y': 0.65})
    person_float_layout.add_widget(decline_label)

    Turn_on_CCTV = Button(text="Turn on CCTV", size_hint=(.5, .2),pos_hint={'center_x': 0.5, 'center_y': .5},background_color=(0,1,0,1))
    person_float_layout.add_widget(Turn_on_CCTV)
    Turn_off_CCTV = Button(text="Turn off CCTV", size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.1},background_color=(1,0,0,1))
    person_float_layout.add_widget(Turn_off_CCTV)
    hide_widget(Turn_on_CCTV,True)
    #add the float layout to the main layout
    float_layout.add_widget(person_float_layout)
#create class for the main window

def hide_widget(wid, dohide=True):
    if hasattr(wid, 'saved_attrs'):
        if not dohide:
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
            del wid.saved_attrs
    elif dohide:
        wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
        wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

class DemoApp(App):
    def build(self):
        float = FloatLayout()

        initiate_Normal_layout(float)

        return float

# run the app
App = DemoApp()
App.run()
