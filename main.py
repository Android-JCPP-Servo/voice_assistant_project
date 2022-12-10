# Import modules
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

# Set up a speech recognizer
recognizer = speech_recognition.Recognizer()

# Set up speaker
speaker = tts.init()
speaker.setProperty('rate', 150) # 150 is a good average rate

# Create TODO list
todo_list = ["Go shopping", "Clean Room", "Program R4-P17 Voice Assistant"]

"""
Mappings and Functions:
If a mapping recognizes a specific command or request, it will pass an appropriate function
"""
def some_function():
    print("Hello World!")

mappings = {"greeting": some_function}

# Set up assistant
assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

# Test assistant request
# assistant.request("How are you?")