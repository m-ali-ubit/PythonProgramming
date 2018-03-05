
# taking input from user
i = input('enter anything:')           # takes input and store it in i
print(i)                               # prints the value of i

# file open and close
f = open('checkModes.txt', 'r')        # read-only mode
f.close()                              # close the file
f = open('checkModes.txt', 'rb')       # read-only binary format mode
f.close()
f = open('checkModes.txt', 'r+')       # read and write mode
f.close()
f = open('checkModes.txt', 'rb+')      # read and write binary format mode
f.close()
f = open('checkModes.txt', 'w')        # write mode ; overwrite file if exist otherwise creates one
f.close()
f = open('checkModes.txt', 'wb')       # write binary format mode ; overwrite file if exist otherwise creates one
f.close()
f = open('checkModes.txt', 'w+')       # read and write mode ; overwrite file if exist otherwise creates one
f.close()
f = open('checkModes.txt', 'wb+')      # read and write binary format mode;overwrite file if exist otherwise creates one
f.close()
f = open('checkModes.txt', 'a')        # append mode
f.close()
f = open('checkModes.txt', 'ab')       # append binary format mode
f.close()
f = open('checkModes.txt', 'a+')       # append and read mode
f.close()
f = open('checkModes.txt', 'ab+')      # append and read binary format mode
f.close()

# file object attributes
# file closed
print(f.closed)                        # returns true if file is closed else false

# file name
print(f.name)                          # returns file name

# file mode
print(f.mode)                          # returns file mode


# read and write file
# read file
fr = open('read.txt', 'r+')            # open file in read and write mode
# when we open the file the pointer is placed at beginning of file
print(fr.read())                       # read() ; reads the whole file
fr.close()

fr = open('read.txt', 'r+')
print(fr.read(10))                     # read(10) ; reads only 10 characters
fr.close()

fr = open('read.txt', 'r+')
print(fr.readline())                   # reads line by line
fr.close()

# write file
fw = open('write.txt', 'r+')
fw.write('Python is a interpreted and high-level programming language.\nPython is a general purpose language')
fw.close()

# to check its done or not go check the file write.txt or we can read that file
fo = open('write.txt', 'r+')
print(fo.read())                      # its working
fo.close()

# some other methods
fo = open('write.txt', 'r+')          # when we open the file, file pointer is on the beginning.
print(fo.read(10))                    # 'Python is '

# passing read(10) reads 10 characters and pointer moves to position 10
# if we run read(10) again, this will print 10 characters from the 11th character position
print(fo.read(10))                    # 'a interpre'
print(fo.tell())                      # 20    ;   read(!0) + read(10) = 20 - pointer's position
fo.seek(0, 0)                         # put pointer to the start of the file
print(fo.tell())                      # 0
fo.close()

# os.rename('text1.txt', 'text2.txt') to rename the file
# os.remove('text.txt') to remove the file
# there are lot more file object and os object methods can be learned from python docs
