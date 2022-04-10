#import necessary imports
import time

from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.textinput import TextInput
CCTV=False
from kivy.config import Config
import kivy.animation as animation
Config.set('graphics', 'resizable', True)
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.animation import Animation


def press(self):
    print("pressed")
#global data
#create a float layout

def appear(widget,duration):
    #animate widget
    animation.Animation(opacity=1, duration=duration).start(widget)

def decline(self):

    Camera_on_Layout(self)
def accept(self):
    sound = SoundLoader.load('accepted_karaw.mp3')
    sound.play()
    Camera_off_Layout(self)
    Turn_on_CCTV_fun(self)
def unknown_bell_press():
    sound = SoundLoader.load('bell-known-person.mp3')
    sound.play()
    appear(warning_label,2)
    appear(warning_Button,2)
    #add sounds here
    print("bell pressed")
    hide_widget(Turn_on_CCTV,True)
    hide_widget(Turn_off_CCTV,False)
    hide_widget(warning_Button,False)
    hide_widget(warning_label,False)
    hide_widget(accept_Button,False)
    hide_widget(accept_label,False)
    hide_widget(decline_Button,False)
    hide_widget(decline_label,False)
    hide_widget(person_label,False)
    hide_widget(background_image_box_accept,True)
    hide_widget(background_image_box_decline,False)
    hide_widget(Bell,False)
    hide_widget(background_image,False)
    hide_widget(person_float_layout,False)
    set_person(person_label,"Unidentified Access!!")
    person_label.color="red"

def set_person(person_label,name):
    person_label.text = name
def known_bell_press(name):

    #add sounds here
    print("bell pressed")
    hide_widget(Turn_off_CCTV, False)
    hide_widget(warning_Button, True)
    hide_widget(warning_label, True)
    hide_widget(accept_Button, False)
    hide_widget(accept_label, False)
    hide_widget(decline_Button, False)
    hide_widget(decline_label, False)
    hide_widget(person_label, False)
    hide_widget(background_image_box_accept, False)
    hide_widget(background_image_box_decline, True)
    hide_widget(Bell, False)
    hide_widget(background_image, False)
    hide_widget(person_float_layout, False)
    set_person(person_label,name)
    person_label.color="blue"

def camera_off():
  CCTV=False
#create class for the main window
def Turn_on_CCTV_fun(self):
    sound = SoundLoader.load('Button-click-sound.mp3')
    sound.play()

    camera_on()


def Turn_off_CCTV_fun(self):
    sound = SoundLoader.load('deny-unknown.mp3')
    sound.play()
    Camera_off_Layout(self)
    camera_off()

def Camera_off_Layout(self):
    #wait for a second
    time.sleep(1)

    hide_widget(Turn_on_CCTV,False)

    hide_widget(Turn_off_CCTV,True)
    hide_widget(accept_Button,True)
    hide_widget(decline_Button,True)
    hide_widget(accept_label,True)
    hide_widget(decline_label,True)
    hide_widget(person_label,True)
    hide_widget(warning_Button,True)
    hide_widget(warning_label,True)
    hide_widget(background_image_box_accept,True)
    hide_widget(background_image_box_decline,True)
    hide_widget(Bell,True)
def Camera_on_Layout(self):
    hide_widget(Turn_on_CCTV,True)
    hide_widget(Turn_off_CCTV,False)
   # unknown_bell_press() test code

    #hide all other widgets
    hide_widget(accept_Button,True)
    hide_widget(decline_Button,True)
    hide_widget(accept_label,True)
    hide_widget(decline_label,True)
    hide_widget(person_label,True)
    hide_widget(warning_Button,True)
    hide_widget(warning_label,True)
    hide_widget(background_image_box_accept,True)
    hide_widget(background_image_box_decline,True)
    hide_widget(Bell,True)
def blank():
    pass
def hide_widget(wid, dohide=True):
    #hide and disable widget
    if hasattr(wid, 'saved_attrs'):
        if not dohide:
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
            del wid.saved_attrs
    elif dohide:
        wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
        wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

person_float_layout = FloatLayout()
background_image = AsyncImage(source='wallpaper.jpeg', allow_stretch=True, keep_ratio=False)
person_float_layout.add_widget(background_image)
Bell = Label(text="There is someone at the door!", font_size=55, color="blue", size_hint=(.2, .2),
                     pos_hint={'center_x': 0.5, 'center_y': 0.85})
person_float_layout.add_widget(Bell)

