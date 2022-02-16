import torch
print(torch.__version__)
print(torch.cuda.is_available())

x = torch.empty(5, 3)
print(x)

# 随机初始换一个矩阵
y = torch.rand(3,3)
print(y)
# print(x* y)

# 使用索引来操作torch 张量
print(x[1,1])

# view 操作相当于reshape
z = y.view(9)
print(z)
op = z.view(-1, 3)
# print(op.size())
print(op)

# 元素的获取
# 如果你有只有一个元素的张量，使用.item()来得到Python数据类型的数值

x = torch.randn(1)
print(x)
print(x.item())

# numpy 与 torch的转化
# Torch Tensor与NumPy数组共享底层内存地址，修改一个会导致另一个的变化。

# 将一个Torch Tensor转换为NumPy数组
a = torch.ones(2,2)
b = a.numpy()

print(a)
print(b)

# 使用numpy 与torch之间的转化
import numpy as np
c = np.ones(3)
d = torch.from_numpy(c)
print(c)
print(d)
print(np.add(c,2))

#tensor 默认的计算都是在cpu里面进行的

# CUDA
# 使用.to 方法 可以将Tensor移动到任何设备中
# is_available 函数判断是否有cuda可以使用
# ``torch.device``将张量移动到指定的设备中
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA 设备对象
    y = torch.ones_like(x, device=device)  # 直接从GPU创建张量
    x = x.to(device)                       # 或者直接使用``.to("cuda")``将张量移动到cuda中
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` 也会对变量的类型做更改


