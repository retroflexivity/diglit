# import sys
import spacy

nlp = spacy.load("en_core_web_sm")
lemmatizer = nlp.get_pipe("lemmatizer")
print(lemmatizer.mode)

for year in range(2015, 2021):
    for month in range(4):
        if ((year == 2015) and (month < 2)):
            continue
        if ((year == 2021) and (month == 1)):
            break

        filename = str(year) + "_" + str(month)

        doc = open("trump_tw/cleansed/" + filename + ".txt", "r")
        text = doc.read()
        doc.close()

        text = nlp(text)
        for token in text:
            print(token.lemma_)

        out = open("trump_tw/lemmatized/" + filename + ".txt", "r+")
        out.seek(0)
        for token in text:
            out.write(token.lemma_ + " ")
        out.truncate()
        out.close()
