import speech_recognition as sr
import chat
import speak
import app
import asyncio
import time
import pygame

async def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(text)
        if "turn on the camera" in text.lower():
            # Turn on the camera
            print("Camera turned on!")
            app.main()
            # Your code to turn on the camera goes here
        else:
            print("Command not recognized or not related to turning on the camera.")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the request.")
        return ""
    


# speak.speak("You are a helpful assistant.")
async def main():
    while True:
        print("PLease say something...")
        user_input = await listen()
        if user_input:
            print("User:", user_input)
            resp = chat.gpt(user_input)
            speak.speak(resp)


asyncio.run(main())

# speak.speak("Do other Azure AI services support this too?")
# print("Do other Azure AI services support this too?")
