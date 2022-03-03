

import torch
import torch.nn.functional as F
# from torch.autograd import Variable
#
# x = torch.ones(2,2)
# print(x.size())
# w = torch.full([2,2],2)
# # w.requires_grad_()
# print(w.size())
# mse = F.mse_loss(torch.ones(2,2), x*w)
# print(mse.item())
#
#
# # mse1 = F.mse_loss(torch.ones(1), x*w)
# print(torch.autograd.grad(mse, [w]))

print("softmax")
a = torch.rand(3)
a.requires_grad_()
p = F.softmax(a, dim=0)
print(p)
print(torch.autograd.grad(p[1], [a], retain_graph=True))





