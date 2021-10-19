import spacy

nlp = spacy.load("en_core_web_sm")
names = []

for year in range(2015, 2022):
    for month in range(4):
        if ((year == 2015) and (month < 2)):
            continue
        if ((year == 2021) and (month == 1)):
            break
        filename = str(year) + "_" + str(month)

        file = open("trump_tw/cleansed/" + filename + ".txt", "r")
        doc = file.read()

        doc = nlp(doc)

        for token in doc:
            if ((token.pos_ == "PROPN") and (token.dep_ == "nsubj") and not(token.text in names)):
                names.append(token.text)

print(names)
