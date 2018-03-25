from tkinter import Tk, Entry, Button, INSERT, PhotoImage,Label
import speech_recognition as sr  # use google speech recognition program
from gtts import gTTS  # use google text-to-speech program
from pygame import mixer  # use the mixer to play computer's speech
from tkinter import Tk, Message
import time
import sys


root = Tk()
root.title('Spech recognition By Shahriar and Anik to Rajib Sir')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

#root.geometry("700x450+50+50")

#for image

img = PhotoImage(file='pic_shr_again.png')
my_image = Label(root, image=img)
my_image.pack(side='top')

#end image




# Print the contents of entry widget to console
def print_content():

    while True:  # continuously listen to user for  input

        r = sr.Recognizer()  # using the Recognizer program from speech recognition tool to recognize your speech
        with sr.Microphone()as source:  # turning the microphone as a listening source
            r.adjust_for_ambient_noise(source)  # this code cancels any background noise
            print('Talk now: ')  # Asks the user to start talking
            audio = r.listen(source)  # Recognizer listens to the microphone's source and stores that content in audio

        try:
            message = (
                r.recognize_google(
                    audio))  # takes the audio content to recognizes the user's speech and stores in message

            print(message)  # outputs and prints the user message, such as 'Hello', etc


            # GOOGLE TEXT TO SPEECH CODE RESPOND BACK TO YOU!  :)

            # condition to respond to "hello"
            if 'hello' in message:  # if google speech recognition hears hello from you
                speech = ('Hello, you look great')  # this is the text response to 'hello'
                tts = gTTS(text=speech, lang='en')  # convert above written text into speech
                tts.save(
                    'D:\\Shahriar\\Speech_Recognition\\hello.mp3')  # save speech in mp3 (change to your file location)
                mixer.init()  # start mixer to play mp3
                mixer.music.load('D:\\Shahriar\\Speech_Recognition\\hello.mp3')  # load file
                mixer.music.play()  # play file



            # condition to respond to "good morning"
            if 'good morning' in message:
                speech = ('Good Morning, how are you')
                tts = gTTS(text=speech, lang='en')
                tts.save('D:\\Shahriar\\Speech_Recognition\\morning_greeting.mp3')
                mixer.init()
                mixer.music.load('D:\\Shahriar\\Speech_Recognition\\morning_greeting.mp3')
                mixer.music.play()

             # condition to respond to "good morning"
            if 'Technology' in message:
                    speech = ('Please say a technology brand you wants to know')
                    tts = gTTS(text=speech, lang='en')
                    tts.save('D:\\Shahriar\\Speech_Recognition\\morning_greeting.mp3')
                    mixer.init()
                    mixer.music.load('D:\\Shahriar\\Speech_Recognition\\morning_greeting.mp3')
                    mixer.music.play()

        except Exception as e:  # throw an exception or error
            print("Could not understand")  # when user speech is meaningless

# Create a button that will print the contents of the entry
button = Button(root, text='Start Speech', command=print_content)
button.pack()
#Print Text
msg = Message(root, text="Project AIR")

# Font is a tuple of (font_family, size_in_points, style_modifier_string)
msg.config(font=('times', 48, 'italic bold underline'))

msg.pack()
my_text = Label(root, text='Sylhet international University')
my_text.pack(side='bottom')

root.mainloop()