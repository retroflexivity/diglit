from pymystem3 import Mystem
import sys

for year in range(2015, 2022):
    for month in range(4):
        if ((year == 2015) and (month < 2)):
            continue
        if ((year == 2021) and (month == 1)):
            break
        filename = str(year) + "_" + str(month)

        doc = open("trump_tw/cleansed/" + filename + ".txt", "r")
        text = doc.read()
        doc.close()

        m = Mystem()
        text = ''.join(m.lemmatize(text))

        out = open("trump_tw/lemmatized/" + filename + ".txt", "r+")
        out.seek(0)
        out.write(text)
        out.truncate()
        out.close()
