import os
import webbrowser
import subprocess

def execute(command: str) -> str:
    command = command.lower()

    # 🌐 Open websites
    if "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube."

    if "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google."

    # 💻 Applications (macOS)
    if "open chrome" in command:
        subprocess.run(["open", "-a", "Google Chrome"])
        return "Opening Chrome."

    if "open vscode" in command or "open vs code" in command:
        subprocess.run(["open", "-a", "Visual Studio Code"])
        return "Opening Visual Studio Code."

    if "open terminal" in command:
        subprocess.run(["open", "-a", "Terminal"])
        return "Opening Terminal."

    # 🔌 System control
    if "shutdown" in command:
        return "Shutdown command blocked for safety."

    return ""

def handle_command(command):
    if "open chrome" in command:
        os.system("open -a 'Google Chrome'")
        return True

    if "open youtube" in command:
        os.system("open https://youtube.com")
        return True

    return False
