
#我们直接可以使用训练好的模型，当然这个与datasets相同，都是需要从服务器下载的
import torchvision.models as models
resnet18 = models.resnet18(pretrained=True)
print(resnet18)