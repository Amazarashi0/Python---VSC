from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Open the file...")
target =  open(filename, 'w')
# open(filename,'w') w是指文件的访问模式是“写入模式”
# open函数默认文件访问模式是r——只读模式。

print("Turncating the file. Goodbey!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3)

print("And finally, we close it.")
target.close()

# 文件命令：
#     close: 关闭文件。与编辑器中的‘文件’——‘保存’一个意思
#     read: 读取文件内容。返回结果可以赋值给一个变量。
#     readline: 读取文本文件的一行。
#     truncate: 清空文件。
#     write('stuff'): 将"stuff"写入文件。
#     seeek(0): 将读写位置移动到文件开头。
