import os
import os.path as dir
import fnmatch
import re
import Rhino
from scriptcontext import doc

def fileHisory():
    path = dir.dirname(doc.ActiveDoc.Path)
    filename = dir.splitext(dir.basename(doc.ActiveDoc.Name))[0]
    
    folder = dirHistory(path)

    revHistory(filename, folder)

def revHistory(filename, folder):
    files = []
    filter = filename + '*.3dm'
    for (dirpath, dirnames, filenames) in os.walk(folder):
        files.extend(filenames)
        break

    print files
    files = fnmatch.filter(files, filter)
    print files
    
    count = len(fnmatch.filter(files, filter))

    print int(files[0][-7:-4])


def dirHistory(path):
    a = dir.join(str(path), '_history')
    if not dir.exists(a):
        os.makedirs(a)
        print "History folder created"
    else:
        print "History folder located"
    return a



if __name__ == "__main__":
    fileHisory()
