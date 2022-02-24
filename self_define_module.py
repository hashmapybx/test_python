import torch.nn.functional as F
import torch
from torch import nn


class Net(nn.Module):
    def __init__(self) -> None:
        super(Net,self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=3)
        # 线形层输入1350个特征 输出10个特征
        self.fc1 = nn.Linear(1350, 10)

    def forward(self, x): # [1,1,32,32]
        print(x.size())
        # 卷积 -> 激活 -> 池化
        x = self.conv1(x)
        x = F.relu(x)
        print(x.size()) # [1,6, 30, 30]
        x = F.max_pool2d(x,(2,2))
        x = F.relu(x)
        print(x.size()) # [1,6,15,15]

        x = x.view(x.size()[0], -1) # 这里做的就是压扁的操作 就是把后面的[1, 6, 15, 15]压扁，变为 [1, 1350]
        print(x.size())
        x = self.fc1(x)
        return x

net = Net()
print(net)
print("网络可以学习的参数")
for parameters in net.parameters():
    print(parameters)

print("net.named_parameters可同时返回可学习的参数及名称。")
for name,parameters in net.named_parameters():
    print(name,':',parameters.size())

print("自定义输入数据")
input = torch.randn(1, 1, 32, 32) # 这里的对应前面fforward的输入是32
out = net(input)
out.size()

net.zero_grad()
out.backward(torch.ones(1,10))
