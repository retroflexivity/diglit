from pymystem3 import Mystem
import sys

doc = open(sys.argv[1], "r")
text = doc.read()
doc.close()

m = Mystem()
text = ''.join(m.lemmatize(text))

print(text)
output = open(sys.argv[2], "r+")
output.seek(0)
output.write(text)
output.truncate()
output.close()
