import speech_recognition as sr

def input_text_field():
	return str(input("\nenter - "))

def input_speech_field():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = 0.3
		r.energy_threshold = 101
		r.non_speaking_duration = 0.25
		audio = r.listen(source)
	try:
		query = r.recognize_google(audio, language="en-us")
	except Exception as e:
		return "None"

	return query.lower()

def is_triggered(question,trigger_word):
	if(trigger_word in question):
		return True
	else:
		return False

def trigger_input_field(trigger_word):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = 0.3
		r.energy_threshold = 1000
		r.non_speaking_duration = 0.25
		audio = r.listen(source)
		
	try:
		query = r.recognize_google(audio, language="en-us")
		if(trigger_word in query.lower()):
			return True

	except Exception as e:
		return False

	return  False
