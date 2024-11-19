import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice to a Spanish voice, if available
voices = engine.getProperty('voices')
spanish_voice_found = False
for voice in voices:
    if 'spanish' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        spanish_voice_found = True
        break

if not spanish_voice_found:
    print("No Spanish voice found. Using the default voice.")

# Set speech properties (optional for clarity)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level from 0.0 to 1.0

def SpeakText(command):
    """Function to convert text to speech."""
    engine.say(command)
    engine.runAndWait()

print("Say 'salir' to exit the program.")
while True:
    try:
        with sr.Microphone() as source2:
            print("Listening...")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)

            # Recognize speech in Spanish
            MyText = r.recognize_google(audio2, language='es-ES')
            MyText = MyText.lower()

            if MyText == "salir":
                print("Programa terminado.")
                break

            print("¿Dijiste:", MyText)
            SpeakText(MyText)

    except sr.RequestError as e:
        print("No se pudieron solicitar los resultados; {0}".format(e))

    except sr.UnknownValueError:
        print("No se entendió el audio, por favor intenta de nuevo.")
