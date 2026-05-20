import serial
import time
import speech_recognition as sr
import pyttsx3
import random
import sounddevice as sd
import numpy as np

# Arduino connection
arduino = serial.Serial("COM4", 9600)
time.sleep(2)

# AI setup
engine = pyttsx3.init()
r = sr.Recognizer()

# Braille mapping
braille_map = {
    'a':'100000','b':'110000','c':'100100','d':'100110','e':'100010',
    'f':'110100','g':'110110','h':'110010','i':'010100','j':'010110',
    'k':'101000','l':'111000','m':'101100','n':'101110','o':'101010',
    'p':'111100','q':'111110','r':'111010','s':'011100','t':'011110',
    'u':'101001','v':'111001','w':'010111','x':'101101','y':'101111','z':'101011'
}

words = ["cat", "dog", "bed", "bat", "tea"]

# Speak
def speak(text):
    print("AI:", text)
    engine.say(text)
    engine.runAndWait()

# Listen 
def listen():
    while True:
        print("\nGet ready...")
        time.sleep(1)
        print("Speak now...")

        duration = 4
        fs = 16000

        recording = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype='int16',
            device=1
        )
        sd.wait()

        # boost audio
        recording = recording * 15

        print("Audio level:", np.max(recording))

        audio = sr.AudioData(recording.tobytes(), fs, 2)

        try:
            text = r.recognize_google(audio, language="en-IN")
            text = text.lower()
            print("✅ You said:", text)
            return text

        except:
            print("❌ Could not understand")
            speak("I did not understand, please say again")

# Send to Arduino
def send_letter(letter):
    if letter in braille_map:
        pattern = braille_map[letter]
        print(f"Sending {letter} → {pattern}")
        arduino.write((pattern + "\n").encode())
        time.sleep(1)

def show_word(word):
    for ch in word:
        send_letter(ch)
        time.sleep(0.5)

# Main loop
try:
    while True:
        speak("Say a word or say random word")

        command = listen()

        if "random" in command:
            word = random.choice(words)

            speak("Read this word")
            print("Word:", word)

            show_word(word)

            speak("Now say the word")
            student = listen()

            if student == word:
                speak("Correct")
            else:
                speak("Wrong. The word was " + word)

        else:
            speak(command)
            show_word(command)

except KeyboardInterrupt:
    print("\nExiting...")
    arduino.close()