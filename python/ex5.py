# 字符串：用 "" 把一些文本括起来就创建了一个字符串："text"
# 字符串可以作为值赋给变量
my_name = "Zed A .Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = "blue"
my_teeth = "white"
my_hair = "brown"

# 格式化字符串(format string)：把字符串内的变量返回对应的值
# 用 {} 可以将变量嵌入字符串内
# 字符串可以通过 print() 函数被打印出来
print (f"Let's talk about {my_name}.")
print (f"he's {my_height} inche tall.")
print (f"he's {my_weight} ponuds heavy.")
print ("Actually that's not too heavy.")
print (f"he's got {my_eyes} eyes and {my_hair} hair.")
print (f"he's teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print (f"If I add {my_age},{my_height}, and {my_weight} I get {total}.")


print ("my height =", 74 * 2.54, "cm.")
print ("my weight =", 180 * 0.4536, "kg.")
