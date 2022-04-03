result = open("result.txt", "w", encoding='utf-8')
new = open("new.txt", encoding="utf8")
old = open("old.txt", encoding="utf8")


for i in old:
    last_common = i

chat_text = str()
count = 0 

for chat_text in new:
    if (chat_text in last_common):
        count = -1
    if count == -1:
        result.write(chat_text)
        
result.close()
new.close()
old.close()