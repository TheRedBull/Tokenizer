import collections
import os
import string
import sys

#find and use the path of this program to locate the text files to be read/tokenized
path = os.path.dirname(os.path.abspath(__file__))
#the master file contains the list of the files to be read/tokenized
fileList = open("masterList.txt","r")
#create a new/empty list
masterFileList = []

for fileName in fileList:
    #system out to let you know which file is being processed
    sys.stderr.write("Looking for %s" % fileName)
    #join the path to the file name - this allows the file to be found
    filePathName = os.path.join(path, fileName.rstrip('\n'))
    #check if the files in the master list exist and can be opened
    try:
        f=fileContent = open(filePathName, 'r')
        f.close
        print("Found! Reading %s" % fileName)
    #catch the error if a file is in the master list but doesn't really exist
    except IOError:
        sys.stderr.write('***WARNING*** File does not exist: %s\n' % fileName)
    #for existing files
    if (os.path.exists(fileName)):
        fileContent = open(filePathName, 'r')
        #read the contents of the file and convert to lowercase
        lowercase = fileContent.read().lower()
        #remove the punctuations
        strip = lowercase.translate(None, string.punctuation)
        #split each word based on whitespace
        tokenize = strip.split()
        #appens each files contents into the list
        masterFileList.extend(tokenize)
        #close the file after read
        fileContent.close()
print "\nAll files have been read. Here is the list of unique words and their frequency across all files:"

counter = collections.Counter(masterFileList)
for word, count in counter.most_common():
    print("{0} {1}".format(word, count))
