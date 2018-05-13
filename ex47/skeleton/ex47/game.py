class Room(object): # 创建Room类

	def __init__(self, name, description): # 在Room类下创建下空对象
		self.name = name # 初始化
		self.description = description # 初始化
		self.paths = {} # 初始化

	def go(self, description): # 定义函数
		return self.paths.get(description, None)

	def add_paths(self, paths): # 定义函数
		self.paths.update(paths)
		