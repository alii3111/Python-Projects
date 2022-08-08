import shelve

shelfFiles = shelve.open("mydata")

cats = ['xoom', 'poom', 'koom', 'doom']

shelfFiles['cats'] = cats
list(shelfFiles.keys())
list(shelfFiles.values())

shelfFiles.close()