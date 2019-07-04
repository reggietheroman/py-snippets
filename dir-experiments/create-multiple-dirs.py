import os

def createDirs(dirs):
    try:
        for dir in dirs:
            os.mkdir(dir)
    except Exception as e:
        print ("Error creating directiories: %s" % e)

# run the code

dirs = ["./dir1", "./dir2", "./dir3"]

createDirs(dirs)
