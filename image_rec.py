import numpy as np
import json
import PIL
from PIL import Image
import timm
import torch
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform


def imagery(file, n_outputs):
    labels = json.load(open('./src/imagenet21_class_index(ukr).json', encoding='utf-8'))

    tree = torch.load('./src/imagenet21k_miil_tree.pth')
    eng_labels = np.array(list(tree['class_description'].values()))

    model = timm.create_model('tresnet_m_miil_in21k', pretrained=True).eval()
    config = resolve_data_config({}, model=model)
    transform = create_transform(**config)

    img = Image.open(file).convert('RGB')
    tensor = transform(img).unsqueeze(0)
    logits = model(tensor)
    out = logits.detach().cpu().numpy()
    idx_list = np.argpartition(out, -n_outputs, axis=1)[:, -n_outputs:]

    eng_label_list = []
    ukr_label_list = []
    for im_index in idx_list[0]:
        ##print(im_index)
        ukr_label = labels.get(f"{im_index}")
        eng_label = str(eng_labels[im_index]).replace('_', ' ')
        ##print(ukr_label, eng_label)
        ukr_label_list.append(ukr_label)
        eng_label_list.append(eng_label)

    return ukr_label_list, eng_label_list


