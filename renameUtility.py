import os, re

def filterString(fileName, fileType):
    if fileType == "folder":
        newName = list(re.sub("[\[{)\}(+\-.\]]", "", fileName))
        newName = ''.join(newName)
        return re.sub(' +', ' ', newName).strip()
    else :
        newName = list(re.sub("[\[{)\}(+\-.\]]", "", fileName[:-4]))
        newName = ''.join(newName + list(fileName)[-4:])
        return re.sub(' +', ' ', newName).strip()
# break regex into filter helper2 w/ tests (to include whitespace filtration from line 7/11)
def renameUtility(path):
    files = os.listdir(path)
    renameFilesCount = 0
    for index, file in enumerate(files):
        if os.path.isdir(os.path.join(path, ''.join(file))):
            renameFilesCount += renameUtility(os.path.join(path, ''.join(file)))
            newName = filterString(file, "folder")
            rejoinedPathName = os.path.join(path, ''.join(newName))
            # os.rename(os.path.join(path, file), rejoinedPathName)
        else :
            newName = filterString(file, "file")
            if newName != file:
                renameFilesCount = renameFilesCount + 1
                # print("rename files count " + str(renameFilesCount))
                os.rename(os.path.join(path, file), os.path.join(path, ''.join(newName)))

    return renameFilesCount

# renameUtility("C:\\Users\\Timothy\Desktop\\target folder\\subTargetFolder")
# build path parser to avoid having to add \\
# line 25 is hitting, but renameFilesCount isn't being updated?