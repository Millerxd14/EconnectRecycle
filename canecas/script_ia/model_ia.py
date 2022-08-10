import torch
import torchvision
from torch.utils.data import random_split
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import os
##other libraries

import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path


base = os.getcwd()
dir_completa = os.path.join(base, "canecas/script_ia/", "modeloprueba08052022.pth")


dir_completa = dir_completa.replace('\\', '/')

#print("This file path, relative to os.getcwd()")
#print(dir_completa + "\n")
#
def accuracy(outputs, labels):
    _, preds = torch.max(outputs, dim=1)
    return torch.tensor(torch.sum(preds == labels).item() / len(preds))

class ImageClassificationBase(nn.Module):
    def training_step(self, batch):
        images, labels = batch 
        out = self(images)                  # Generate predictions
        loss = F.cross_entropy(out, labels) # Calculate loss
        return loss
    
    def validation_step(self, batch):
        images, labels = batch 
        out = self(images)                    # Generate predictions
        loss = F.cross_entropy(out, labels)   # Calculate loss
        acc = accuracy(out, labels)           # Calculate accuracy
        return {'val_loss': loss.detach(), 'val_acc': acc}
        
    def validation_epoch_end(self, outputs):
        batch_losses = [x['val_loss'] for x in outputs]
        epoch_loss = torch.stack(batch_losses).mean()   # Combine losses
        batch_accs = [x['val_acc'] for x in outputs]
        epoch_acc = torch.stack(batch_accs).mean()      # Combine accuracies
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}
    
    def epoch_end(self, epoch, result):
        print("Epoch {}: train_loss: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}".format(
            epoch+1, result['train_loss'], result['val_loss'], result['val_acc']))


class ResNet(ImageClassificationBase):
    def __init__(self):
        super().__init__()
        # Use a pretrained model
        self.network = models.resnet50(pretrained=True)
        # Replace last layer
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, 6)
    
    def forward(self, xb):
        return torch.sigmoid(self.network(xb))

model = ResNet()

#print(model)

dir_model = dir_completa
model.load_state_dict(torch.load(dir_model, map_location='cpu'))
model.eval()

transformations = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])

classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def predict_image(img, model):

    xb = img.unsqueeze(0)#Convertir imagen a tensor
    '''
    [
        [1,2,3,4],
        [123,4,8,2],
        [9,8,7,51]
    ]
    '''
    #Tensor xb
    # Get predictions from model
    
    yb = model(xb)
    prob, preds  = torch.max(yb, dim=1)#['0.1', '0.5', '0.05', '0.7', '0.0004', '0.4']
    return classes[preds[0].item()]

def predict_external_image(image):
    try:
        example_image = transformations(image)
        return predict_image(example_image, model)
    except:
        return "No posible to predict that image"



