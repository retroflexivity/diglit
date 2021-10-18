import sys

punctls = ".,!?;:—–1234567890IVX"
endings = ["-й", "-ый", "-м", "-ым", "-го", "-ого", "-му", "-ому", "-ом"]

doc = open(sys.argv[1], "r+")
text = doc.read()

for i in punctls:
    text = text.replace(i,"")
for i in endings:
    text = text.replace(i,"")
text = text.replace("‑", "-")

print(text)
doc.seek(0)
doc.write(text)
doc.truncate()
doc.close()
