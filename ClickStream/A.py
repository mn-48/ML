import json
import os
import time
from pynput import mouse, keyboard

# Define log file in the current directory
LOG_FILE = os.path.join(os.getcwd(), "clickstream_log.json")

# Load existing data if the file exists
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        try:
            clickstream_data = json.load(f)
        except json.JSONDecodeError:
            clickstream_data = []
else:
    clickstream_data = []

# Mouse Listener
def on_click(x, y, button, pressed):
    event = {
        "event": "mouse_click",
        "timestamp": time.time(),
        "button": str(button),
        "position": (x, y),
        "pressed": pressed
    }
    clickstream_data.append(event)
    save_data()

# Keyboard Listener
def on_press(key):
    try:
        key_name = key.char if hasattr(key, 'char') else str(key)
        event = {
            "event": "key_press",
            "timestamp": time.time(),
            "key": key_name
        }
        clickstream_data.append(event)
        save_data()
    except AttributeError:
        pass

# Function to save data persistently
def save_data():
    with open(LOG_FILE, "w") as f:
        json.dump(clickstream_data, f, indent=4)

# Start listeners
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

print("Clickstream Logger Running... Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print(f"\nClickstream data saved in {LOG_FILE}")
