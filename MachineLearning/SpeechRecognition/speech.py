import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        r.energy_threshold = 4000
        try:
            audio = r.listen(source, timeout=10)  # Menambahkan opsi timeout menjadi 10 detik
        except sr.WaitTimeoutError:
            print("No speech detected")
            return "None"

        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("The command is:", Query)

        except sr.UnknownValueError:
            print("Could not understand audio")
            return "None"

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    minute = time[14:16]
    speak("The time is " + hour + " hours and " + minute + " minutes")


def greet():
    speak("Hello, I am your desktop assistant. How may I help you?")


def processQuery():
    greet()

    while True:
        query = takeCommand().lower()

        if query == "None":
            continue

        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks")
            webbrowser.open("www.geeksforgeeks.org")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")

        elif "which day is it" in query:
            tellDay()

        elif "tell me the time" in query:
            tellTime()

        elif "bye" in query:
            speak("Goodbye. Check out GeeksforGeeks for more exciting things")
            exit()

        elif "from wikipedia" in query:
            speak("Searching on Wikipedia")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=4)
                speak("According to Wikipedia")
                speak(result)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Multiple matches found. Please be more specific.")

        elif "tell me your name" in query:
            speak("I am Jarvis, your desktop assistant")


if __name__ == '__main__':
    processQuery()
