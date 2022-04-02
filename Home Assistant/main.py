import sys
import time

import message_processor
import input_engine
import output_engine
from playsound import playsound


def welcome():
	playsound(str(sys.path[0])+'\\Audio\\beep.wav')
	time.sleep(1)
	message = "WELCOME \nI am your assistant \nHow can I help you?\n"
	output_engine.tts_and_print(message)
	
def exit_message():
	message = "Bye I hope to see you soon"
	output_engine.tts_and_print(message)


if __name__=="__main__":
	welcome()
	
	is_loop = True
	trigger_word = "alexa"

	while is_loop:

		question = input_engine.input_speech_field()

		if input_engine.is_triggered(question,trigger_word):

			playsound(str(sys.path[0])+'\\Audio\\end.wav')
			print(question)
			solution = message_processor.message_processor(question)
			output_engine.tts_and_print(solution)
			print()

			if "exit" in question:
				exit_message()
				is_loop = False
			
