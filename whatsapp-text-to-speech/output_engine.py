import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def text_to_speech(text):
	engine.say(text)
	engine.runAndWait()

def print_text(text):
	print(text)

def tts_and_print(text):
	print_text(text)
	text_to_speech(text)