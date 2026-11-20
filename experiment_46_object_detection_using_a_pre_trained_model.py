# CSA17 - Artificial Intelligence | Experiment 46 (Manual Ex. 5.6): Object Detection using a Pre-trained Model
# Name            : V V Naveen Kumar
# Register Number : 192321018

import torch
from torchvision.io import read_image, write_png
from torchvision.utils import draw_bounding_boxes
from torchvision.models.detection import (fasterrcnn_resnet50_fpn,
                                            FasterRCNN_ResNet50_FPN_Weights)

weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn(weights=weights, box_score_thresh=0.6)
model.eval()
categories = weights.meta["categories"]

img = read_image("street.jpg") # any JPG/PNG image on disk
batch = [weights.transforms()(img)]

with torch.no_grad():
    result = model(batch)[0]

names = [categories[i] for i in result["labels"]]
for name, score, box in zip(names, result["scores"], result["boxes"]):
    print("%-12s confidence %.2f box=%s" % (name, score, [int(v) for v in box]))

labels = ["%s %.2f" % (n, s) for n, s in zip(names, result["scores"])]
annotated = draw_bounding_boxes(img, result["boxes"], labels, colors="red", width=3)
write_png(annotated, "detected.png")
print("Annotated image saved as detected.png")


# ============================================================
# OUTPUT
# ============================================================
# [NOT EXECUTED HERE - requires PyTorch/torchvision, pretrained weights download and street.jpg]
# [Sample output reproduced from the lab manual; exact numbers vary per run]
#
# person       confidence 0.99 box=[112, 84, 205, 330]
# car        confidence 0.97 box=[300, 180, 560, 330]
# traffic light confidence 0.91 box=[40, 20, 62, 75]
# car        confidence 0.88 box=[10, 200, 120, 300]
# Annotated image saved as detected.png
