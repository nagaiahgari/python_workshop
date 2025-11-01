# Author : Balaji Nagaiahgari
# This is python program uses pyttsx3 module which basically reads the text that you pass in.
# Pre-requisite : install pyttsx3 module >> pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()

engine.say("my name is Balaji Nagaiahgari")
engine.runAndWait()