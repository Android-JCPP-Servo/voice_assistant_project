def listen(recognizer, mic):
    # Remove ambient noise
    recognizer.adjust_for_ambient_noise(mic, duration=1.0)
    # Initialize the audio
    audio = recognizer.listen(mic)
    # Translate to text based on audio
    text = recognizer.recognize_google(audio)
    text = text.lower()
    # Return text
    return text