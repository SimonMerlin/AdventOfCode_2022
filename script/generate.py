import os
import shutil

SOURCE_DIRECTORY = './../template'
SOURCE_FILE = 'decX_part1.py'


def copyTree(dest):
    if os.path.exists(os.path.join('..',dest)):
        raise Exception("Folder already exists, cannot create a new one")
    shutil.copytree(SOURCE_DIRECTORY, os.path.join('..',dest))
    print("Folder created in {}".format(os.path.join('..',dest)))

def renameFiles(day):
    for root, dirs, files in os.walk(os.path.join('..',day)):
        for name in files:
            if ".py" in name:
                newName = 'dec{}_{}.py'.format(day, root.split('\\')[-1])
                os.rename(os.path.join(root,name),os.path.join(root,newName))
                print("File ranamed in {}".format(os.path.join(root,newName)))

                    
if __name__ == '__main__':
    day = input("Day : ")
    copyTree(day)
    renameFiles(day)
