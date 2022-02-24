# 训练一个图像分类器
# torchvison 加载数据和归一化训练集和测试集
# 定义一个卷积神经网络
# 定义损失函数
# 在训练集上面训练网络
# 在测试集上面测试网络

# 1 read data
import torch
import torchvision
import torchvision.transforms as transforms

# torchvision的输出是[0,1]的PILImage图像，我们把它转换为归一化范围为[-1, 1]的张量。
from nlp.show_image import imshow

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.2,0.2, 0.2), (0.2,0.2, 0.2))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=True, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


if __name__ == '__main__':

    # 获取随机数据
    for indx, data in enumerate(trainloader):
        img, label = data
        # imshow(torchvision.utils.make_grid(img))
        print(img.shape)
        print("label: {}".format(label))
        break


# 可视化图像数据
# imshow(torchvision.utils.make_grid(images))

# 显示图像标签
# print(' '.join('%5s' % classes[labels[j]] for j in range(4)))