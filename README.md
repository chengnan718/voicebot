# Project Title

AI voice Chatbot

This project is based on AI voice chatbot with rasa, vosk, SpeechRecognition

## Installation

### Install Dependencies

pip install vosk pyaudio requests

### Setup Rasa server

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
