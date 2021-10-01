# 数字和数字运算

print ("I wil now count my chickens:")

print ("Hens", 25 + 30 / 6)
print ("Roosters", 100 - 25 * 3 % 4) # 100 - [（25 * 3） / 4]的余数 = 100 - 3 = 97

print ("Now I will count the eggs:")

print (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print ("Is it true that 3 + 2 < 5 - 7 ?") # 对数学命题真假进行询问。该问询语法只能独占一个print函数使用

print (3 + 2 < 5 - 7)

print ("What is 3 + 2?", 3 + 2) # 只能问询真假
print ("What is 5 - 7?", 5 - 7)

print ("Oh, that's why it is False.")

print ("How about some more.")

print ("Is it greater?", 5 > -2) # 该问询语法可以与其它语句连用
print ("Is it greater or equal?", 5 >= -2) #True
print ("Is it less or equal?", 5 <= -2) #False

print ("Let's get some floating number")
print (5.0 + 6.0 * 900)

print ("1) Is it greater?", 5 > -2, "2) What is 3 + 2?", 3 + 2, "3)", 5.0 + 6.0 * 900)
# 多个语句之间用 ，分隔

# (2) print()函数体中可直接进行数字运算（整型、浮点型）并打印出结果
# (3) print()函数可以对数学命题真假进行询问并得到答案："True" or "False"


# 运算优先级： "PEMDAS"即"PE(M&D)(A&S)"---
# 一 括号(Parentheses)，
# 二 指数(Exponents)，
# 三 乘(Multiplication)，除(Division)，
# 四 加(Addition)，减(Subtraction)
