from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) # 将文件光标移动到文件的任意位置(针对字节而言)，然后对文件进行操作（增、删等）。

def print_a_line(line_count, f): # 逐行读取文件
	print line_count, f.readline() #readline()里面的代码会扫描文件的每一个字节，直到找到一个\n位置，然后它停止读取文件，
	#并且返回此前的文件内容，文件f会记录每次调用readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行了。

current_file = open(input_file) # 读取输入的文件

print "First let's print the whole file:\n"

print_all(current_file) # 之前定义的函数，读取文件

print "Now let's rewind, kind of like a tape."

rewind(current_file) #之前定义的函数，将光标移到起始位置

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)