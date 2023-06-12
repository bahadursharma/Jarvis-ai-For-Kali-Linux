import time
from playsound import playsound

def set_reminder():
    minutes = int(input("Enter the number of minutes for the reminder: "))
    seconds = minutes * 60
    time.sleep(seconds)
    playsound("/home/mr_zenox/Desktop/Jarvis/mp3(data)/Jarvis Reminder.mp3")
    print(f"{minutes} minutes have passed. Time for your reminder!")


set_reminder()