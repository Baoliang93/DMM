# Debiased Mapping for Full-Reference Image Quality Assessment

This is the repository of paper [Debiased Mapping for Full-Reference Image Quality Assessment](https://arxiv.org/abs/2302.11464). 

### Highlights:
* The perception bias of existing deep-feature based FR-IQA measures is explored, which may cause inferior performance on misaligned features and restored content.
* We propose an SVD-based debiased mapping to mitigate the perception bias. Specifically, the SVs distance and base angle consistency are designed to capture and measure the feature distortion reliably.


### ====== PyTorch Implementation ======
**Installation:** 
- ```pip install DMM-PyTorch```

**Requirements:**  
- Python >= 3.6
- PyTorch >= 1.0

**Usage:** 
```python

from DMM_PyTorch import DMM
from torchvision import transforms
from PIL import Image

def prepare_PIL_Image(PIL_Image):
    msize = min(PIL_Image.size)
    if  msize>128:
        tar_size = max(int(msize/(1.0*48))*32,128)
        image =transforms.functional.resize(PIL_Image,tar_size)
    image = transforms.ToTensor()(image)
    return image.unsqueeze(0)

model = DMM().cuda()

ref_pth =  './Images/I04.BMP'  
dist_pth =  './Images/i04_24_2.bmp' 
  
ref =  prepare_PIL_Image(Image.open(ref_pth).convert("RGB")).cuda()
dist = prepare_PIL_Image(Image.open(dist_pth).convert("RGB")).cuda()

dmm_score = model(ref, dist)
print(dmm_score)
```
or

```bash
git clone https://github.com/Baoliang93/DMM
cd DMM_PyTorch
python DMM.py --ref <ref_path> --dist <dist_path>
```



