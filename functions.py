import os

def cleanDir(input_):
    os.system("clear")
    print("clearing files....")
    
    for root, dirs, files in os.walk(input_):
     for name in files:
      print(os.path.join(root, name))
      os.remove(os.path.join(root, name))
    
    print("finding folders....")
    
    dirsFound = []
    for root, dirs, files in os.walk(input_):
        for name in dirs:
            print("found:" + os.path.join(root, name))
            dirsFound.append(os.path.join(root, name))
    
    print("ordering dirs...")
    
    dirsToDelete = []
    
    num = len(dirsFound) - 1
    while num != -1:
        dirsToDelete.append(dirsFound[num])
        print(dirsFound[num])
        num = num - 1
    
    print(dirsToDelete)
    
    for x in dirsToDelete:
        try:
            os.rmdir(x)
            print(x)
        except NotADirectoryError:
            print(x)
            os.remove(x)
    


