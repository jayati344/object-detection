import pygame
from gtts import gTTS


def speak(text):
    try:
        tts = gTTS(text=text)
        pygame.mixer.init()
        tts.save("audio.mp3")
        audio = pygame.mixer.Sound("audio.mp3")
        audio.play()
    except Exception as e:
        print(e)