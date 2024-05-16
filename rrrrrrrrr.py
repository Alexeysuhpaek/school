from collections import Counter
with open('music.txt',encoding="utf8") as f:
    baobab = f.read()
    # for row in f.readlines():
    #     print(row)
# print(baobab)
buba_list = []
banned = [' ','.',',','!','"',':','\n']
lyrics_word = ''
for w in baobab:
    w = w.lower()
    if w not in banned:
        lyrics_word+=w
    else:
        buba_list.append(lyrics_word)
        lyrics_word = ''



hepustoi_slovar = {}
for w in buba_list:
    if w not in hepustoi_slovar:
        hepustoi_slovar[w] = 1
    else:
        hepustoi_slovar[w]  += 1

print(hepustoi_slovar.get)


a = Counter(buba_list)
print (a.most_common(4))