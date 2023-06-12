from speak import speak 
import pywhatkit
import time
import pyautogui as gui

def bath_mode():
    speak("ok sir i am going to make your bath special")
    song_name = "The Good Life Radio • 24/7 Live Radio | Best Relax House, Chillout, Study, Running, Gym, Happy Music"
    pywhatkit.playonyt(song_name)
    speak(f'here are some music to make your bath special')
    gui.press('f')
    time.sleep(4*200)
    speak("your bathing time out sir ! now i am gonna stop this mode !you need to focus on your work")
    time.sleep(3)
    gui.hotkey('alt','f4')

