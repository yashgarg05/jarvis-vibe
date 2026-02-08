from listener import listen
from brain import think
from commands import execute
from voice import speak
import voice
import sys
import time

RUNNING = True
def main():
    print("Jarvis is online. Say 'exit' to quit.")
    speak("Jarvis online.")

    while True:
        # Since speak() is blocking, we don't strictly need to check voice.speaking here 
        # unless speak() becomes async. But we'll keep it clean.
        if voice.speaking:
            time.sleep(0.1)
            continue
        command = listen()

        if not command:
            speak("I didn't hear anything.")
            continue

        print("You:", command)
        command = command.lower()

        if "exit" in command or "stop" in command or "quit" in command:
            speak("Exiting now. Goodbye.")
            time.sleep(0.5)   # let voice finish
            sys.exit(0)       # HARD EXIT (no coming back)

        # 🧠 Try system command first
        result = execute(command)

        if result:
            speak(result)
            continue

        # 🤖 Otherwise use AI brain
        reply = think(command)
        print("Jarvis:", reply)
        speak(reply)

if __name__ == "__main__":
    main()