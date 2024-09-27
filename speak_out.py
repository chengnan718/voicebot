import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}, Name: {voice.name}, Languages: {voice.languages}")
