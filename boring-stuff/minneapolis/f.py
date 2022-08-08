
myFile = open('index.txt', 'a')
myFile.write("\nGood Morning world \n")
content = myFile.read()

myFile.close()
print(content)