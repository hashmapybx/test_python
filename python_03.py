# 自定义网络接口

"""
首先说明一个神经网络的训练过程：
1、定义一些需要学习的参数（w b）的network model
2、在数据集上面进行迭代
3、通过input得到output
4、计算loss,(输出结果和正确值的差值)
5、讲梯度反向传播回网络的参数
6、更新网络参数 weight = weight - learning_rate * gradient
"""
import torch
from torch import nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self) -> None:
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x)) # 讲输出的结果flatten
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return  x


    def num_flat_features(self, x):
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)

#

params = list(net.parameters())
# print(params) # 返回的是可以被学习参数权重
print(len(params))
print(params[0].size())  # conv1's .weight

# 测试随机输入32×32。 注：这个网络（LeNet）期望的输入大小是32×32，
# 如果使用MNIST数据集来训练这个网络，请把图片大小重新调整到32×32。
x = torch.randn(1,1,32,32)
out = net(x)
print(out)

# 将素有的参数的梯度缓存清零，然后随机梯度的反向传播

net.zero_grad()
out.backward(torch.randn(1,10))

# 计算损失函数
target =torch.randn(1,10)
 # randn(1,10) = target.view(1,-1)
# target_b = target.view(1,-1)
# target = torch.randn(10)
print("target size", target.size())
print(target)

# 均方跟误差
loss_func = nn.MSELoss()
print(loss_func)
loss = loss_func(out, target)
print(loss)

# 损失函数的反向传播
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)
loss.backward()

print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)

# 最后一件事情就是更新网络权重

# 在实践中的更新规则是
# weight = weight - lr * gradient

# PyTorch中构建了一个包torch.optim实现了所有的这些规则。 使用它们非常简单：

import torch.optim as optim

optimizer = optim.SGD(net.parameters(), lr=0.01)
optimizer.zero_grad()
output = net(input)
loss = loss_func(output, target)
loss.backward() # 反向传播
optimizer.step()  # 梯度更新



