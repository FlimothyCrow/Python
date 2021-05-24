import os, re

def removeSpaces(str):
    return re.sub(' +', ' ', str).strip()

def renameUtility(path):
    files = os.listdir(path)
    counter = 0
    for index, file in enumerate(files):
        if os.path.isdir(os.path.join(path, ''.join(file))):
            renameUtility(os.path.join(path, ''.join(file)))
            name = list(file)
            newName = [' ' if i in [".", "[", "]", "{", "}", "(", ")", "+", "-"] else i for i in name[:-4]]
            newName = ''.join(newName + name[-4:])
            counter += 1 if file != newName else counter
            os.rename(os.path.join(path, file), os.path.join(path, ''.join(removeSpaces(newName))))
        else :
            name = list(file)
            newName = [' ' if i in [".", "[", "]", "{", "}", "(", ")", "+", "-"] else i for i in name[:-4]]
            newName = ''.join(newName + name[-4:])
            counter += 1 if file != newName else counter
            os.rename(os.path.join(path, file), os.path.join(path, ''.join(removeSpaces(newName))))
    print("total files renamed: %s" % counter)

renameUtility("C:\\Users\\Timothy\\Desktop\\target folder\\")

# renameUtility("D:\\Flim's Documents\\gegl-0.0\\plug-ins\\archives\BitTorrent downloads (complete)\\to be checked\\ww")

# build path parser to avoid having to add \\
