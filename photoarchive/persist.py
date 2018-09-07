import json
from filedata import Filedata

def ReadDictionary():
    filedict = dict()

    with open('filedict.json') as f:
        tmpArr = json.load(f)

        for item in tmpArr:
            fdata = Filedata(**item)
            #print(fdata.filename)
            filedict[fdata.hash] = fdata

    return filedict

def SaveDictionary(filedict):
    tmpArr = []
    for item in filedict.values():
        tmpArr.append(item.__dict__)
    
    with open('filedict.json', 'w') as f:
        json.dump(tmpArr, f, indent=4)

def FindInDict(fdata, filedict):
    for item in filedict.values():
        if (fdata.EqualTo(item)):
            return True

    return False

def ReadTreatedFiles():
    treatedfiles = set()

    with open('treatedfiles.txt', encoding="utf_8") as f:
        for line in f:
            a = line.split(sep=",", maxsplit=1)
            line = a[0]
            line = line.rstrip("\n")
            treatedfiles.add(line)

    return treatedfiles

def SaveTreatedFiles(treatedfiles):    
    with open('treatedfiles.txt', 'a', encoding="utf_8") as f:
        for tf in treatedfiles:
            f.write(tf + "\n")

    print("Saved {} treated files".format(len(treatedfiles)))