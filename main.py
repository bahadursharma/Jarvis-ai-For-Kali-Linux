from listen import Listen
from speak import speak
from playsound import playsound
from youtubesearch import listen_and_searchyt
import random
from openfunctions import open_chrome
from openfunctions import open_whatsapp
from openfunctions import open_code
from openfunctions import open_googledrive
from openfunctions import open_rootTerminal
from openfunctions import open_terminal
from incriseVolume import increase_volume
from update import update_pc
from checkip import check_ip_using_wifi
import pyautogui as gui
from batterycharging import plug_check
import threading
from timesp import check_time
from openlinkedin import open_linkedin
import webbrowser
from sendmassegeonwhatsapp import Send_massege_on_Whatsapp
from openCHAtGpt import chatgpt
from qna import load_qa_data
from openytstudio import open_ytstudio
from open_telegram import open_telegram
from open_youtube import open_youtube
from shutdown import shutdown
from shutdown import reboot
from open_mysql import open_MYSQL
from wish import greating
from sendmassegeonwhatsapp import Send_massege_on_Whatsapp2
from sendmassegeonwhatsapp import Send_massege_on_Whatsapp3
import pywhatkit
from wether_report import Temp
from wether_report import temcity
from switchdash import switch_dash_1
from switchdash import switch_dash_2
from switchdash import switch_dash_3
from switchdash import switch_dash_4
from switchdash import switch_dash_5
from switchdash import switch_dash_6
from switchdash import switch_dash_7
from switchdash import switch_dash_8
from opengoogleclassroom import open_googleclassroom
from check_map import map
from bath_mode import bath_mode

qa_file_path = "/home/zenox/Jarvis/database/qna_log.txt"
qa_dict = load_qa_data(qa_file_path)


