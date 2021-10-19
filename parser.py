import sys
import re

punctls = ".,!?;:—–1234567890"
# endings = ["-й", "-ый", "-м", "-ым", "-го", "-ого", "-му", "-ому", "-ом"]

doc = open(sys.argv[1], "r+")
text = doc.read()
doc.close()

text = re.sub('https://t.co/[0-z]*', "", text)

for i in punctls:
    text = text.replace(i,"")

# for i in endings:
#     text = text.replace(i,"")
# text = text.replace("‑", "-")

print(text)
# output = open(sys.argv[2], "r+")
# output.seek(0)
# output.write(text)
# output.truncate()
# output.close()
