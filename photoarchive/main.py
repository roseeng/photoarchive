import persist
import photoarchive
import sys

folder = r"C:\Users\g\Pictures\Scannat"
#print(photoarchive.filetypes)
if (len(sys.argv) > 1):
    folder = sys.argv[1]

filedict = persist.ReadDictionary()
print("Read {} files from db".format(len(filedict)))

treatedfiles = persist.ReadTreatedFiles()
print("Read {} treated files".format(len(treatedfiles)))
newtreatedfiles = list()

try:
    photoarchive.Manage(folder, treatedfiles, filedict, newtreatedfiles)
except KeyboardInterrupt:
    print("aborted by user")
except Exception as ex:
    print("Error: " + str(ex))

persist.SaveDictionary(filedict)
persist.SaveTreatedFiles(newtreatedfiles)
