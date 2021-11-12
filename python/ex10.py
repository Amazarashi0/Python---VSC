tabby_cat = "\tI'm tabbed in."
persian = "I'm split\n on a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian)
print(backlah_cat)
print(fat_cat)


#转义序列(escape sequence)：
# \\ 反斜杠(\)
# \' 单引号
# \" 双引号
# \a ASCII响铃符(BEL)
# \b ASCII退格符(BS)
# \f ASCII进纸符(FF)
# \n ASCII换行符(LF)
# \r ASCII回车符(CR)
# \t ASCII水平制表符
# \v ASCII垂直制表符
# \uxxxx 值为16位十六进制值xxxx的字符
# \Uxxxxxxxx 值为32位十六进制值xxxxxxxx的字符
# \ooo 值为八进制值ooo的字符
# \xhh 值为十六进制值hh的字符
# \N{name} Unicode数据库中的字符名，其中name是它的名字，仅Unicode适用
