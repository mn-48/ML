import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime

# Initialize Text-to-Speech engine with a female voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (index 1)

# Function to speak text
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to listen to user commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Can you repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None

# Function to process commands
def process_command(command):
    if "alexa" in command:  # Wake word
        command = command.replace("alexa", "").strip()
        if "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}.")
        elif "who is" in command or "what is" in command:
            query = command.replace("who is", "").replace("what is", "").strip()
            info = wikipedia.summary(query, sentences=2)
            speak(info)
        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            return False
        else:
            speak("Sorry, I don't understand that command.")
    return True

# Main function
def main():
    speak("Hello! I'm your Alexa-like assistant. How can I help you today?")
    while True:
        command = listen()
        if command:
            if not process_command(command):
                break

if __name__ == "__main__":
    main()