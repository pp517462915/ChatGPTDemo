import multiprocessing
import pyttsx3
import time
from threading import Thread



def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread

    return wrapper


def speak(text):
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


def stop_speaker():
    global term
    term = True
    t.join()


@threaded
def manage_process(p):
    global term
    while p.is_alive():
        if term:
            p.terminate()
            term = False
        else:
            continue


def text_to_voice_pyttsx3(text):
    time.sleep(0.5)
    global t
    global term
    term = False
    p = multiprocessing.Process(target=speak, args=(text,))
    p.start()
    t = manage_process(p)


if __name__ == "__main__":
    text_to_voice_pyttsx3("s an AI language model, I cannot physically book a trip for you, but I can provide you with some general information on the cost of traveling to Beijing.")
    time.sleep(1)
    stop_speaker()
    text_to_voice_pyttsx3("this process is running right now")
    time.sleep(1.5)
    stop_speaker()