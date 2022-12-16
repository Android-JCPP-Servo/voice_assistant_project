# Import internal modules
import sys
import threading
import tkinter as tk

# Import external modules
import speech_recognition
import pyttsx3 as tts

# Import custom modules
from neuralintents import GenericAssistant

# Create an assistant class
class Assistant:

    # Provide simple constructor
    def __init__(self):

        # Initialize recognizer with speech recognition
        self.recognizer = speech_recognition.Recognizer()

        # Initialize speaker
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        # Initialize assistant
        self.assistant = GenericAssistant("intents.json", intent_methods={"file: self.create_file"})
        self.assistant.train_model()

        # Implement graphical interface
        self.root = tk.Tk()
        self.label = tk.Label(text="💿", font=("Arial", 120, "bold"))
        self.label.pack()

        

    # Method for creating a file
    def create_file(self):

        # Temporarily pass
        pass