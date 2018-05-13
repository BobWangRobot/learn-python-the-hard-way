# -*- coding: utf-8 -*-

formatter = "%r %r %r %r" # 可以换成 %s 替换字符串，用 %d 替换整数。
#  只有在想要获取某些东西的调试信息时才能用到%r。%r给你的是变量的“程序员原始版本”，又被称作“原始表示”（raw representation）。

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # 里面有个单引号，所以输出时，外侧是双引号
	"So I said goodnight."
)