import speech_recognition as sr

listener = sr.Recognizer()

with sr.Microphone() as input_source:
    print("i am ready..speak")
    voice_input=listener.listen(input_source)
    try:

        text = listener.recognize_google(voice_input)
        print(text)

    except sr.UnknownValueError:
        print("Could not understand")
'''
    try:
       text=listener.recognize_google(voice_input)
       print(text)
       
'''

