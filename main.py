#ASSISTANT BOT FOR SERVICE
#Named as PERCY

import datetime
import webbrowser
import openai
import  requests
import speech_recognition as sr
import win32com.client
import os
import subprocess
from config import apikey
import random

chatbot=" "
def chat(query):
    global chatbot
    print(chatbot)

    openai.api_key = apikey
    chatbot+="Helper:{prompt}\n PERCY:";

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatbot,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response['choices'][0]['text'])
    chatbot+= f"{response['choices'][0]['text']}\n"
    return  response["choices"][0]["text"]
def ai(prompt):
    openai.api_key = apikey
    testseries=f"{prompt}\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response['choices'][0]["text"])
    testseries+=response['choices'][0]["text"]

    if not os.path.exists("openai"):
        os.mkdir("openai")

    with open(f"openai/prompt-{random.randint(1,245242331)}","w") as f:
        f.write(testseries)

speaker =win32com.client.Dispatch("SAPI.SpVoice")
def takeCommand():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing..............................")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said{query}")
            return query

        except Exception as e:
            return "Some error occured, from Percy"
def say(text):
    speaker.Speak(text)

if __name__ == '__main__':

    print(say('Welcome aboard to Virtual Assistant services'))
    print(say("This is PERCY,your own personal the Virtual Assistant "))
    while True:
        print("PERCY ,listening................")
        query = takeCommand()

        #todo:Add more sites
        sites =[["times of india","https://timesofindia.indiatimes.com/?from=md"],["wikipedia","https://www.wikipedia.org/"]]

        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening{site[0]} sir............")
                webbrowser.open(site[1])

    #todo:Add a any feature within this you want to execute on command

        if "what is the time".lower() in query.lower():
            strfTime =datetime.datetime.now().strftime("%H:%M::%S")
            print(say(f"Sir\mam The time is {strfTime}"))

        if "Please open canva".lower() in query.lower():
            #todo:type the paticualar file location here which you want access
            say("opening Canva sir")
            webbrowser.open("https://www.canva.com/")

        if "Please open google chrome".lower() in query.lower():
            say("opening google sir")
            webbrowser.open("https://www.google.com/")

        if "Please open YOUTUBE".lower() in query.lower():
            say("opening Youtube sir")
            webbrowser.open("https://www.youtube.com/")

        if "Open Music".lower() in query.lower():
            musicpath = "C:\\Users\\avika\\OneDrive\\Desktop\\DONT.mp3"
            say("opening Music sir")
            os.system(f"start {musicpath}")

        if "Open pro".lower() in query.lower():
            pro="C:\\Users\\avika\\OneDrive\\Desktop\\pro.lnk"
            say("opening pro sir")
            os.system(f"start {pro}")

        if "Tell News".lower() in query.lower():
            url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-10-15&sortBy=publishedAt&apiKey=ef0aa6f5b4b0454d86a50cf19938d71c&language=en"
            response = requests.get(url)
            data = response.json()
            articles = data.get('articles')
            for title in articles:
                print(say(title['title']))

        if "Open photoshop".lower() in query.lower():
            photo="C:\\Users\\avika\\OneDrive\\Desktop\\Photoshop.lnk"
            say("opening Photoshop sir")
            os.system(f"start {photo}")

        if "talk to me".lower() in query.lower():
            ai(prompt=query)

        elif "quit".lower() in query.lower():
            exit()

        elif "Reset".lower() in query.lower():
            chatbot=" "
        else:
            print("PERCY Assisting")
            chat(query)