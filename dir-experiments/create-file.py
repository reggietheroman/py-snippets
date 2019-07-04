def createFile(path):
    try:
        open(path, "w+")
    except Exception as e:
        print ("File %s not created." % path)
        print ("Error: %s" % e)

# run the code

path = "./tmp.txt"

createFile(path)
