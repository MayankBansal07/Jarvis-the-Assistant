 commands
def listen_for_command():
    """Listens for a command from the user."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening for your command...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print("Command received:", command)
            process_command(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
