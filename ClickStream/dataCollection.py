from pynput import mouse, keyboard
import time
import json

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
    print(event)

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
        print(event)
    except AttributeError:
        pass

# Start listeners
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener = keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()

try:
    # Keep the script running
    mouse_listener.join()
    keyboard_listener.join()
except KeyboardInterrupt:
    # Stop listeners
    mouse_listener.stop()
    keyboard_listener.stop()

    print(clickstream_data)

    # Save data to JSON file
    try:
        with open("clickstream_log.json", "w") as f:
            json.dump(clickstream_data, f, indent=4)
        print("Clickstream data saved to clickstream_log.json.")
    except Exception as e:
        print(f"Error saving data: {e}")













                  





                      



                         








