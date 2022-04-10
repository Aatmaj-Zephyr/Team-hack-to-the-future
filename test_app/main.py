'''
Project Vwatch-
This project identifies using face detection if the person standing at the doorstep of our home is a known person or an unknown person.
For more info- Read the README at the bottom of this file.
The entire source code is available at https://github.com/Aatmaj-Zephyr/Team-hack-to-the-future

===========================================================
Made with love by Team Hack to the Future-
- Aatmaj Zephyr
- Ritvik Jindal
- Rahul Dandhona
- Atharva Karawade
'''
#import necessary imports

#kivy imports
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
import kivy.animation as animation
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage

#other imports

import face_recognition
import cv2
import numpy as np
import pickle
import time

#setting up
Config.set('graphics', 'resizable', True)

#global data
#create a float layout

def appear(widget,duration):
    #make the widget visible
    #animate widget
    animation.Animation(opacity=1, duration=duration).start(widget)

def decline(self):
    #when the user presses decline
    #add sounds here
    #turn on the camera
    Camera_on_Layout(self)
    camera_on()

def accept(self):
    #when the user presses accept
    Camera_off_Layout(self)

    #play sound
    sound = SoundLoader.load('test_app_accepted_karaw.mp3')
    sound.play()

    #wait for a second
    time.sleep(1)
    #turn on the camera
    Turn_on_CCTV_fun(self)
def unknown_bell_press():
    #when unknown person presses the bell
    #play sound
    sound = SoundLoader.load('test_app_bell-known-person.mp3')
    sound.play()
    #add warning to the user
    appear(warning_label,2)
    appear(warning_Button,2)

    #add sounds here
    print("bell pressed")

    #show and hide appropriate widgets
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
    #set the person label
    person_label.text = name
    
def known_bell_press(name):
    #when known person presses the bell

    #add sounds here
    print("bell pressed")
    
    #show and hide appropriate widgets
    hide_widget(Turn_off_CCTV, False)
    hide_widget(Turn_on_CCTV, True)
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


def Turn_on_CCTV_fun(self):
    #turn on the camera
    
    #play sound
    sound = SoundLoader.load('test_app_Button-click-sound.mp3')
    sound.play()
    
    
    while True:
        hide_widget(accept_Button, False)
        hide_widget(decline_Button, True)
        hide_widget(accept_label, True)
        hide_widget(decline_label, True)
        hide_widget(person_label, True)
        hide_widget(warning_Button, True)
        hide_widget(warning_label, True)
        hide_widget(background_image_box_accept, True)
        hide_widget(background_image_box_decline, True)
        hide_widget(Bell, True)
        value = detect()

        if (value == "unknown"):
            unknown_bell_press()
            break
        elif (value == "null"):
            continue
        else:
            known_bell_press(value)
            break




def Turn_off_CCTV_fun(self):
    #turn off the camera
    
    #play sound
    sound = SoundLoader.load('test_app_deny-unknown.mp3')
    sound.play()
    
    #show and hide appropriate widgets from the layout
    Camera_off_Layout(self)

def Camera_off_Layout(self):
    #turn off the camera
    
    #wait for a second
    time.sleep(1)
    
    #show and hide appropriate widgets
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
    #turn on the camera
    #show and hide appropriate widgets
    hide_widget(Turn_on_CCTV,True)
    hide_widget(Turn_off_CCTV,False)
   # unknown_bell_press() .....test code

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
    #blank function
    pass

def hide_widget(wid, dohide=True):
    #hide or show a widget
    if hasattr(wid, 'saved_attrs'):
        
        if not dohide:
            #Save the properties of the widget and then hide it
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
            del wid.saved_attrs
    elif dohide:
        #load the saved properties of the widget and then show it
        wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
        wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

person_float_layout = FloatLayout()
#make a float layout which is embedded in the main layout

background_image = AsyncImage(source='wallpaper.jpeg', allow_stretch=True, keep_ratio=False)
#make a background image which is AsyncImage.

person_float_layout.add_widget(background_image)
#add the background image to the float layout


Bell = Label(text="There is someone at the door!", font_size=55, color="blue", size_hint=(.2, .2),
                     pos_hint={'center_x': 0.5, 'center_y': 0.85})
#make a label which is notifies the use about the presence of a person at the door.
person_float_layout.add_widget(Bell)
#add the label to the float layout

