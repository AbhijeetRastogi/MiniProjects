from datetime import datetime
import webbrowser

def message_processor(question):

	ans = str()
	
	if (("time" or "now") in question):
		now = datetime.now()
		d = datetime.strptime(str(now.hour),"%H")
		ans = "The time is "+d.strftime(f"%I:{now.minute} %p")

	elif "how are you" in question:
		ans = "I am fine. Thanks for asking"

	elif "open" in question:
		if "google" in question:
				webbrowser.open('https://www.google.com')
				ans = "opening"
		elif "gmail" in question:
				webbrowser.open('https://www.gmail.com')
				ans = "opening"
	return ans