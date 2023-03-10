# This is a sample Python script.
import time

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import openai
from VoiceInput.test import voice_input
from TextToVoice.test import text_to_voice_gtts
from TextToVoice.test2 import text_to_voice_pyttsx3
from TextToVoice.test2 import stop_speaker
import threading
import config

def chatGPTModel(question):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": question},
        ]
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    return result
    
def choice_helper():
    choice = input("Please choice voice input or word input:(v/w)")
    
    if choice.upper() == "V":
        text_to_voice_pyttsx3('load voice')
        while True:
            time.sleep(0.5)
            _ = input("Please press Enter to start speak.")
            stop_speaker()
            str = voice_input()
            if str.upper() == "STOP" or str.upper() == "QUIT":
                break
            print("--------------------------the answer----------------------------")
            answer = chatGPTModel(str)
            print(answer)
            # too slow
            # text_to_voice_gtts(answer)
            text_to_voice_pyttsx3(answer)
            print("--------------------------the answer----------------------------")
    elif choice.upper() == "W":
        while True:
            str = input("Enter your question(enter:N or NO to quit):")
            if str.upper() == "NO" or str.upper() == "N":
                break
            print("--------------------------the answer----------------------------")
            answer = chatGPTModel(str)
            print(answer)
            print("--------------------------the answer----------------------------")
        

if __name__ == '__main__':
    choice_helper()
    # text_to_voice_pyttsx3('load voice')
    # choice = input("Please choice voice input or word input:(v/w)")
    # while True:
    #     time.sleep(3)
    #     text_to_voice_pyttsx3('load voice')
