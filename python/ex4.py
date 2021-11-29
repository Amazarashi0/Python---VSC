# 定义并赋值变量(variable)

cars = 100 # 将100赋给变量名为"car"的变量
space_in_a_car = 4.0 # 变量名中的符号 _ 表示空格
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # 将两变量计算的值赋给新变量
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars availible.")
print ("There are only", drivers, "drivers availible.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "peopple today")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

print ("three are", 100, "cars available.")

# (4) print() 函数可以直接输出函数体中变量名对应变量的值

# “=”：为变量赋值。将右边的值赋给左边的变量名
# "=="：检查左右两边的值是否相等

# # # Help on built-in function print in module builtins:
# print(...)
#    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
#    Prints the values to a stream, or to sys.stdout by default.
#    Optional keyword arguments:
#    file:  a file-like object (stream); defaults to the current sys.stdout.
#    sep:   string inserted between values, default a space.
#    end:   string appended after the last value, default a newline.
#    flush: whether to forcibly flush the stream.
