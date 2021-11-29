# 提问-用户输入

print("How old are you?", end = "")
age = input()
print("How tall are you?", end = "")
height = input()
print("Howmuch do you weight?", end = "")
weight = input()

print(f"So, you are {age} old, {height} tall and {weight} heavy.\n\n")

print("# the other example:\n")
print("\\*\fwhat is x\f?", end = "")
x = int(input("{}x = ".format("*" * 6)))
print("\\*\twhat is y ?", end = "")
y = int(input("*y = "))

print("#\t\bz = x + y =", x + y)

## 提问并输入答案
# 1）接收输入的内容
# 2）改变输入的内容
# 3）打印出输入的内容

## end = ""用来提示print不用换行符结束这一行

# # # Help on built-in function input in module builtins:
#
# input(prompt=None, /)
#     Read a string from standard input.  The trailing newline is stripped.
#
#     The prompt string, if given, is printed to standard output without a
#     trailing newline before reading input.
#
#     If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
#     On *nix systems, readline is used if available.

#    从标准输入中读取字符串，并取消换行尾符。
#    如果给出了提示字符串，则在读取输入前将不带换行尾符的提示字符串打印到标准输出。
