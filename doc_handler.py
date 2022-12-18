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
    # Initialize file
    with open("somefile.txt", "w") as f:
        # Write message
        f.write('HELLO WORLD!\n')
    # Play R4-P17 response
    play_response()

# Method for editing a current file
def edit_file():
    # Print astromech translation
    print("\nJack says:", "What would you like to add? (Say STOP when you're done!)\n")
    # Play R4-P17 response
    play_command()
    # Call method to listen to audio
    listen_to_audio()

# Method for handling audio from edit_file function
def listen_to_audio():
    # Set primary initializers: recognizer and done
    recognizer = speech_recognition.Recognizer()
    done = False
    # Begin loop if done is still False
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
                # Pass text to writing handler
                done = write_to_file(text)
                # If done is FALSE again, run the function asking for clarification...
                if done == False:
                    listen_to_audio()
                else:
                    done = True
                    print('\nJack says:', "Check our your new file!\n")
                    play_response()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            # State the model didn't recognize the audio
            print("\nJack says:", "I didn't understand you! Please try again!\n")
            play_command()

# Method for writing new text to a file
def write_to_file(text):

    """
    TODO:
    1. Place IF statements within open() method
    2. Add checker for "comma"
    3. Add checker for "enter"
    4. Add checker for "exclamation point"
    ...
    """

    # Check if text ends with "period"...
    if text.endswith("period"):
        # Remove "period" from text
        text = text.strip("period")
        # Initialize file and set to "append"
        with open('somefile.txt', 'a') as f:
            # Write to the file
            f.write(text.strip() + '. ')
        # Return False
        return False

    # Check if text ends with "stop"...
    elif text.endswith("stop"):
        # Remove "period" from text
        text = text.strip("stop")
        # Initialize file and set to "append"
        with open('somefile.txt', 'a') as f:
            # Write to the file
            f.write(text.strip() + '.\n')
        # Return False
        return True

# Method for deleting file
def delete_file():
    if os.path.exists("somefile.txt"):
        os.remove("somefile.txt")
        # Play R4-P17 response
        play_response()
    else:
        print("\nJack says:", "The file doesn't exist")
        play_command()