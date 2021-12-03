from sys import argv # 导入模组及参数
# read the WYSS section for how to run this
sciript, first, second = argv # 将参数解包
print("the script is callde:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



#1：将sys模块导入脚本(script)（即你写的python程序）
# import(导入)语句——将python的模组（模块module，也称作库library）引入脚本
# argv——参数变量(argument variable):保存着运行python脚本时传递给脚本的参数。

#第3行——将argv解包：将argv中的内容取出，解包，将所有的参数依次赋值给左边的变量。

### 一旦程序用到argv，要注意调用程序时必须添加完整的命令行参数。
# 例如该程序需要传递3个命令行参数：python ex13.py first 2nd 3rd
# 变量不足错误提示：ValueError: not enough values to unpack (expected 3, got 1)

# 输入参数的区别：input & argv
# input：调用程序后脚本运行过程中用户输入参数
# argv：命令行调用程序时输入
