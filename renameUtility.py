import os

def renameUtility(path):
    files = os.listdir(path)
    for index, file in enumerate(files):
        name = list(file)
        newName = [' ' if i in [".", "[", "]", "{", "}"] else i for i in name[:-4]]
        newName = ''.join(newName + name[-4:])
        os.rename(os.path.join(path, file), os.path.join(path, ''.join(newName)))


renameUtility("C:\\Users\\Timothy\\Desktop\\target folder\\subFolder0")

