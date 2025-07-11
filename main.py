import speech_recognition as sr
import webbrowser
import pyttsx3
from musiclib import music
import requests
import pyautogui
import pygetwindow as gw
import threading
import google.generativeai as genai
# import wolframalpha
# import pygame
# import openai
# import psutil
# import os
# import time
# from PIL import Image
# import tkinter as tk
# from tkinter import messagebox
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys  # For system-specific operations
# import re   # For pattern matching (if needed)
# import pyaudio  # For audio input/output

newsapi = "64e39ea42a01457e88474943253c558d"
gemini_api_key = "AIzaSyCNtrzLdOlVmAsjkMGgK6bZvoEoHtT907A"
genai.configure(api_key=gemini_api_key)

# Speak function to convert text to speech
def speak(text):
    """Converts text to speech."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to process general queries using Gemini API
def get_answer_from_gemini(query):
    """Fetches an answer to a query using the Gemini API."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    try:
        # Adding a prompt for short responses
        query = f"{query}. Make the response short and concise."
        response = model.generate_content(query)
        answer = response.text if response and response.text else "I couldn't fetch a proper response."
        return answer
    except Exception as e:
        return f"An error occurred while fetching the data: {e}"

# Process command function
def process_command(command):
    """Processes the user's command."""
    command = command.lower()

    if "open google" in command:
        speak("Opening the browser.")
        webbrowser.open("https://www.google.com")
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        speak(f"Playing {song}.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif "what is your name" in command:
        speak("I am Jarvis, your personal assistant.")
    elif "ask" in command:  # If the user asks a general question
        query = command.replace("ask", "").strip()  # Remove 'ask' from the query
        if query:
            speak(f"Let me find the answer to: {query}")
            answer = get_answer_from_gemini(query)  # Fetch answer using Gemini
            print("Gemini's Response:", answer)
            speak(answer)
        else:
            speak("Please ask a complete question.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        # Fallback to Gemini for undefined commands
        # speak("I didn't understand that command. Let me try to fetch an answer for you.")
        answer = get_answer_from_gemini(command)  # Send the command to Gemini
        print("Gemini's Response:", answer)
        speak(answer)

# Listen for commands
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

# Listen for wake word
def listen_for_jarvis():
    """Listens for the wake word 'Jarvis'."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening for the wake word 'Jarvis'...")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            if "jarvis" in command:
                speak("Yes, I am listening.")
                listen_for_command()
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Main loop
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    try:
        while True:
            listen_for_jarvis()
    except KeyboardInterrupt:
        print("\nExiting program.")
        speak("Goodbye Sir! Have a nice day")
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")





# Stop current music
# def stop_current_music():
#     """Closes the current browser tab playing the music."""
#     try:
#         browser_windows = [win for win in gw.getWindowsWithTitle('YouTube')]
#         if browser_windows:
#             for win in browser_windows:
#                 win.activate()
#                 pyautogui.hotkey('ctrl', 'w')  # Close the tab
#             speak("Stopped the current music.")
#     except Exception as e:
#         print(f"An error occurred while stopping the music: {e}")

# Mute or pause current music
# def mute_current_music():
#     """Mutes or pauses the music playing in the browser."""
#     try:
#         browser_windows = [win for win in gw.getWindowsWithTitle('YouTube')]
#         if browser_windows:
#             for win in browser_windows:
#                 win.activate()
#                 pyautogui.hotkey('k')  # Toggle play/pause
#     except Exception as e:
#         print(f"An error occurred while muting the music: {e}")