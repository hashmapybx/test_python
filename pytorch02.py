import torch


a = torch.rand(4,3,28,28)
# a 的shape里面第一个dim代表的是batch channel weight hight
print("szie is: ",a.size())
print("第一个batch的数据: ",a[0].shape)
print("第一个batch 下面的第一个通道的数据是： ",a[0,0].shape)
print(a[0,0,1,1])

print("="*50)
print(a.shape)
print("=====切片======")
print(a[:2].shape)
print(a[:1,:2,:,:].shape)
print(a[:3,-1,:,:].shape)
print("select by steps")
print(a[:,:,0:28:2,0:28:2].shape)
print(a[:,:,::2, ::2].shape)
print(a.index_select(1, torch.arange(2)).shape)
print(a.index_select(3, torch.arange(8)).shape)

src = torch.tensor(
    [[1,2,3],[4,5,6]]
)
print("src size", src.size())
# print(torch.take(src, torch.tensor([0,2])))
print(src.view(-1))
# 首先将input（这里为src）中的元素按照一维展开，
# 然后在里面将index中的元素取出来形成一个新的tensor。index可以不只是一维tensor，可以是多维tensor：
print(torch.take(src, torch.tensor([0,2,3])))