import output_engine

chat_file = "result.txt"

for chat_text in open(chat_file, encoding="utf8"):
	output_engine.tts_and_print(chat_text)