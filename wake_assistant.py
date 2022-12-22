# Import internal modules
import os
import sys
import threading
import tkinter as tk

# Import external modules
import speech_recognition
import pyttsx3 as tts

# Import custom modules
from neuralintents import GenericAssistant
from play_sounds import play_greeting, play_response, play_command, play_goodbye
from mappings import pass_mappings

# Create an assistant class
class Assistant:
    # Provide simple constructor
    def __init__(self):
        # Initialize recognizer with speech recognition
        self.recognizer = speech_recognition.Recognizer()
        # Grab the mappings from pass_mappings()
        mappings = pass_mappings
        # Initialize assistant
        self.assistant = GenericAssistant("./intents/assistants.json", intent_methods=mappings)
        self.assistant.train_model()
        # Implement graphical interface
        self.root = tk.Tk()
        self.label = tk.Label(text="💿", font=("Arial", 120, "bold"))
        self.label.pack()
        # Listen for the audio
        threading.Thread(target=self.run_assistant).start()
        # Set main loop
        self.root.mainloop()

    # Method for run_assistant
    def run_assistant(self):
        # Run in a separate thread
        while True:
            try:
                # Set microphone
                with speech_recognition.Microphone() as mic:
                    # Remove ambient noise
                    self.recognizer.adjust_for_ambient_noise(mic, duration=1.0)
                    # Initialize the audio
                    audio = self.recognizer.listen(mic)
                    # Translate to text based on audio
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    # Activate only if specific text in thread
                    if "hey jack" in text:
                        # Set color
                        self.label.config(fg="red")
                        # Play .WAV file
                        print("\nJack says:", "I'm listening!\n")
                        play_greeting()
                        # Get the command
                        audio = self.recognizer.listen(mic)
                        # Translate to text based on audio
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        # Check if text is STOP
                        if text == "stop":
                            # Quit the program
                            print("\nJack says:", "Goodbye!\n")
                            play_goodbye()
                            self.root.destroy()
                            sys.exit(0)
                        # If text IS NOT stop
                        else:
                            # Check if text is not empty
                            if text is not None:
                                # Set response
                                response = self.assistant.request(text)
                                # If the response is not empty
                                if response is not None:
                                    # Respond...
                                    print("\nJack says:", response + '\n')
                                    # Play R4-P17 response
                                    play_command()
                            # Reset color
                            self.label.config(fg="black")
            except:
                # Deactivate program
                self.label.config(fg="black")
                continue

# Create instance of assistant
Assistant()