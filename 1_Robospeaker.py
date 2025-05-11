#pip install pyttsx3 (run this command in your terminal to install the library)
# This is a simple text-to-speech program.
# It prompts the user for input and speaks the text aloud.
# This script uses the pyttsx3 library to convert text to speech.

import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    user_input = input("What should I say? (Type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    engine.say(user_input)
    engine.runAndWait()
