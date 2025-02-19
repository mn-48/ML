import time
import json
import os
import subprocess
from pynput import mouse, keyboard
import psutil

# File to store clickstream data
LOG_FILE = "clickstream_data.json"

# Global clickstream data
clickstream_data = []

# Load existing data safely
def load_data():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

clickstream_data = load_data()

# Save data persistently
def save_data():
    try:
        with open(LOG_FILE, "w") as f:
            json.dump(clickstream_data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# Get active window (Linux alternative for PyGetWindow)
def get_active_application():
    try:
        output = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"])
        return output.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return "Unknown"

# Get browser history (fallback if `browserhistory` isn't supported)
def get_browsing_history():
    try:
        output = subprocess.check_output(["sqlite3", os.path.expanduser("~/.mozilla/firefox/*.default-release/places.sqlite"), 
                                          "SELECT url FROM moz_places ORDER BY last_visit_date DESC LIMIT 10;"])
        history = output.decode("utf-8").split("\n")
        return history
    except Exception as e:
        print(f"Error fetching browsing history: {e}")
    return []

# Mouse Listeners
def on_click(x, y, button, pressed):
    event = {
        "event": "mouse_click",
        "timestamp": time.time(),
        "window": get_active_application(),
        "button": str(button),
        "position": (x, y),
        "pressed": pressed
    }
    clickstream_data.append(event)
    save_data()
    print(event)

def on_scroll(x, y, dx, dy):
    event = {
        "event": "mouse_scroll",
        "timestamp": time.time(),
        "window": get_active_application(),
        "position": (x, y),
        "scroll_delta": (dx, dy)
    }
    clickstream_data.append(event)
    save_data()
    print(event)

def on_move(x, y):
    event = {
        "event": "mouse_move",
        "timestamp": time.time(),
        "window": get_active_application(),
        "position": (x, y)
    }
    clickstream_data.append(event)
    save_data()
    print(event)

# Keyboard Listener
def on_press(key):
    try:
        key_name = key.char if hasattr(key, 'char') else str(key)
        event = {
            "event": "key_press",
            "timestamp": time.time(),
            "window": get_active_application(),
            "key": key_name
        }
        clickstream_data.append(event)
        save_data()
        print(event)
    except AttributeError:
        pass

# Main Function
def main():
    # Start listeners
    mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll, on_move=on_move)
    keyboard_listener = keyboard.Listener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    # Time tracking for history collection
    last_history_check = time.monotonic()

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
                save_data()
                print(event)

            # Fetch browsing history every 10 minutes
            if time.monotonic() - last_history_check >= 600:  # 600 seconds = 10 minutes
                browsing_history = get_browsing_history()
                if browsing_history:
                    event = {
                        "event": "web_browsing_history",
                        "timestamp": time.time(),
                        "history": browsing_history
                    }
                    clickstream_data.append(event)
                    save_data()
                    print(event)
                last_history_check = time.monotonic()

            time.sleep(1)  # Wait 1 second before the next check

    except KeyboardInterrupt:
        # Stop listeners
        mouse_listener.stop()
        keyboard_listener.stop()

        print("\nClickstream data saved in", LOG_FILE)

if __name__ == "__main__":
    main()
