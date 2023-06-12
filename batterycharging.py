import psutil
from playsound import playsound
from speak import speak


def plug_check():
    prev_status = None  # Initialize prev_status variable
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        status = battery.power_plugged
        if prev_status is not None and status != prev_status:  # Check if the status has changed
            if status:
                print("Charger plugged in.")
                playsound("/home/zenox/Jarvis/mp3(data)/Jarvis - Charging.mp3")
                speak("Jarvis System now in charging mode.")
            else:
                print("Charger unplugged.")
                playsound('/home/zenox/Jarvis/mp3(data)/Samsung Galaxy Charging Sound.mp3')
                speak("charging function stoped ")
                
        prev_status = status  
    
