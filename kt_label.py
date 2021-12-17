import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

#sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


def convert(size, box, image_id):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    if x < 0 or y < 0 or w < 0 or h < 0:
        print(image_id)
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open('kt_all_ann/%s%s.xml'%(image_id, '_v001_1'))     #xml file path
    out_file = open('all_labels/%s.txt'%(image_id,), 'w')           #output txt file path
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text

        if cls == 'Vehicle_Car' or cls == 'Vehicle_Bus' or cls == 'Vehicle_Motorcycle' or cls == 'Vehicle_Unknown':
            cls_id = 0
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b, image_id)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            #print(cls)
            
        elif cls == 'Pedestrian_Pedestrian' or cls == 'Pedestrian_Bicycle':
            cls_id = 1
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b, image_id)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            #print(cls)
        elif cls == 'TrafficLight_Red' or cls == 'TrafficLight_Yellow' or cls == 'TrafficLight_Green' or cls == 'TrafficLight_Arrow' or cls == 'TrafficLight_RedArrow' or cls == 'TrafficLight_YellowArrow' or cls == 'TrafficLight_GreenArrow':
            cls_id = 2
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b, image_id)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            #print(cls)
        
        elif cls == 'TrafficSign_Speed' or cls == 'TrafficSign_Else':    
            cls_id = 3
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b, image_id)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            #print(cls)
            
        else:
            continue

#for year, image_set in sets:
if not os.path.exists('/all_labels/'):
    os.makedirs('/all_labels/')
image_ids = open('list.txt').read().strip().split()     #list of dataset image_id
list_file = open('kt_train.txt', 'w')     #list of image path for training. you should split this file if you want validation set.
for image_id in image_ids:
    list_file.write('kt_all_images/%s.jpg\n'%(image_id))
    convert_annotation(image_id)
list_file.close()

