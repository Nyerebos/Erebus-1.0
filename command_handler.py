import subprocess

def handle_command(command):
    if command == "Open Notepad":
        notepad_path = r"C:\User\Me\ProgramFiles\Notepad.exe"
        subprocess.Popen([notepad_path])
    elif command == "Open Star Citizen":
        star_citizen_path = r"C:\User\Me\ProgramFiles\Star Citizen.exe"
        subprocess.Popen([star_citizen_path])
