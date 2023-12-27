import numpy as np
import json
from PIL import Image
import timm
import torch
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform

def imagery():
    labels = json.load(open('./src/imagenet21_class_index(ukr).json', encoding='utf-8'))

    tree = torch.load('./src/imagenet21k_miil_tree.pth')
    eng_labels = np.array(list(tree['class_description'].values()))

    model = timm.create_model('tresnet_m_miil_in21k', pretrained=True).eval()
    config = resolve_data_config({}, model=model)
    transform = create_transform(**config)


    file = './src/last_img.jpg'
    img = Image.open(file).convert('RGB')
    tensor = transform(img).unsqueeze(0)
    logits = model(tensor)
    out = logits.detach().cpu().numpy()
    idx = np.argmax(out, axis=1)
    im_index = idx[0]
    ukr_label = labels.get(f"{im_index}")
    eng_label = str(eng_labels[im_index]).replace('_', ' ')
    return f'{ukr_label} *({eng_label})*'


