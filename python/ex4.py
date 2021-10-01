# 定义并赋值变量
cars = 100 # 将100赋给变量名为"car"的变量
space_in_a_car = 4.0
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

# “=”：为变量赋值。将右边的值赋给左边的变量名
# "=="：检查左右两边的值是否相等
