# 🗣️ Text-to-Speech (TTS) Program using Python

A simple and beginner-friendly command-line **Text-to-Speech (TTS)** tool built using Python's `pyttsx3` library. The program converts user input text into audible speech and continues to run until the user types "exit".

---

## 📦 Requirements

Before running the script, install the required library:

bash
pip install pyttsx3
`

---

## 🚀 Features

* Converts typed text into spoken words.
* Continues to prompt until user types `'exit'`.
* Cross-platform and offline (no internet required).
* Lightweight and fast response time.

---

## 📂 How to Use

1. Open a terminal.
2. Navigate to the folder containing the Python script.
3. Run the script:

bash
python text_to_speech.py


4. Type a sentence and hear it spoken aloud.
5. To quit, type:


exit


---

## 💡 Example


What should I say? (Type 'exit' to quit): Hello, welcome to my Python project!
# (Speech: "Hello, welcome to my Python project!")

What should I say? (Type 'exit' to quit): exit
Goodbye!


---

## 🛠️ Tech Stack

* **Python 3**
* **[pyttsx3](https://pypi.org/project/pyttsx3/)** (Text-to-Speech library)

---

## ⚙️ Additional Notes

* This script works offline and uses your system's default voice engine (SAPI5 on Windows, NSSpeechSynthesizer on macOS, and espeak on Linux).
* No external APIs or internet connection are required.

---

## 🧠 Concepts Covered

* Python loops and user input
* Integration with external libraries
* Text-to-speech functionality
* Handling user exit conditions

---

## 👤 Author

**Ahmad**
GitHub: [Ahmad2627](https://github.com/Ahmad2627)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

