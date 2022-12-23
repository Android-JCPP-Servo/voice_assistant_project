# Import required modules
import speech_recognition
from AppOpener import run

# Import custom modules
from play_sounds import play_response, play_command

# Method for getting user input and opening applications
def open_app():

    # Get the app name
    print("\nJack says:", "Which app would you like to open?")
    play_command()
    # Set primary initializers: recognizer and done
    recognizer = speech_recognition.Recognizer()
    done = False
    # Begin loop if done is still False
    while not done:
        # Get the input
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
                # Open app based on input
                run(text)
                play_response()
                done = True
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            # State the model didn't recognize the audio
            print("\nJack says:", "I didn't understand you! Please try again!\n")
            play_command()