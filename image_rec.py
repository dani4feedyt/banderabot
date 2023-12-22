import numpy as np
import cv2
import torch
import json
from torchvision.transforms.functional import normalize, resize
from torchvision.models import densenet121


def imagery():
    labels = json.load(open('imagenet_class_index.json', encoding='utf-8'))

    model = densenet121(pretrained=True).eval()

    file = './src/last_img.jpg'
    image = cv2.imread(file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = torch.from_numpy(image)
    img = img.permute(2, 0, 1)
    print('Image shape:', img.shape)
    input_tensor = normalize(resize(img, [244, 244]) / 255., [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    out = model(input_tensor.unsqueeze(0))
    out = out.detach().cpu().numpy()
    idx = np.argmax(out, axis=1)
    str_idx = str(idx[0])
    return labels[str_idx][1]


