import pyttsx3
player=pyttsx3.init()

#code for changing default male to female voice
voices=player.getProperty("voices")
player.setProperty('voice', voices[0].id)  #0 for male , 1 for female


player.say("hello everyone")
player.runAndWait()