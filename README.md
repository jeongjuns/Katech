# Katech
katech contest (Team ProjectVI)

## Installation
YOLOR (https://github.com/WongKinYiu/yolor)
```
git clone https://github.com/jeongjuns/Katech.git
```

## Docker environment
```
# create the docker container, you can change the share memory size if you have more.
nvidia-docker run --name yolor -it -v your_coco_path/:/coco/ -v your_code_path/:/yolor --shm-size=64g nvcr.io/nvidia/pytorch:20.11-py3

# apt install required packages
apt update
apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
pip install seaborn thop

# install mish-cuda if you want to use mish activation
# https://github.com/thomasbrandon/mish-cuda
# https://github.com/JunnYu/mish-cuda
cd /
git clone https://github.com/JunnYu/mish-cuda
cd mish-cuda
python setup.py build install

# install pytorch_wavelets if you want to use dwt down-sampling module
# https://github.com/fbcotter/pytorch_wavelets
cd /
git clone https://github.com/fbcotter/pytorch_wavelets
cd pytorch_wavelets
pip install .

# go to code folder
cd /yolor

```

## Dataset format
Pascal VOC(XML) to YOLO(txt)
using kt_label.py (You should modify the image and label path to suit you)
```
python kt_label.py
```
## Testing mAP
```
python test.py --data data/kt.yaml --img 1920 --batch 4 --conf ?? --iou ?? --device 0 --cfg cfg/yolor_p6_kt.cfg --weights ??? --name katech_mAPtest --save-txt --names data/kt.names --verbose
```

## Training schedule
```
python -m torch.distributed.launch --nproc_per_node 4 --master_port 9127 we.py --batch-size 16 --img 1280 1280 --data kt.yaml --cfg cfg/yolor_p6_kt.cfg --device 0,1,2,3 --sync-bn --hyp data/hyp.scratch.1280.yaml --epochs 300 --weights yolor_p6.pt --name ??? --workers 16
```

## Image Inference
```
python detect.py --source inference/images/horses.jpg --cfg cfg/??? --weights ?????? --conf ???? --img-size 1920 --device 0
```

## Dataset format
YOLO(txt) to Pascal VOC(XML)
```
???
```
