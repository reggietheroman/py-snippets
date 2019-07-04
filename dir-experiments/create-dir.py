import os

def newDir(path):
    try:
        os.mkdir(path)
    except OSError:
        print ("Creating directory failed with: %s" % path)
    else:
        print ("Successfully created directory %s" % path)

# run the code

path = "./temp"

newDir(path)
