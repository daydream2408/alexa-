import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests


recognizer = sr.Recognizer()



def speak(text):
         engine=pyttsx3.init()
         engine.say(text)
         engine.runAndWait()
         engine.stop()


def processcommand(c):
        if "open google" in c:
             
              webbrowser.open("https://google.com")
        elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "open linkedin" in c.lower():
             webbrowser.open("https://linkedin.com")
        elif c.lower().startswith("play"):
             song=c.lower().split(" ")[1]
             link=  musiclibrary.music[song]
             webbrowser.open(link)
        elif "news" in c.lower():
           r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
           if r.status_code == 200:
               # Parse the JSON response
               data = r.json()
            
               
               articles = data.get('articles', [])
            
            
               for article in articles:
                   speak(article['title'])

    
        



if __name__ == "__main__":
        speak("starting alexa.....")

        while True:
            # obtain audio from the microphone
            r = sr.Recognizer()
        

            
            print("recognizing......")
            # recognize speech using google
            try:
                    with sr.Microphone() as source:
                        print("Listning")
                        audio = r.listen(source)
                    word = r.recognize_google(audio)
                    if (word.lower()=="alexa"):
                        speak("ya")
                          
                        
                    
                        #listen for comand
                        with sr.Microphone() as source:
                            print("alexa active")
                            audio = r.listen(source)
                            command = r.recognize_google(audio)

                            processcommand(command)
            
            except Exception as e:
                speak("sorry did you say somthing")
                print(" error; {0}".format(e))



