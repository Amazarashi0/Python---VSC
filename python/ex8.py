formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "Mabe a poem",
    "or a song about fear"
))

# 函数(function)：formatter.format(...)
# (1)取定义的formatter字符串；
# (2)调用它的format函数，这相当于告诉它执行一个叫作format的命令行命令；
# (3)给format传递4个参数，这些参数和formatter变量中的{}匹配，相当于将参数传递给了format这个命令。

# 即：将 format(...) 中的参数传递给字符串 formatter 中的变量{}。

# True 和 False 是Python中的关键字，所以不需要加引号，加引号后就成为字符串了。
