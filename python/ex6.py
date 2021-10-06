# 字符串和文本

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "do't"
y = f"Thoese who know {binary} and those who {do_not}."

print (x)
print (y)

print (f"I said: {x}") # 两层格式化
print (f"I also said: {y}")


hilarious = False
joke_evaluation = "Is't that joke so funny? {}!"

print (joke_evaluation.format (hilarious)) # 第二种格式化方法：".format()"
print (f"Is't that joke so funny? {hilarious}！") # 第一种格式化方法："f-string"

print ("Is't that joke so funny? {}!".format("False")) # ".format()"


w = "This is the left side of..."
e = "a string with a right side."

print (w + e)

# () print()函数中可以用 + 使两个字符串顺序相接
