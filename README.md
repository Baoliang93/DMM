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
model = DMM()
# calculate DeepDC between X, Y (a batch of RGB images, data range: 0~1) 
dmm_score = model(X, Y)
```
or

```bash
git clone https://github.com/Baoliang93/DMM
cd DMM_PyTorch
python DMM.py --ref <ref_path> --dist <dist_path>
```



