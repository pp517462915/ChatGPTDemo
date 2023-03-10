import speech_recognition as sr

def voice_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # try:
        text = r.recognize_google(audio)
        print("You said: ", text)
    # except sr.UnknownValueError:
    #     print("Oops! Didn't catch that")
    # except sr.RequestError as e:
    #     print("Uh oh! Could not request results from Google Speech Recognition service; {0}".format(e))

    return text


if __name__ == "__main__":
    voice_input()
