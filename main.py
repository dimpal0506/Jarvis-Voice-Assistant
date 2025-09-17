import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize

print("Jarvis is starting...")

def start():
    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call(["adb", "connect", "192.168.0.106:5555"])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Mam, How can I help you")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)


# ✅ Call the function so it actually runs
if __name__ == "__main__":
    start()