background_image_box_accept = Image(source='images copy.jpeg', allow_stretch=True, keep_ratio=False,
                         opacity=0.3, size_hint=(.8, .6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
#make a background image which is to be put in the background of the screen if the user accepts..
person_float_layout.add_widget(background_image_box_accept)
#add the background image to the float layout

background_image_box_decline = Image(source='unknown.jpeg', allow_stretch=True, keep_ratio=False,
                             opacity=0.3, size_hint=(.8, .6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
#make a background image which is to be put in the background of the screen if the user declines..
person_float_layout.add_widget(background_image_box_decline)
#add the background image to the float layout

person_label = Label(text="Unidentified Access!!",bold=True, font_size=60,color="red", size_hint=(.2, .2), pos_hint={'center_x':0.5, 'center_y':0.5})
#make a label to warn the user that the person is not known.
person_float_layout.add_widget(person_label)
#add the label to the float layout

accept_Button=Image(source ='icons8-login-64.png',pos_hint={'center_x':0.8, 'center_y':0.30})
#make a logo to accept the access.
person_float_layout.add_widget(accept_Button)
#add the logo to the float layout

accept_label=Button(text="accept",background_color=(0, 0, 0, 0),size_hint=(0.20, 0.15),on_press=accept,font_size=40,bold=True,color="green",pos_hint={'center_x':0.8, 'center_y':0.25})
#make a button to accept the access.
person_float_layout.add_widget(accept_label)
#add the button to the float layout

decline_Button = Image(source='icons8-close-64.png', on_press=press,size_hint=(.2, .2),
                      pos_hint={'center_x': 0.2, 'center_y': 0.30})
#make a logo to decline the access.
person_float_layout.add_widget(decline_Button)
#add the logo to the float layout

decline_label = Button(text="decline",background_color=(0, 0, 0, 0),size_hint=(0.20, 0.15),on_press=decline,font_size=40,bold=True, color="red",  pos_hint={'center_x': 0.2, 'center_y': 0.25})
#make a button to decline the access.
person_float_layout.add_widget(decline_label)
#add the button to the float layout

#make a logo to warn the user that the person is not known.
warning_Button = Image(source='icons8-warning-64.png',
                       pos_hint={'center_x': 0.5, 'center_y': 0.70})
#make a logo to warn the user that the person is not known.
person_float_layout.add_widget(warning_Button)

#make a label to warn the user that the person is not known.
warning_label = Label(text="Warning!!", bold=True,font_size=40,color="red", size_hint=(.1, .1), pos_hint={'center_x': 0.5, 'center_y': 0.65})
#add the label to the float layout
person_float_layout.add_widget(warning_label)

Turn_on_CCTV = Button(text="Turn on CCTV", on_press=Turn_on_CCTV_fun,size_hint=(.5, .1),pos_hint={'center_x': 0.5, 'center_y': 0.2},background_color=(0,1,0,1))
#Button to turn on the CCTV.
person_float_layout.add_widget(Turn_on_CCTV)
#add the button to the float layout

Turn_off_CCTV = Button(text="Turn off CCTV", on_press=Turn_off_CCTV_fun,size_hint=(.5, .1), pos_hint={'center_x': 0.5, 'center_y': 0.1},background_color=(1,0,0,1))
#button to turn off the CCTV.
person_float_layout.add_widget(Turn_off_CCTV)
#add the button to the float layout

#add the float layout to the main layout
class DemoApp(App):
    #make a class for the app
    def build(self):
        #build the app
        float = FloatLayout()
        #make a float layout for the background
        float.add_widget(person_float_layout)
        #add the float layout to the main layout
        return float
    #return the main layout
    
Camera_off_Layout(None)
#call the function to make the camera off layout

#play sound for opening of the app
sound = SoundLoader.load('test_app_app-opening.wav')
sound.play()


#machine learning part
pickle_file=open("ref_name.pkl" , "rb")
#open the pickle_file to read the names of the people
ref_dictt=pickle.load(pickle_file)
#read the names of the people
pickle_file.close()
#close the first pickle file ! Do not forget to close the file after you are done with it.
pickle_file=open("ref_embed.pkl","rb")
#open the pickle_file to read the embeddings of the people
embed_dictt=pickle.load(pickle_file)
#read the embeddings of the people
pickle_file.close()
#close the second pickle file ! Do not forget to close the file after you are done with it.


known_face_encodings = []
#make an empty list to store the embeddings of the people
known_face_names = []
#make an empty list to store the names of the people
for ref_id , embed_list in embed_dictt.items():
    #for each person in the embeddings
    for my_embed in embed_list:
        #add the embedding of the person to the list
        known_face_encodings +=[my_embed]
        #add the name of the person to the list
        known_face_names += [ref_id]

def camera_on():
    #function to turn on the camera
   while True:
       #Until value is on...
        value=detect()

        if(value=="unknown"):
            #unknown person has accessed the door
            unknown_bell_press()
            #call the function to say unknown person
            break
        elif(value=="null"):
            #no person has accessed the door yet
            continue
        else:
            #known person has accessed the door
            known_bell_press(value)
            break

def most_common_element(lst):
    #function to find the most common element in a list
    return max(set(lst), key=lst.count)

def detect():
    #function to detect the person
    detect_list=[]
    #make an empty list to store the names of the people
    known_face_encodings = []
    #make an empty list to store the embeddings of the people
    known_face_names = []
    #make an empty list to store the names of the people
    for ref_id, embed_list in embed_dictt.items():
        #for each person in the embeddings
        for my_embed in embed_list:
            #add the embedding of the person to the list
            known_face_encodings += [my_embed]
            #add the name of the person to the list
            known_face_names += [ref_id]
            #make a list to store the names of the people

    video_capture = cv2.VideoCapture(0)
    #make a video capture object to capture the video from the camera

    process_this_frame = True
    #make a boolean variable to check if the frame is to be processed or not

    for i in range(0,10):
        try:
            #try to capture the frame
            ret, frame = video_capture.read()
            #read the frame
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            #resize the frame
            rgb_small_frame = small_frame[:, :, ::-1]
            #convert the frame to RGB

            if process_this_frame:
                #if the frame is to be processed

                face_locations = face_recognition.face_locations(rgb_small_frame)
                #find the face locations
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                #find the face encodings

                face_names = []
                #make a list to store the names of the people

                if (len(face_encodings) != 0):
                    #if there are faces in the frame
                    for face_encoding in face_encodings:
                        #for each face in the frame
                        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                        #find the matches


                        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                        #find the distances
                        best_match_index = np.argmin(face_distances)
                        #find the index of the best match
                        if matches[best_match_index]:
                            #if the best match is a match
                            name = known_face_names[best_match_index]
                            #get the name of the person
                        face_names.append(name)
                        #add the name of the person to the list
                else:
                    #if there are no faces in the frame
                    print("null")
                    #print null
                    detect_list.append("null")
                    #add null to the list
                    continue
                    #continue to the next frame

            process_this_frame = not process_this_frame
            #change the value of the boolean variable

            cv2.imshow('Video', frame)
            #show the frame

            print(ref_dictt[name])
            #print the name of the person

            detect_list.append(ref_dictt[name])
            #add the name of the person to the list

        except:
            #if the frame is not captured
            print("unknown")
            #The user is not recognized
            detect_list.append("unknown")
            #add unknown to the list

        if cv2.waitKey(1) & 0xFF == ord('q'):
            #if the user presses q
            break
            #break the loop and quit the camera

    video_capture.release()
    #release the camera
    cv2.destroyAllWindows()
    #destroy all the windows
    print()
    #print a new line to separate the output
    most_value= most_common_element(detect_list)#most repeated value
   # print("The person is: ", most_value)   .....test code

    if(all(ele == detect_list[0] for ele in detect_list)):
        #if all the elements in the list are the same
        print(detect_list[0])
        #print the first element
    print(most_value)
    #print the most repeated value

    return most_value
    #return the most repeated value

App = DemoApp()
#make a new instance of the class
App.run()
#run the app

'''
README

-----------------------------------------------------------------------------------------------------------------------
# Wait,Watch,Enable!

Stay alert, don't get hurt ! Now that the covid pandemic which rocked the world is coming to an end, things are returning to normalcy with the working sector being reopened again.
However, home theft and robbery has been surging up to new records as the older generations as well as young kids being home alone,are getting more and more vulnerable. 

To solve this rising problem and provide a sense of safety to the vulnerable demographic...We , team HACK TO THE FUTURE have developed a mobile application called WaIT,Watch,Enable!

Working of Application:

Whenever a person arrives at the front door,the cctv camera installed detects his/her face. An old /spare mobile is attached to the doorframe inside the house which takes the data from the cctv and using face detection tech , identifies whether the person is an insider or a stranger and notifies thorugh the app.

If its an acquaintance, then the app displays the name of the person and thus, guarantees that its a person the user is acquainted with. The user has an option to accept or deny the notification. If accepted,then the user can open the door and a notification is sent to the caretaker of the house with the details of the person.If its a stranger, then the user can simply deny the request.

Key Features of Application:
1) Safeguards the older demographic as well the young agegroup
    
Senior citizens , around the 60+ age group experience mental problems and are vulnerable to thefts. This app would greatly benefit them to provide them safety in their own residence.
        Younger children generally are brash,naive and quite impulsive and hence, prone to crimes such as kidnapping , thus this app would be a relief to parents!
        
2) Promotes reusability of older smartphones,thus conserving resources.

An older android compatible smartphone can be fixed on the door frame and be used to run the application.  
    
3) Has colourful and easy to use interface, thus enriching user experience to the fullest
     
Has minimalistic buttons and bright colors used to appeal to the users which appeal to the targeted demographic and vastly enhances the user experience.       

 Tools and frameworks used :
1) Python 
2) Kivy 
3) OpenCV 
4) Buildozer 

'''






