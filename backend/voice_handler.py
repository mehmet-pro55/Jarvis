import speech_recognition as sr
import pyttsx3

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        """Converts text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listens to the microphone and returns recognized text."""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return None
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return None

# Example usage:
# voice_handler = VoiceHandler()
# voice_handler.speak("Hello, how can I assist you?")
# recognized_text = voice_handler.listen()