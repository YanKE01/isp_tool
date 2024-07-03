import matplotlib.pyplot as plt

# 曲线数据
data = [
    (0, 0),
    (16, 38),
    (32, 62),
    (48, 83),
    (64, 101),
    (80, 118),
    (96, 134),
    (112, 150),
    (128, 164),
    (144, 178),
    (160, 192),
    (176, 205),
    (192, 218),
    (208, 231),
    (224, 243),
    (240, 255)
]

# 分离 x 和 y 数据
x_data, y_data = zip(*data)

# 创建一个图形
plt.figure(figsize=(10, 6))

# 绘制曲线
plt.plot(x_data, y_data, marker='o', linestyle='-', color='b', label='Curve')

# 添加标签和标题
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Curve Plot')
plt.legend()

# 显示网格
plt.grid(True)

# 显示图形
plt.show()
