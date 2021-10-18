import sys

punctls = ".,!?;:—–1234567890"

doc = open(sys.argv[1], "r+")
text = doc.read()

for i in punctls:
    text = text.replace(i,"")
text = text.replace("‑", "-")
print(text)
doc.seek(0)
doc.write(text)
doc.close()
