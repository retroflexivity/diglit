# import sys
import re

punctls = '“”".,!?;—–&'

for year in range(2015, 2022):
    for month in range(4):
        if ((year == 2015) and (month < 2)):
            continue
        if ((year == 2021) and (month == 1)):
            break
        filename = str(year) + "_" + str(month)
        # print(filename)

        unpsd = open("trump_tw/unparsed/" + filename + ".txt", "r")
        unps = unpsd.read()
        unpsd.close()


        ps = re.sub('........t.co/[0-z]+', "", unps)
        ps = ps.replace(' - ', " ")
        ps = ps.replace("%", "percent")
        ps = ps.replace(": ", " ")
        ps = ps.replace(":\n", "\n")

        usr = re.findall('@[&-z’]+', ps)
        ps = re.sub('@[&-z’]+', "", ps)

        hst = re.findall('#[&-z’]+', ps)
        ps = re.sub('#[&-z’]+', "", ps)


        for i in punctls:
            ps = ps.replace(i,"")

        if (filename == "2015_2"):
            print(ps)

        psd = open("trump_tw/cleansed/" + filename + ".txt", "r+")
        psd.seek(0)
        psd.write(ps)
        psd.truncate()
        psd.close()

        usrd = open("trump_tw/hashtags/" + filename + ".txt", "r+")
        usrd.seek(0)
        for i in hst:
            usrd.write(i + "\n")
        usrd.truncate()
        usrd.close()

        hstd = open("trump_tw/users/" + filename + ".txt", "r+")
        hstd.seek(0)
        for i in hst:
            hstd.write(i + "\n")
        hstd.truncate()
        hstd.close()
