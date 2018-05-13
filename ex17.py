# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
# in_file = open(from_file) # 写完open就及时写close
# indata = in_file.read() # 这个不用写close

# indata = open(from_file).read() # 无需再运行close()了，因为read()一旦运行，文件就会被python关掉
# print "The input file is %d bytes long" % len(indata)

# print "Does the output file exists? %r" % exists(to_file) 
# exists函数将文件名字符串作为参数，如果文件存在的话，返回TRUE，否则返回FALSE。

# print "Ready, hit RETURN to continue, CTRL-C abort."
# raw_input()

# out_file = open(to_file, 'w') #记得写close
# out_file.write(indata) #无需写close

out_file = open(to_file, 'r+').write(open(from_file).read())

# print "Alright, all done."

# out_file.close()
# in_file.close()