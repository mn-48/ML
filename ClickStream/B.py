import time
import json
from pynput import mouse, keyboard
import psutil
import pygetwindow as gw
from browserhistory import get_browserhistory

# Global variables to store clickstream data
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

def on_scroll(x, y, dx, dy):
    event = {
        "event": "mouse_scroll",
        "timestamp": time.time(),
        "position": (x, y),
        "scroll_delta": (dx, dy)
    }
    clickstream_data.append(event)
    print(event)

def on_move(x, y):
    event = {
        "event": "mouse_move",
        "timestamp": time.time(),
        "position": (x, y)
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

# Application Usage Tracker
def get_active_application():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.title
    except Exception as e:
        print(f"Error getting active application: {e}")
    return None

# Web Browsing History
def get_browsing_history():
    try:
        history = get_browserhistory()
        return history
    except Exception as e:
        print(f"Error fetching browsing history: {e}")
    return None

# Main Function
def main():
    # Start mouse and keyboard listeners
    mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll, on_move=on_move)
    keyboard_listener = keyboard.Listener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    try:
        while True:
            # Track active application every second
            active_app = get_active_application()
            if active_app:
                event = {
                    "event": "application_usage",
                    "timestamp": time.time(),
                    "application": active_app
                }
                clickstream_data.append(event)
                print(event)

            # Fetch browsing history periodically (e.g., every 10 minutes)
            if int(time.time()) % 600 == 0:  # Every 10 minutes
                browsing_history = get_browsing_history()
                if browsing_history:
                    event = {
                        "event": "web_browsing_history",
                        "timestamp": time.time(),
                        "history": browsing_history
                    }
                    clickstream_data.append(event)
                    print(event)

            time.sleep(1)  # Wait for 1 second before the next iteration

    except KeyboardInterrupt:
        # Stop listeners
        mouse_listener.stop()
        keyboard_listener.stop()

        # Save data to JSON file
        try:
            with open("clickstream_data.json", "w") as f:
                json.dump(clickstream_data, f, indent=4)
            print("Clickstream data saved to clickstream_data.json.")
        except Exception as e:
            print(f"Error saving data: {e}")

if __name__ == "__main__":
    main()