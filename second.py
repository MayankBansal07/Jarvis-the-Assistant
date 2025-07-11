import os
import requests
import webbrowser
from gtts import gTTS
import speech_recognition as sr

newsapi = "YOUR_NEWSAPI_KEY"

def speak(text):
    """Converts text to speech using gTTS and plays the audio."""
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("speech.mp3")
        os.system("start speech.mp3")  # Use 'start' for Windows
        # os.remove("speech.mp3")
    except Exception as e:
        print(f"An error occurred in the TTS system: {e}")

def get_news():
    """Fetches top headlines for India."""
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        if articles:
            speak("Here are the top news headlines.")
            for article in articles[:5]:  # Speak only the top 5 headlines
                speak(article.get("title", "No title available"))
        else:
            speak("Sorry, I couldn't find any news articles.")
    else:
        speak("Sorry, I couldn't fetch the news.")

def process_command(command):
    """Processes the user's command."""
    command = command.lower()
    if "open google" in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening Youtube...")
        webbrowser.open("https://www.youtube.com")
    elif "open linkdein" in command:
        speak("Opening LinkedIn...")
        webbrowser.open("https://www.linkedin.com/feed/")
    elif command.startswith("play"):
        speak("Playing the requested song.")  # Add your song logic here
    elif "what is your name" in command:
        speak("I am Jarvis, your personal assistant.")
    elif "news" in command:
        get_news()
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that command. Can you please repeat?")

def listen_for_command():
    """Listens for a command from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening for your command...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            print("Command received:", command)
            process_command(command)
        except sr.UnknownValueError:
            speak("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            speak(f"Error with the speech recognition service: {e}")
        except Exception as e:
            speak(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    try:
        while True:
            listen_for_command()
    except KeyboardInterrupt:
        speak("Goodbye!")
