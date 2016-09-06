#Python script

wiki = open("wiki.txt")
mywords = wiki.read().split()
print (mywords)

wiki.close()
