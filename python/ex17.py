from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these on one line, how?
# indata = open(from_file).read()
in_file = open(from_file) # 打开文件
indata = in_file.read() # 读取文件。读取需要传递的字符串并返回一个值

print(f"The input file is {len(indata)} bytes long")
# len()：以数值的形式返回传递的字符串长度

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
# 以写入模式打开文件
out_file.write(indata)
# 将传递的字符串写入目标文件中

print("Alright, all done.")

out_file.close()
in_file.close()
# 对应上文的open，read则不需要，其运行后就会自动关掉

# (first make a sample file)
# echo "This is a test file" >ex17test.txt
# (then look at it)
# cat ex17_test.txt
# python ex17.py ex17_test.txt new_file.txt
