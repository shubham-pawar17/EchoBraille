import serial
        alphabet_mode()

    # -------- EASY QUIZ --------
    elif "easy mode" in command:
        quiz_mode(easy_words)

    # -------- HARD QUIZ --------
    elif "hard mode" in command:
        quiz_mode(hard_words)

    # -------- QUIZ --------
    elif "quiz mode" in command:
        quiz_mode(easy_words)

    # -------- TEACHER MODE --------
    elif "teacher mode" in command:
        teacher_mode(["apple", "banana", "mango"])

    # -------- DIRECT WORD DISPLAY --------
    else:
        speak(command)
        show_word(command)

# ---------------- MAIN PROGRAM ----------------
def main():
    global running

    main_menu()

    while running:

        if paused:
            speak("System is paused. Say continue to resume")
            cmd = listen()

            if "continue" in cmd:
                process_command(cmd)

            continue

        speak("Waiting for command")

        command = listen()

        process_command(command)

    arduino.close()
    speak("Program terminated")

# ---------------- START ----------------
if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nExiting...")
        arduino.close()