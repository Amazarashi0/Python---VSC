# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

# ok, that *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    # 直接用()里的名称作为变量名，解包参数可以被跳过
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one arguments
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# # # 函数(function)功能：1）给代码段命名；2）接收参数（or not）
# 定义函数：def 函数名(参数):
# 函数内容：     解包参数
#               其他（读取、写入、输出、打印、··· ···）
