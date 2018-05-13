# -*- coding: utf-8 -*-

class Student(object): # 创建类
    def __init__(self, name, score): # 创建的空对象，以后调用需要传入两个参数
        self.name = name # 初始化
        self.score = score # 初始化

    def get_grade(self): # 定义函数
        if self.score >= 90: # 条件语句
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
  
# 以上可以封装。
          
lisa = Student('Lisa', 99) # 调用，传入2个参数
bart = Student('Bart', 59) # 调用，传入2个参数
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())