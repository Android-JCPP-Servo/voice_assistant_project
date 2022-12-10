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

