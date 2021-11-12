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

# 提问并输入答案
# 1）接收输入的内容
# 2）改变输入的内容
# 3）打印出输入的内容
