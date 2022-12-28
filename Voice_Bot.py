import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit

player = pyttsx3.init()
listener = sr.Recognizer()


def listen_from_user():
    with sr.Microphone() as input_source:
        print("i am ready..speak")
        voice_input = listener.listen(input_source)
        try:

            text_command = listener.recognize_google(voice_input)
            print(text_command)

        except sr.UnknownValueError:
            text_command = "Could not understand"

    return text_command


def play(text):
    voices = player.getProperty("voices")
    player.setProperty('voice', voices[0].id)  # 0 for male , 1 for female
    player.say(text)
    player.runAndWait()


def run_voice_bot():
    command = listen_from_user()
    if "what is" in command:
        command = command.replace("what is ", "")
        print(command)
        final = wikipedia.summary(command, 2, auto_suggest=False)
        play(final)


    elif "play" in command:
        command = command.replace("play", "")
        print(command)
        pywhatkit.playonyt(command)

    else:
        play("sorry we didn't understood")





run_voice_bot()

#pywhatkit.playonyt("sukoon")


