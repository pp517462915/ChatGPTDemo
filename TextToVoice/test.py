import threading
import time

import pyttsx3
from gtts import gTTS
import os
from win32com.client import Dispatch
from playsound import playsound


def stop_pyttsx3_engine():
    engine = pyttsx3.init()
    time.sleep(0.5)

    if engine._inLoop:
        engine.endLoop()

def text_to_voice_pyttsx3(text):

    # engine.startLoop(True)
    stop_pyttsx3_engine()
    thread = threading.Thread(target=excute_text_to_voice_pyttsx3, kwargs={"text": text})
    thread.start()

    # if engine._inLoop:
    #     engine.endLoop()


def excute_text_to_voice_pyttsx3(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Set the speech rate
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)

    # """VOLUME"""
    # volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    # """VOICE"""
    # voices = engine.getProperty('voices')  # getting details of current voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)  # changing index, changes voices. 1 for female

    # Say something
    engine.say(text)

    # Run and wait for the speech to finish
    engine.runAndWait()
    engine.stop()




def text_to_voice_gtts(text):
    tts = gTTS(text = text, lang = 'en')
    file_path = "C:\\Users\\pp517\\PycharmProjects\\ChatGPTDemo\\TextToVoice\\pcvoice.mp3"
    delete_file(file_path)
    tts.save(file_path)
    # to start the file from python
    playsound(file_path)
    delete_file(file_path)
    # playsound("pcvoice.mp3")
    # os.system("start pcvoice.mp3")

start_text_to_voice_window = 0
def text_to_voice_window(text):
    speaker = Dispatch("SAPI.SpVoice")
    global start_text_to_voice_window
    if not start_text_to_voice_window:
        excute_text_to_voice_window(speaker, "start load voice device")
        start_text_to_voice_window += 1

    thread = threading.Thread(target=excute_text_to_voice_window, kwargs={"speaker" : speaker, "text": text})
    thread.start()


def excute_text_to_voice_window(speaker, text):
    speaker.speak(text)

def delete_file(file_path):
    # Checking if file exists or not
    if os.path.exists(file_path):

        # Delete the file
        os.remove(file_path)

if __name__ == '__main__':
    # text_to_voice_gtts("")
    # text_to_voice_window("")
    # for i in range(2):
    #     text_to_voice_window("test")

    # speaker = Dispatch("SAPI.SpVoice")
    # print(speaker.GetVoices().Item(1).GetDescription())
    # # speaker = Dispatch(speaker.GetVoices().Item(1).GetDescription())
    # speaker.speak("test")

    # engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice)
    # engine.setProperty("voice", voices[3].id)
    # engine.say("Hello World!")
    # engine.runAndWait()
    # engine.stop()
    # text_to_voice_pyttsx3("test")

    # for i in range(2):
    #     text_to_voice_pyttsx3("test")

    text_to_voice_pyttsx3("test21231231")
    time.sleep(0.5)
    text_to_voice_pyttsx3("test21231231")
    # text_to_voice_pyttsx3("test21231231")
