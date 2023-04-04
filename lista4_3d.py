import os, sys
from subprocess import Popen, PIPE

argv = sys.argv[1::]

lines = []

for i in argv:
    process = Popen(["python3", "lista4_3abc.py"], stdin=PIPE, stdout=PIPE, text=True)
    process.stdin.write(i)
    process.stdin.close()
    lines.append(process.stdout.readline().strip())



results = []
#sign_count, word_count, lines_count, sign_max, count, word_max, count_w
for line in lines:
    temp = line.split("\t")
    # przekształca dane wyjściowe procesu na słownik jeżeli nie wystąpił błąd
    if not temp[0].__contains__("#"): results.append({"sign_count":int(temp[0]), "word_count":int(temp[1]), "lines_count":int(temp[2]), "sign_max":temp[3], "word_max":temp[4]})


files = 0
signs = 0
words = 0
lines = 0
signs_dict = {}
words_dict = {}
sign = ""
word = ""
for dictionary in results:
    
    files+=1
    signs+=dictionary["sign_count"]
    words+=dictionary["word_count"]
    lines+=dictionary["lines_count"]
    if signs_dict.get(dictionary.get("sign_max")): signs_dict[dictionary.get("sign_max")] += 1
    else: signs_dict[dictionary.get("sign_max")] = 1
    if words_dict.get(dictionary.get("word_max")): words_dict[dictionary.get("word_max")] += 1
    else: words_dict[dictionary.get("word_max")] = 1


# sprawdzanie najliczniejszego znaku
count=0
for entry in signs_dict:
    temp_c = signs_dict[entry]
    if temp_c>count:
        sign=entry
        count=temp_c

# sprawdzanie najliczniejszego słowa
count_w=0
for entryw in words_dict:
    temp_w = words_dict[entryw]
    if temp_w>count_w:
        word=entryw
        count_w=temp_w

# wynik
print("pliki: {}\nznaki: {}\nsłowa: {}\nlinie: {}\nnajpopularniejszy znak: {}\nnajpopularniejsze słowo: {}\n".format(files, signs, words, lines, sign, word))