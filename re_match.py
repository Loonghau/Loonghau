# -*- coding: utf-8 -*-
""" 
@Time : 2021/8/13 17:26
@Author : Loonghau XU
@FileName: re_match.py
@SoftWare: PyCharm
"""
# . 匹配任意1个字符（除了\n）
# [ ]   匹配[ ]中列举的字符[ab456c][a-z]
# \d    匹配数字，即0-9
# \D    匹配非数字，即不是数字
# \s    匹配空白，即 空格，tab键\t,\n
# \S    匹配非空白
# \w    匹配单词字符，即a-z、A-Z、0-9、_,国家的文字
# \W    匹配非单词字符

# 匹配任意一个数字
# 使用\d
# 判断用户是否输入的是速度与激情系列

# print(re.match("速度与激情\d", "速度与激情2").group())
# print(re.match("速度与激情\d", "速度与激情0").group())
# print(re.match("速度与激情\d", "速度与激情9").group())
# print(re.match("速度与激情\d", "速度与激情a").group())

# 使用[]
# 格式1:[单个值,...]
# 判断用户只想看1,4,8的速度与激情

# print(re.match("速度与激情[148]", "速度与激情1").group())
# print(re.match("速度与激情[148]", "速度与激情4").group())
# print(re.match("速度与激情[148]", "速度与激情8").group())
# print(re.match("速度与激情[148]", "速度与激情9").group())

# 格式2:[范围,...]
# 判断用户只看1到8的速度与激情
# print(re.match("速度与激情[12345678]", "速度与激情1").group())
# print(re.match("速度与激情[12345678]", "速度与激情8").group())
# print(re.match("速度与激情[1-8]", "速度与激情2").group())
# print(re.match("速度与激情[1-8]", "速度与激情8").group())
# print(re.match("速度与激情[1-8]", "速度与激情9").group())

# 格式3:[数字字符]
# 判断用户输入的速度与激情1到8或者速度与激情a-h
#
# print(re.match("速度与激情[1-8]", "速度与激情8").group())
# print(re.match("速度与激情[a-h]", "速度与激情a").group())
# print(re.match("速度与激情[a-h]", "速度与激情h").group())
# print(re.match("速度与激情[a-h]", "速度与激情e").group())
# print(re.match("速度与激情[1-8a-h]", "速度与激情a").group())
# print(re.match("速度与激情[1-8a-h]", "速度与激情8").group())


# 使用\w 即a-z、A-Z、0-9、_这个范围太广,不要轻易用,汉字也可以匹配,其他的国家的语言也可以匹配
# 匹配的单词字符
# 判断用户输入包含速度与激情

# print(re.match("速度与激情\w", "速度与激情8").group())
# print(re.match("速度与激情\w", "速度与激情a").group())
# print(re.match("速度与激情\w", "速度与激情z").group())
# print(re.match("速度与激情\w", "速度与激情A").group())
# print(re.match("速度与激情\w", "速度与激情Z").group())
# print(re.match("速度与激情\w", "速度与激情_").group())
# print(re.match("速度与激情\w", "速度与激情好").group())
# print(re.match("速度与激情\w", "速度与激情あなたのことが好きです").group())
#


# 使用\s
# --匹配空白字符
# --空格 或者 tab(\t),\n换行
# --判断用户速度与激情 8
# print(re.match("速度与激情\s8", "速度与激情 8").group())
# print(re.match("速度与激情\s8", "速度与激情\t8").group())
# print(re.match("速度与激情\s8", "速度与激情\n8").group())
# #

# --大写是所有小写的非*******

# .匹配任意1个字符（除了\n）
#   --匹配任意的字符
#   --判断包含速度与激情字符串的
# print(re.match("速度与激情.", "速度与激情\tadf").group())
# print(re.match("速度与激情.", "速度与激情\nadf").group())
