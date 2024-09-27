import os
import pyaudio
import vosk
import json
import pyttsx3
import requests

# Path to the downloaded Vosk model
model_path = "vosk-model-small-en-us-0.15"  # Change this to your model's path

# Load the Vosk model
if not os.path.exists(model_path):
    print(f"Model not found at {model_path}")
    exit(1)

model = vosk.Model(model_path)

# Set up PyAudio and check if microphone is available
p = pyaudio.PyAudio()

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to send the transcribed text to the Rasa server and get a response
def send_to_rasa(user_message):
    try:
        # Send the user's message to the Rasa server via the REST API
        response = requests.post(
            'http://localhost:5005/webhooks/rest/webhook',
            json={"sender": "user", "message": user_message}
        )
        return response.json()  # Return the Rasa response as JSON
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Rasa: {e}")
        return None

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

try:
    # Check if there's a default input device (microphone)
    info = p.get_default_input_device_info()
    print(f"Microphone found: {info['name']}")

    # Open a stream for real-time audio capture
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    # Initialize the Vosk recognizer with the model
    recognizer = vosk.KaldiRecognizer(model, 16000)

    print("Listening...")

    while True:
        # Read microphone data
        data = stream.read(4000, exception_on_overflow=False)

        # If Vosk recognizes speech, process the results
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print(f"Recognized: {result['text']}")

            text = result['text']
            if text:
                # Send the recognized text to Rasa
                rasa_response = send_to_rasa(text)

                if rasa_response:
                    for response in rasa_response:
                        print(f"Rasa Response: {response['text']}")
                        speak(response['text'])
        else:
            # Get partial results if available
            partial_result = json.loads(recognizer.PartialResult())
            print(f"Partial: {partial_result['partial']}")

except IOError:
    # If no microphone is found or there's an issue with the device
    print("No microphone found or unable to access the microphone. Please check your input device.")

except KeyboardInterrupt:
    # Stop the stream when Ctrl+C is pressed
    print("Stopping...")

finally:
    if 'stream' in locals():
        stream.stop_stream()
        stream.close()
    p.terminate()
