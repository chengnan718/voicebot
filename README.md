# AI voice Chatbot

This project is based on AI voice chatbot with rasa, vosk, SpeechRecognition

## Installation

### Install Dependencies

```bash
pip install vosk pyaudio requests pyttsx3
```

## Structure of the project

### Speech Recognition

```bash
import vosk

# Path to the downloaded Vosk model
model_path = "vosk-model-small-en-us-0.15"  # Change this to your model's path

model = vosk.Model(model_path)
```

### Rasa Server

- Create a new Rasa Project

```bash
rasa init --no-prompt
```

- Modify domain.yml to add some intents and responses

```bash
version: "3.0"

intents:
  - greet
  - goodbye
  - affirm
  - deny

responses:
  utter_greet:
    - text: "Hello! How can I assist you today?"
  utter_goodbye:
    - text: "Goodbye! Have a great day!"
  utter_affirm:
    - text: "Glad to hear that!"
  utter_deny:
    - text: "Sorry to hear that."

actions:
  - utter_greet
  - utter_goodbye
  - utter_affirm
  - utter_deny

```

- Define NLU Data in data/nlu.yml

```bash
version: "3.0"
nlu:
- intent: greet
  examples: |
    - hello
    - hi
    - hey
    - good morning
    - good evening
- intent: goodbye
  examples: |
    - goodbye
    - see you later
    - bye
- intent: affirm
  examples: |
    - yes
    - yeah
    - indeed
- intent: deny
  examples: |
    - no
    - never
- intent: ask_weather
  examples: |
    - what's the weather like
    - tell me the weather
    - how's the weather

```

- Train your Rasa model

```bash
rasa train

```

- Run the Rasa server- default port is 5005

```bash
rasa run -m models --enable-api
```

## VOSK model link

https://drive.google.com/drive/folders/1lTqi0J2Fkskw8sPkn-Nq1lLaYAx5XH57