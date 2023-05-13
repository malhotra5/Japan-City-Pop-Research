import os
import re
import string
import pickle
from deep_translator import GoogleTranslator


def getNames(album):
    files = []
    for dirpath, _, filename in os.walk(os.getcwd()):
        for filename in filename:
            if("finalWordAnal" not in dirpath and album in dirpath):
                txtfile_full_path = os.path.join(dirpath, filename)
                files.append(txtfile_full_path)

    return files


def splitLanguage(text):
    res = []
    start = False
    s = ""
    for i in text:
        if ord(i) > 256:
            if (start == False):
                start = True
            if (start == True):
                s = s + i
        else:
            if start == True:
                start = False
                res.append(s)
                s = ""

    return res

def englishPercent(text):
    text = text.replace("\n", " ")
    text = text.replace("\u3000", " ")
    jWords = splitLanguage(text)
    allWords = text.split(" ")
    return len(allWords) - len(jWords), len(allWords)
    

def readFiles(n):
    f = open(n, errors="ignore", encoding='utf8')
    text = f.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    ecount, acount = englishPercent(text)
    # print("The total percentage of English words is {}".format([percentage]))
    f.close()
    if (len(text) <= 5000):
        text = GoogleTranslator(source='auto', target='en').translate(text)
    else:
        n = 5000
        chunks = [str[i:i+n] for i in range(0, len(str), n)]
        for i in range(len(chunks)):
            chunks[i] = GoogleTranslator(source='auto', target='en').translate(chunks[i])

        text = "".join(chunks)

    return text, ecount, acount

def wCount(text, dic):
    s = text.replace("\n", " ")
    s = s.split()
    for i in s:
        w = i.lower()
        if w in dic.keys():
            dic[w] += 1
        else:
            dic[w] = 1

    return dic

def readAlbum(files):
    songs = []
    e = 0
    a = 0
    for i in files:
        print("Reading file {}".format(i))
        t, eword, aword = readFiles(i)
        songs.append(t)
        e += eword
        a += aword
    return songs, e/a

def createAnal(texts, dic):
    for i in texts:
        wCount(i, dic)

def saveDic(dic, path):
    file = open(path + ".pkl", "wb")
    pickle.dump(dic, file)
    file.close()

def readDic(path):
    file = open(path, "rb")
    d = pickle.load()
    file.close()
    return d


albumNames = ["circus town", "spacy", "moonglow", "ride on time", "for you", "big wave", "artisan", "season's greetings", "cozy"]
for i in albumNames:
    names = getNames(i)
    songs, perc = readAlbum(names)
    print("The total percentage of English words is {}".format(perc))
    count = {}
    createAnal(songs, count)
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    saveDic(count, "finalWordAnal/{}".format(i))
