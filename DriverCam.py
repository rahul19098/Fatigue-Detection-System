from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.switch import Switch
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.camera import Camera
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
import cv2
import os
from pygame import mixer
import time

class DriverCamApp(App):
    audio = r"C:\Users\ravin\Desktop\Fatique\audio\5.wav"

    def build(self):
        layout = FloatLayout()

        # Background image
        image = Image(source='bg.jpg', size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(image)

        # Buttons
        open_camera_btn = Button(text='Open Cam', size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'y': 0.8})
        open_camera_btn.bind(on_press=self.open_camera)
        layout.add_widget(open_camera_btn)

        open_record_btn = Button(text='Open Cam & Record', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.7})
        open_record_btn.bind(on_press=self.open_camera_record)
        layout.add_widget(open_record_btn)

        open_detect_btn = Button(text='Open Cam & Detect', size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5, 'y': 0.6})
        open_detect_btn.bind(on_press=self.open_camera_detect)
        layout.add_widget(open_detect_btn)

        detect_record_btn = Button(text='Detect & Record', size_hint=(None, None), size=(150, 50), pos_hint={'center_x': 0.5, 'y': 0.5})
        detect_record_btn.bind(on_press=self.detect_and_record)
        layout.add_widget(detect_record_btn)

        detect_blink_btn = Button(text='Detect Eye Blink & Record With Sound', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'y': 0.4})
        detect_blink_btn.bind(on_press=self.detect_blink_record)
        layout.add_widget(detect_blink_btn)
        
        # toggle_button1 = ToggleButton(text='customize alerm sound', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'y': 0.3})
        # toggle_button1.bind(on_press=self.check_state)
        # layout.add_widget(toggle_button1)

        self.file_chooser = FileChooserListView()
        self.popup = Popup(content=self.file_chooser, title="Select a File", size_hint=(None, None), size=(400, 400))

        Cbutton = Button(text='customize alerm sound', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.5, 'y': 0.3})
        Cbutton.bind(on_press=self.open_file_selector)
        layout.add_widget(Cbutton)
        
        # Other widgets
        # label = Label(text='Change Alert Sound', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.4, 'y': 0.3}, color=(0, 0, 0, 1))
        # layout.add_widget(label)

        # toggle_switch = Switch(active=False, size_hint=(None, None), size=(300, 50), pos_hint={'center_x': 0.6, 'y': 0.3})
        # toggle_switch.bind(active=self.on_toggle)
        # layout.add_widget(toggle_switch)

        exit_btn = Button(text='EXIT', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'y': 0.1})
        exit_btn.bind(on_press=self.stop)
        layout.add_widget(exit_btn)

        return layout


    def on_toggle(self, instance, value):
        self.switch_active = value
        if value:
            print("Switch is ON")
        else:
            print("Switch is OFF")

    def open_camera(self, instance):
        capture = cv2.VideoCapture(0)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)  # Create a resizable window
        
        while True:
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Add a close button at the bottom center
            # cv2.rectangle(frame, (200, 440), (440, 480), (0, 0, 255), -1)
            # cv2.putText(frame, 'CLOSE', (265, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
            
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            
            if key & 0xFF == ord('q'):  # Press 'q' to quit
                break
            elif key == ord('c'):  # Press 'c' to close the window
                cv2.destroyAllWindows()
                return
            
        capture.release()
        cv2.destroyAllWindows()


    def open_camera_record(self, instance):
        capture = cv2.VideoCapture(0)
        # resolution = (1280, 720)  
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        op = cv2.VideoWriter(r'C:\Users\DELL\Desktop\Driver\Sample1.avi', fourcc, 11.0, (640, 480))
        while True:
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # frame = cv2.resize(frame, resolution)
            cv2.imshow('frame', frame)
            op.write(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        op.release()
        capture.release()
        cv2.destroyAllWindows()   

    def open_camera_detect(self, instance):
        capture = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\lbpcascade_frontalface.xml')
        eye_glass = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\haarcascade_eye_tree_eyeglasses.xml')
        while True:
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, 'Face', (x+w, y+h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eye_g = eye_glass.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eye_g:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()

    def detect_and_record(self, instance):
        capture = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\lbpcascade_frontalface.xml')
        eye_glass = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\haarcascade_eye_tree_eyeglasses.xml')
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        op = cv2.VideoWriter(r'C:\Users\ravin\Desktop\Fatique\NewSample2.avi', fourcc, 9.0, (640, 480))
        while True:
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, 'Face', (x+w, y+h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eye_g = eye_glass.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eye_g:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            op.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xff == ord('q'):
                break
        op.release()
        capture.release()
        cv2.destroyAllWindows()

    def detect_blink_record(self, instance):        
        capture = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\lbpcascade_frontalface.xml')
        eye_cascade = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\haarcascade_eye.xml')
        blink_cascade = cv2.CascadeClassifier(r'C:\Users\ravin\Desktop\Fatique\CustomBlinkCascade.xml')

        print(DriverCamApp.audio)
        while True:
            ret, frame = capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, 'Face', (x+w, y+h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
                blink = blink_cascade.detectMultiScale(roi_gray)
                for (eyx, eyy, eyw, eyh) in blink:
                    cv2.rectangle(roi_color, (eyx, eyy), (eyx+eyw, eyy+eyh), (255, 255, 0), 2)
                    
                    self.alert(DriverCamApp.audio)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        capture.release()
        cv2.destroyAllWindows()

    def open_file_selector(self, instance):
        self.popup.open()
        self.file_chooser.bind(on_submit=self.on_file_selected)

    def on_file_selected(self, *instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0]
        if selected_file:
            print("Selected file:", selected_file)
            DriverCamApp.audio = selected_file
        self.popup.dismiss()


    def alert(self, sound_file="5.wav"):
        # path=os.path.join(r"C:\Users\ravin\Desktop\Fatique",sound_file)
        mixer.init()
        alert = mixer.Sound(sound_file)
        alert.play()
        time.sleep(0.1)
        alert.play()    
    




if __name__ == '__main__':
    DriverCamApp().run()
