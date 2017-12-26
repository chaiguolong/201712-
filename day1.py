#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 字符串要格式化后再输出，不要使用+号去拼接，否则会造成多次访问内存，引起效率下降
import copy
name = "baby_plus"
st = "test %s" % name
print("test %s %s" % (name, name))
print(st)
# 数据类型：列表（数组）,通过下标取值,以及各种取值方式,取值的时候后面的下标的值不取，并且只能从左往右取值
lis = ["1", "two", 3, name, st]
for n in range(4):
    print("---")
    print(lis[n])
    print(lis[-(n+1)])
    print(lis[1:4])
    print(lis[2:])
lis.append("append")
lis.insert(2, "insert")
print(lis[:])
print(lis[-6:-1])
lis.remove("two")
lis2 = lis.copy()
print("lis2=", lis2)
# 引入copy庫可以进行深度复制,若不使用该函数的话，就只能进行第一层的复制
lis_deep = [1, 2, 3, 2, lis]
lis2_copy = lis_deep.copy()
lis2_deepcopy = copy.deepcopy(lis_deep)
lis_deep[4][3] = "changed".center(10,"*")
print("lis2_copy=", lis2_copy)
print("lis2_deep=", lis2_deepcopy)
# [::]里面第一个参数为起始位置，第二个为结束位置，第三个为步进
lis3 = lis_deep[::2]
print(lis3)
# 对列表进行拓展
lis_deep.extend(lis_deep)
print("测试extend 函数 对列表进行拓展", lis_deep)
# count计数，计算出相同值的个数
lis_count = lis_deep.count(2)
print("测试 count计数，计算出相同值的个数:[%s] \n list=%s" % (lis_count, lis_deep))
# 配合if in 判断，index找位置,然后修改
for n in range(lis_count):
    print("测试 count计数 %s".center(30,"-") % n)
    if 2 in lis_deep:
        lis_ele_position = lis_deep.index(2)
        print("测试index 函数取出第一个值：", lis_deep[lis_ele_position])
        lis_deep[lis_ele_position] = n+1
        print(lis_deep[lis_ele_position])

# reverse 函数用于反向，solt 函数用于排序
lis_deep.reverse()
print("测试 reverse函数用于反向：{test} \n\n{test2}".format(test = lis,test2 = lis_deep))

# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
print("测试 pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值：", str(len(lis_deep)).center(50,"+"))
lis_deep.pop()
print("测试 pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值：", str(len(lis_deep)).center(50,"+"))
# del 全局命令，删除内存里的数据
print(lis_deep)
del lis_deep[:6]
print("测试del: ", lis_deep)

"""
20160925补充
enumerate 方法可以取出索引，生成元组
"""
for index, i in enumerate(lis_deep):
    print("测试enumerate ", "索引：", index, "内容： ", i)




























