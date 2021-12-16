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
nvidia-docker run --name test -it -v your_code_path/:/yolor --shm-size=64g nvcr.io/nvidia/pytorch:20.11-py3

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
cd yolor

```

## Convert Dataset format
Make list.txt (image name list)   
Such as..
```
1_20200602_140054_000420
1_20200602_140054_000450
1_20200602_140054_000480
1_20200602_140054_000510
1_20200602_140054_000540
1_20200602_140054_000570
1_20200602_140054_000600
1_20200602_140054_000630
1_20200602_140054_000660
1_20200602_140054_000690
1_20200602_140054_000720
1_20200602_140054_000750
1_20200602_140054_000780
1_20200602_140054_000810
1_20200602_140054_000840
1_20200602_140137_000000
1_20200602_140137_000030
1_20200602_140137_000060
1_20200602_140137_000090
1_20200602_140137_000120
1_20200602_140137_000150
1_20200602_140137_000180
```

Convert Pascal VOC(xml) to YOLO(txt) using kt_label.py (**You should modify the image and label path to suit you**)
```
python kt_label.py
```

Modify path in kt.yaml for your environment
```
train: kt2yolo/kt_train.txt
val: kt2yolo/kt_val.txt
test: kt2yolo/kt_val.txt
```
## Testing mAP
[`Katech_best.pt`](https://drive.google.com/file/d/1Q16YUdUz8SA0L76d4g3waFaRMxMCcidd/view?usp=sharing)   
Download best weight training with Katech training dataset for test mAP
```
python test.py --data data/kt.yaml --img 1920 --batch 4 --conf 0.3 --iou 0.5 --device 0 --cfg cfg/yolor_p6_kt.cfg --weights Katech_best.pt --name katech_mAPtest --save-txt --names data/kt.names --verbose
```

## Training schedule
[`yolor_p6.pt`](https://drive.google.com/file/d/1Tdn3yqpZ79X7R1Ql0zNlNScB1Dv9Fp76/view?usp=sharing)   
Download COCO pretrained weight for initialization
```
python -m torch.distributed.launch --nproc_per_node 4 --master_port 9127 we.py --batch-size 16 --img 1280 1280 --data kt.yaml --cfg cfg/yolor_p6_kt.cfg --device 0,1,2,3 --sync-bn --hyp data/hyp.scratch.1280.yaml --epochs 300 --weights yolor_p6.pt --name Katech --workers 16
```

## Image Inference
```
python detect.py --source inference/images/ --img-size 1920 --conf 0.3 --iou 0.5 --device 0 --cfg cfg/yolor_p6_kt.cfg --weights Katech_best.pt --save-txt --names data/kt.names
```

## Convert Dataset format
YOLO(txt) to Pascal VOC(xml)   
Move images to convert_yolo2kt/kt/images   
Move txt labels to convert_yolo2kt/kt/labels   
```
cd convert_yolo2kt
python yolo_to_kt.py
```
