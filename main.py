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
def create_note():
    # Get the speech recognizer
    global recognizer

    # Have speaker request more info
    speaker.say("What do you want to write onto your list?")
    speaker.runAndWait() # Wait for user input

    # Prevent program from failing - Loop until the program understands the command
    done = False

    while not done:
        # Try processing user input
        try:
            # Set microphone
            with speech_recognition.Microphone() as mic:
                # Block out ambient noise
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                # Get the user input
                audio = recognizer.listen(mic)

                # Decipher user input
                note = recognizer.recognize_google(audio)
                # Set text to lowercase
                note = note.lower()

                # Save note to specific file
                speaker.say('Choose a filename!')
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                # Get filename and set it to lowercase
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'r') as f:
                f.write(note)
                done = True
                speaker.say(f"I successfully created the note {filename}!")

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            # State the model didn't recognize the audio
            speaker.say("I didn't understand you! Please try again!")
            speaker.runAndWait()

mappings = {"greeting": some_function}

# Set up assistant
assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

# Test assistant request
# assistant.request("How are you?")