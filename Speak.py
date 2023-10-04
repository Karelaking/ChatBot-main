import pyttsx3 as pt


def Speak(text):
    engine = pt.init()
    engine.setProperty('rate', 185)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


if __name__ == '__main__':
    Speak()
