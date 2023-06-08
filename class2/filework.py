try:
    fh = open("file.txt","w")
    fh.write("this is my first line")

except IOError:
    print("File import error")
else:
    print("file written successfully")
