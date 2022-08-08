import requests
response2 = requests.get('https://automatetheboringstuff.com/files/dictionary.txt')
response2.raise_for_status()
playfile = open('dictionary.txt', 'wb') # connect using 'wb' mode
for chunk in response2.iter_content(200): # method returns "chunk" of data
    playfile.write(chunk) # method writes the chunk to the file
    playfile.close()


read_data = [] # create an array
read_file = open('dictionary.txt', 'rb') # 'r' mode also works – what's included???
my_data = (read_file.readline()) # read a line
while my_data: # loop while there is something to
    read_data.append(my_data) # append a file line to the array
    my_data = (read_file.readline()) # read the next line
    print(len(read_data)) # how many lines in the array?
    print(read_data) # print the whole array
    for line in read_data: # loop through the array
        if read_data.index(line) < 100: # let's just print 100 lines
            print(read_data.index(line), line) # not all 4853!
   
    break