def main():
    playsound("/home/zenox/Jarvis/mp3(data)/Welcome Back Sir.mp3")
    while True:
        rise_cmd = ("jarvis", "javid", "jarvis", "javied",
                    "jarvis there", "jarvis are you there", "Javed", "Javed")
        text = Listen().lower()

        if text in rise_cmd:
            rise_cm = ("jarvis", "javid", "jarvis", "javied",
                       "jarvis there", "jarvis are you there", "Javed", "Jaggesh")
            playsound("/home/zenox/Jarvis/mp3(data)/Jarvis On (mp3cut.net).mp3")
            while True:
                text = Listen().lower()
                text = text.replace("jarvis", "")

                if "wake up" in text or "wakeup" in text:
                    random_choice = random.choice(["speak", "playsound"])
                    if random_choice == "speak":
                        speak("Hello sir, I am here. How may I help you?")
                    else:
                        playsound(
                            "/home/mr_zenox/Desktop/Jarvis/mp3(data)/Jarvis Startup ! Jarvis tiktok pc sound.mp3")
                elif "set alarm" in text:
                    speak(
                        "Sir, this is my beta version and I can't set alarms using voice. Please enter the time:")
                    # alarm_time = input()
                    # set_alarm(alarm_time)

                elif "youtube search" in text:
                    speak("What should I search on YouTube, sir?")
                    listen_and_searchyt()

                elif text.startswith("play song "):
                    song_name = text.replace("play song", "")
                    song_name = song_name.replace("on youtube", "")
                    pywhatkit.playonyt(song_name)
                    speak(f'Playing {song_name} on YouTube.')
                    speak("enjoy sir")

                elif "open chrome" in text:
                    open_chrome()

                elif "open instagram" in text:
                    webbrowser.get("https://www.instagram.com/")

                elif "open whatsapp" in text:

                    open_whatsapp()

                elif "open code editor" in text:
                    open_code()

                elif "open google drive" in text:
                    open_googledrive()

                elif "open root terminal" in text:
                    open_rootTerminal()

                elif "open terminal" in text:
                    open_terminal()

                elif "update my laptop" in text:
                    update_pc()

                elif "check IP address using Wi-Fi" in text:
                    check_ip_using_wifi()

                elif "increase volume" in text:
                    increase_volume()

                elif "open google classroom" in text or "open classroom" in text or "open googleclassroom" in text:
                    open_googleclassroom()

                elif "close" in text or "close this window" in text or " close window" in text:
                    gui.hotkey('alt', 'f4')

                elif "stop" in text or "play" in text or "pause" in text:
                    gui.hotkey('space')

                elif "thanks" in text or "thank you" in text:
                    responses = ["You're welcome sir!", "No problem sir.",
                                 "My pleasure!", "Not a problem at all sir., for you sir any time"]
                    response = random.choice(responses)
                    speak(response)

                elif "ya there" in text or "are you there" in text or "there" in text:
                    playsound(
                        "/home/mr_zenox/Desktop/Jarvis/mp3(data)/Jarvis Confirm-male.mp3")

                elif "hello" in text:
                    responses = ["hello sir , how may i assist you",
                                 "hello sir i am excited to assist you", "My pleasure sir", "for you sir any time"]
                    response = random.choice(responses)
                    speak(response)

                elif "love you" in text or "i love you" in text:
                    responses = ["love you to sir ", "love you three thousent sir",
                                 "love you four thousent sir", "i love you to sir"]
                    response = random.choice(responses)
                    speak(response)

                elif "minimise this window" in text or "minimise window" in text or "minimise" in text:
                    gui.hotkey('winleft', 'h')

                elif "what time" in text or "what is the time" in text or "what is the time jarvis" in text:
                    check_time()

                elif "mute" in text or "mute jarvis" in text:
                    gui.hotkey('f1')

                elif "open linkedin" in text:
                    open_linkedin()

                elif "open chatgpt" in text or "open chat gpt" in text:
                    speak("here you go.")
                    chatgpt()

                elif text.startswith("who is "):
                    if text in qa_dict:
                        speak(qa_dict[text])
                    else:
                        query = text.replace("who is ", "")
                        query = query.replace("search on google", "")
                        query = query.strip()
                        if query:
                            url = "https://www.google.com/search?q=" + query
                            webbrowser.open_new_tab(url)
                            speak("Here are the search results for " + query)
                        else:
                            speak("I didn't catch what you said")

                elif text.startswith("what is "):
                    if text in qa_dict:
                        speak(qa_dict[text])
                    else:
                        query = text.replace("what is ", "")
                        query = query.replace("search on google", "")
                        query = query.strip()
                        if query:
                            url = "https://www.google.com/search?q=" + query
                            webbrowser.open_new_tab(url)
                            speak("Here are the search results for " + query)
                        else:
                            speak("I dont know")

                elif text.startswith("how to "):
                    if text in qa_dict:
                        speak(qa_dict[text])
                    else:
                        query = text.replace("how to ", "HOW TO ")
                        query = query.replace("search on google", "")
                        query = query.strip()
                        if query:
                            url = "https://www.google.com/search?q=" + query
                            webbrowser.open_new_tab(url)
                            speak("Here are the search results for " + query)
                        else:
                            speak("I dont know")

                elif "send message on whatsapp" in text:
                    Send_massege_on_Whatsapp()

                elif "who are you" in text or "indroduse yourself" in text:
                    playsound("/home/zenox/Jarvis/mp3(data)/Jarvis.mp3")

                elif text in qa_dict:
                    speak(qa_dict[text])

                elif "open youtube studio" in text or "open youtube studio" in text:
                    open_ytstudio()

                elif "open telegram" in text:
                    open_telegram()

                elif "open youtube" in text:
                    open_youtube()

                elif "shutdown my laptop" in text or "shutdown" in text:
                    shutdown()

                elif "restart" in text or "restart my laptop" in text:
                    reboot()

                elif "open mysql" in text or "open my sql" in text or "open database" in text:
                    open_MYSQL()

                elif "good morning" in text or "good afternoon" in text or "good evening" in text:
                    greating()

                elif "good night" in text or "happy night" in text or "sweet dream" in text:
                    responses = ["good night sir , sleep well sir", "good night sir ,sweet dreams",
                                 "good night sir", "ok sir i will meet you new dream world"]
                    response = random.choice(responses)
                    speak(response)

                    speak("sir can i send good night to you special one and dad")
                    text = Listen().lower()
                    if "yes" in text or "yes please" in text:
                        Send_massege_on_Whatsapp2()
                        Send_massege_on_Whatsapp3()
                        playsound("/home/zenox/Jarvis/mp3(data)/JARVIS Message Sent.mp3")
                    elif "no" in text or "no thanks" in text or "no need" in text:
                        pass

                elif "check temperature outside" in text or "check temperature" in text:
                    Temp()


                elif "check temprature bangaluru" in text or "check temprature in banglore" in text or "temprature in banglore" in text:
                    temcity()

                elif "switch dash 1" in text or "switch dash one" in text:
                    switch_dash_1()

                elif "switch dash 2" in text or "switch dash two" in text or "switch dash to" in text:
                    switch_dash_2()

                elif "switch dash 3" in text or "switch dash three" in text:
                    switch_dash_3()

                elif "switch dash 4" in text or "switch dash four" in text:
                    switch_dash_4()

                elif "switch dash 5" in text or "switch dash five" in text:
                    switch_dash_5()

                elif "switch dash 6" in text or "switch dash six" in text:
                    switch_dash_6()

                elif "switch dash 7" in text or "switch dash seven" in text:
                    switch_dash_7()

                elif "switch dash 8" in text or "switch dash eight" in text:
                    switch_dash_8()

                elif "show dash" in text or "so dash" in text or "soo dash" in text:
                    gui.press('winleft')

                elif text in rise_cm:
                    main()

                elif text.startswith("where is "):
                    if text in qa_dict:
                        speak(qa_dict[text])
                    else:
                        text = text.replace("where is ", "")
                        text = text.strip()
                        map(text)

                elif "i am going to take bath" in text or "you want bath" in text or "bath" in text or "star bathing mode" in text or "start bath mode" in text:
                    bath_mode()

                elif "mute song" in text or "mute music" in text:
                    gui.press('m')

                elif "open Ggmail" in text or "open mail" in text or "open e mail" in text or "open email" in text or "open gmail" in text:
                    speak("opening mail.")
                    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")


thread1 = threading.Thread(target=plug_check)
thread2 = threading.Thread(target=main)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
