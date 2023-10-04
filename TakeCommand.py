import speech_recognition as sr

recognizer = sr.Recognizer()


def TakeCommand():
    try:
        with sr.Microphone() as source2:
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = recognizer.listen(source2, 2, 5)
            MyText = recognizer.recognize_google(audio2)
            MyText = MyText.lower()
            return MyText
            print("Did you say ", MyText)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")


if __name__ == '__main__':
    TakeCommand()

