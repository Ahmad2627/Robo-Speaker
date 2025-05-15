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