background_image_box_accept = Image(source='images copy.jpeg', allow_stretch=True, keep_ratio=False,
                         opacity=0.3, size_hint=(.8, .6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
person_float_layout.add_widget(background_image_box_accept)
background_image_box_decline = Image(source='unknown.jpeg', allow_stretch=True, keep_ratio=False,
                             opacity=0.3, size_hint=(.8, .6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
person_float_layout.add_widget(background_image_box_decline)
person_label = Label(text="Unidentified Access!!",bold=True, font_size=60,color="red", size_hint=(.2, .2), pos_hint={'center_x':0.5, 'center_y':0.5})
person_float_layout.add_widget(person_label)
accept_Button=Image(source ='icons8-login-64.png',pos_hint={'center_x':0.8, 'center_y':0.30})
person_float_layout.add_widget(accept_Button)
accept_label=Button(text="accept",background_color=(0, 0, 0, 0),size_hint=(0.20, 0.15),on_press=accept,font_size=40,bold=True,color="green",pos_hint={'center_x':0.8, 'center_y':0.25})
person_float_layout.add_widget(accept_label)


decline_Button = Image(source='icons8-close-64.png', on_press=press,size_hint=(.2, .2),
                      pos_hint={'center_x': 0.2, 'center_y': 0.30})
person_float_layout.add_widget(decline_Button)
decline_label = Button(text="decline",background_color=(0, 0, 0, 0),size_hint=(0.20, 0.15),on_press=decline,font_size=40,bold=True, color="red",  pos_hint={'center_x': 0.2, 'center_y': 0.25})
person_float_layout.add_widget(decline_label)

warning_Button = Image(source='icons8-warning-64.png',
                       pos_hint={'center_x': 0.5, 'center_y': 0.70})
person_float_layout.add_widget(warning_Button)
warning_label = Label(text="Warning!!", bold=True,font_size=40,color="red", size_hint=(.1, .1), pos_hint={'center_x': 0.5, 'center_y': 0.65})
person_float_layout.add_widget(warning_label)

Turn_on_CCTV = Button(text="Turn on CCTV", on_press=Turn_on_CCTV_fun,size_hint=(.5, .1),pos_hint={'center_x': 0.5, 'center_y': 0.2},background_color=(0,1,0,1))
person_float_layout.add_widget(Turn_on_CCTV)
Turn_off_CCTV = Button(text="Turn off CCTV", on_press=Turn_off_CCTV_fun,size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.1},background_color=(1,0,0,1))
person_float_layout.add_widget(Turn_off_CCTV)
#add the float layout to the main layout
class DemoApp(App):
    def build(self):
        float = FloatLayout()

        float.add_widget(person_float_layout)

        return float
Camera_off_Layout(None)
sound = SoundLoader.load('app-opening.wav')
sound.play()
# run the app


import face_recognition
import cv2
import numpy as np
import glob
import pickle
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.uix.camera import Camera


f=open("ref_name.pkl" , "rb")
ref_dictt=pickle.load(f)
f.close()
f=open("ref_embed.pkl","rb")
embed_dictt=pickle.load(f)
f.close()


known_face_encodings = []
known_face_names = []
for ref_id , embed_list in embed_dictt.items():
    for my_embed in embed_list:
        known_face_encodings +=[my_embed]
        known_face_names += [ref_id]
def camera_on():
    while True:
        time.sleep(1)
        value=detect()

        if(value=="unknown"):
            unknown_bell_press()
            break
        elif(value=="null"):
            continue
        else:
            known_bell_press(value)
            break
def most_common_element(lst):
    return max(set(lst), key=lst.count)
def detect():
    detect_list=[]
    known_face_encodings = []
    known_face_names = []
    for ref_id, embed_list in embed_dictt.items():
        for my_embed in embed_list:
            known_face_encodings += [my_embed]
            known_face_names += [ref_id]

    video_capture = cv2.VideoCapture(0)

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    for i in range(0,20):
        try:
            ret, frame = video_capture.read()

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            if process_this_frame:

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                if (len(face_encodings) != 0):
                    for face_encoding in face_encodings:

                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        name = "Unknown"

                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        best_match_index = np.argmin(face_distances)
                        if matches[best_match_index]:
                            name = known_face_names[best_match_index]
                        face_names.append(name)
                else:
                    print("null")
                    detect_list.append("null")
                    continue

            process_this_frame = not process_this_frame


            print(ref_dictt[name])
            detect_list.append(ref_dictt[name])

        except:
            print("unknown")
            detect_list.append("unknown")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    print()
    most_value= most_common_element(detect_list)#most repeated value

    if(all(ele == detect_list[0] for ele in detect_list)):
        print(detect_list[0])
    print(most_value)

    return most_value

App = DemoApp()
App.run()







