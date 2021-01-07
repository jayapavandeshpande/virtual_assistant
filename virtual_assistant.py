# brew install portaudio
# pip3 install pyaudio
# pip3 install SpeechRecognition
# pip3 install gTTS
# pip3 install wikipedia
# pip3 install googlesearch-python

# import pyttsx3
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)


import speech_recognition as sr
from gtts import gTTS

import os
import warnings
import calendar
import random
import datetime
import wikipedia
import webbrowser
from subprocess import call

# ignore any warning
warnings.filterwarnings("ignore")

WAKE_WORDS = ["hey", "hi", "hai", "hello"]
BYE_WORDS = ["bye", "bhai"]
WEB_URLS = {"bugzilla": "https://bugzilla.eng.vmware.com", "google": "https://www.google.com",
            "maas": "http://maas.eng.vmware.com", "maps": "http://maas.eng.vmware.com",
            "confluence": "http://confluence.eng.vmware.com"}


# Record Audio and return string

def recordAudio():
    # Record Audio
    r = sr.Recognizer()

    #
    print(sr.Microphone.list_microphone_names())
    # start microphone recording
    with sr.Microphone() as source:
        print("Say Something !!!")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print(audio)

    # Convert Audio to string using google speech recog
    # data = ''
    try:
        data = r.recognize_google(audio)
        print("Recorded Speech {}".format(data))
        return data
    except Exception as e:
        print("Google speech recognition failed to understand Audio with Exception {}".format(e))


def response(text):
    print(text)

    # Convert Text to Speech
    obj = gTTS(text=text, lang='en', slow=False)

    # Save the Audio to file mp3 format
    obj.save("response.mp3")

    # play mp3
    os.system("open response.mp3")


# wake function
def wakeup(text):
    print("Wakeup")
    text = text.lower()
    for i in WAKE_WORDS:
        if i in text:
            response("hello sir")
            return True
    for i in BYE_WORDS:
        if i in text:
            response("bye sir")
            return True
    # elif "how are" or "howdy" in text:
    #     response("Doing Great Sir")
    else:
        return False


# Date time and Calander
def datetime_calender():
    pass


def open_web(text):
    text = text.lower()
    url = WEB_URLS["google"]
    for key_word in WEB_URLS.keys():
        if key_word in text:
            url = WEB_URLS[key_word]
            break
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    response("Opening {}".format(url))


def search(text):
    text = text.lower()
    text = text.replace("search", "")
    url = "https://www.google.com.tr/search?q={}".format(text)
    print(url)
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    response("Opening {}".format(text))


def news():
    # MacOS
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    TIME_OF_INDIA_URL = "https://timesofindia.indiatimes.com/home/headlines"
    webbrowser.get(chrome_path).open(TIME_OF_INDIA_URL)
    response("Here are some headlines from the Times of India,Happy reading")


def screenshot():
    call(["screencapture", "screenshot.jpg"])


def play_youtube(text):
    pass


if __name__ == '__main__':
    while True:
        statement = recordAudio()
        if statement:
            if WAKE_WORDS or BYE_WORDS in statement:
                wakeup(statement)

            elif "open" in statement:
                open_web(statement)

            elif 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                response(f"the time is {strTime}")

            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                response("I was built by Jayapavan Deshpande")

            elif 'search' in statement or "play" in statement:
                print("hello")
                search(statement)

            elif 'news' in statement:
                news()

            elif "take screenshot" in statement:
                screenshot()

            elif "Good" in statement:
                response("thank you sir")
