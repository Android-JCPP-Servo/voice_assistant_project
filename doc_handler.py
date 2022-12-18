"""
DOC HANDLER

Methods for handling simple write-to-file tasks
"""
# Import internal modules
import os

# Import external modules
import speech_recognition

# Sound player imports
from play_sounds import play_response, play_command

# Method for creating a file
def create_file():
    # Play R4-P17 response
    play_response()
    # Initialize file
    with open("somefile.txt", "w") as f:
        # Write message
        f.write('HELLO WORLD!\n')


# Method for editing a current file
def edit_file():
    # Play R4-P17 response
    play_response()
    # Print astromech translation
    print("\nJack says:", "What would you like to add?\n")
    done = False
    while not done:
        try:
            # Set microphone
            with speech_recognition.Microphone() as mic:
                # Remove ambient noise
                recognizer.adjust_for_ambient_noise(mic, duration=1.0)
                # Initialize the audio
                audio = recognizer.listen(mic)
                # Translate to text based on audio
                text = recognizer.recognize_google(audio)
                text = text.lower()
                # Initialize file and set to "append"
                with open("somefile.txt", "a") as f:
                    # Write to the file
                    f.write(text, '\n')
                    # Finish operation
                    done = True
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            # State the model didn't recognize the audio
            print("\nJack says:", "I didn't understand you! Please try again!\n")
            play_command()


# Method for deleting file
def delete_file():
    # Play R4-P17 response
    play_response()
    if os.path.exists("somefile.txt"):
        os.remove("somefile.txt")
    else:
        print("\nJack says:", "The file doesn't exist")
        play_command()