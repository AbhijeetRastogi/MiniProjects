import os

chat_file = os.path.dirname(__file__) + "\\input.txt"
chat_text = str()

output = open(os.path.dirname(__file__) + "\\result.txt", "w", encoding='utf-8')

for chat_text in open(chat_file, encoding="utf8"):
    if "<Media omitted>" not in chat_text:
        pos = chat_text.rfind("M - ")# find the last ":"
        chat_text = chat_text[(pos+4):]
        chat_text = chat_text[: chat_text.find(' ')] + chat_text[chat_text.rfind(": "):] 
        output.write(chat_text)
output.close()