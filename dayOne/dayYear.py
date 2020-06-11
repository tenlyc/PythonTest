"""
输入年份 如果是闰年输出True 否则输出False
Verison:0.1
Author:李奕成

"""
year = int(input('请输入年份：'))
# 如果代码写的太长可以用\进行拆分
is_leap = year % 4 == 0 and year % 100 != 0 or \
    year % 400 == 0
print(is_leap)