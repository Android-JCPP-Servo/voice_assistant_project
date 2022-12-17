# Import internal modules
import os
import sys
import threading
import tkinter as tk
import webbrowser

# Import external modules
import speech_recognition
import pyttsx3 as tts

# Sound player
from pydub import AudioSegment
from pydub.playback import play

# Import custom modules
from neuralintents import GenericAssistant

# Create an assistant class
class Assistant:
    
    # Provide simple constructor
    def __init__(self):

        # Create URLs
        self.work_url = 'https://cyberlandr.a2hosted.com/web'
        self.music_url = 'https://www.youtube.com/'
        self.church_url = 'https://www.lds.org/'
    
        # Initialize recognizer with speech recognition
        self.recognizer = speech_recognition.Recognizer()

        # Initialize speaker
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        # Initialize assistant
        mappings = {
            "file": self.create_file,
            "edit": self.edit_file,
            "delete": self.delete_file,
            "work": self.open_work,
            "youtube": self.open_youtube,
            "church": self.open_church,
        }
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

    
    """
    Method for playing audio to simplify Separation of Concerns
    """
    def play_sound(self):

        # Play R4-P17 response
        droid_res = AudioSegment.from_wav("./sound_effects/p17_res.wav")
        play(droid_res)


    """
    Methods for handling workday tasks
    """
    
    # Method for opening specific typical workday links
    def open_work(self):

        # Open CyberLandr website
        webbrowser.open_new(self.work_url)

        # Play R4-P17 response
        self.play_sound()


    # Method for opening YouTube
    def open_youtube(self):
        
        # Open YouTube
        webbrowser.open_new(self.music_url)

        # Play R4-P17 response
        self.play_sound()

    
    # Method for opening church website
    def open_church(self):
    
        # Open church website
        webbrowser.open_new(self.church_url)

        # Play R4-P17 response
        self.play_sound()


    """
    Methods for handling simple write-to-file tasks
    """

    # Method for creating a file
    def create_file(self):

        # Play R4-P17 response
        self.play_sound()

        # Initialize file
        with open("somefile.txt", "w") as f:

            # Write message
            f.write('HELLO WORLD!\n')


    # Method for editing a current file
    def edit_file(self):

        # Play R4-P17 response
        self.play_sound()

        # Print astromech translation
        print("\nJack says:", "What would you like to add?\n")

        done = False

        while not done:

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

                    # Initialize file
                    with open("somefile.txt", "w") as f:

                        # Write to the file
                        f.write(text, '\n')

                        # Finish operation
                        done = True

            except speech_recognition.UnknownValueError:

                self.recognizer = speech_recognition.Recognizer()

                # State the model didn't recognize the audio
                print("\nJack says:", "I didn't understand you! Please try again!")
                droid_res = AudioSegment.from_wav("./sound_effects/p17_command.wav")
                play(droid_res)
                # self.speaker.say("I didn't understand you! Please try again!")
                # self.speaker.runAndWait()


    # Method for deleting file
    def delete_file(self):

        # Play R4-P17 response
        self.play_sound()

        if os.path.exists("somefile.txt"):
            os.remove("somefile.txt")
        else:
            print("\nJack says:", "The file doesn't exist")
            droid_res = AudioSegment.from_wav("./sound_effects/p17_command.wav")
            play(droid_res)
            # self.speaker.say("The file doesn't exist")
    

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
                        droid_greet = AudioSegment.from_wav("./sound_effects/p17_greet.wav")
                        play(droid_greet)
                        print("\nJack says:", "I'm awake!\n")

                        # Get the command
                        audio = self.recognizer.listen(mic)

                        # Translate to text based on audio
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()

                        # Check if text is STOP
                        if text == "stop":

                            # Quit the program
                            droid_bye = AudioSegment.from_wav("./sound_effects/p17_bye.wav")
                            play(droid_bye)
                            print("\nJack says:", "Goodbye!\n") # Print droid translation
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
                                    # self.speaker.say(response)
                                    # self.speaker.runAndWait()

                                    # Play R4-P17 response
                                    droid_res = AudioSegment.from_wav("./sound_effects/p17_command.wav")
                                    play(droid_res)


                            # Reset color
                            self.label.config(fg="black")
            
            except:

                # Deactivate program
                self.label.config(fg="black")
                continue

# Create instance of assistant
Assistant()