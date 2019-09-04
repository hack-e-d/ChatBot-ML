from nltk.chat.util import Chat, reflections
from datetime import datetime, date
today = date.today()
now = datetime.now()
time = now.strftime("%H:%M:%S")

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is JARVIS and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"what time is it?",
        [str(time)]
    ],
    [
        r"What date is it?",
        [str(today)]
    ],
    [
        r"hi|hey|hello|holla",
        ["Hello", "Hey there",]
    ],
    [
        r"sup",
        ["Nothing Much just 0's and 1's"]
    ],
    [
        r"(.*) age?",
        ["I'm am AI dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["VIJAY created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Chennai, Tamil Nadu',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm an AI, I am well as long as I'm plugged in!!! ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Dhoni","Ashwin","Raina"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Thalapathy VIJAY"]
],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def JARVIS():
    print("Hi, I'm IRIS and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    JARVIS_chat = Chat(pairs, reflections)
    JARVIS_chat.converse()
if __name__ == "__main__":
    JARVIS()
