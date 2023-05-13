import os
import pickle
from typing_extensions import final

def getNames(fileType):
    files = []
    for dirpath, _, filenames in os.walk(os.getcwd()):
        for filename in filenames:
            if (fileType in filename):
                txtfile_full_path = os.path.join(dirpath, filename)
                files.append(txtfile_full_path)

    return files

def readDic(path):
    f = open(path, "rb")
    d = pickle.load(f)
    f.close()
    return d

def getDics(files):
    dics = []
    for i in files:
        print("Fetching file {}".format(i))
        dics.append(readDic(i))
    return dics

def allSummary(dics):
    pass

files = getNames(".pkl")
dics = getDics(files)

for count, i in enumerate(dics):
    print("Summary for {}".format(files[count]))
    print(i)
    print(" ")


finaldic = dics[0]
for i in range(1, len(dics)):
    # print("Combing {}".format(files[i]))
    # finaldic = dict(list(finaldic.items()) + list(dics[i].items()))
    for j in dics[i].keys():
        if j in finaldic.keys():
            finaldic[j] += dics[i][j]
        else:
            finaldic[j] = dics[i][j]

finaldic = dict(sorted(finaldic.items(), key=lambda x: x[1], reverse=True))
print("Summary of all words combined")
print(finaldic)