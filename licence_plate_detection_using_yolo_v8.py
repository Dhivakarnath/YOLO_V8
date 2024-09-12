# -*- coding: utf-8 -*-
"""Licence Plate Detection Using YOLO_V8.ipynb

Original file is located at
    https://colab.research.google.com/drive/1t8NCU2sk2ya1CEgnuJFANR--9zRjMgtF
"""

!git clone https://github.com/Arijit1080/Licence-Plate-Detection-using-YOLO-V8.git

cd /content/Licence-Plate-Detection-using-YOLO-V8

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="6O1FpH8fM66coiML79yt")
project = rf.workspace("snu-i6ovv").project("license-plate-detector-ogxxg")
dataset = project.version(2).download("yolov8")

!pip install -r requirements.txt

!python /content/Licence-Plate-Detection-using-YOLO-V8/ultralytics/yolo/v8/detect/train.py model=yolov8n.pt data= /content/Licence-Plate-Detection-using-YOLO-V8/License-Plate-Detector-2/data.yaml epochs=100

!python /content/Licence-Plate-Detection-using-YOLO-V8/ultralytics/yolo/v8/detect/predict.py model='/content/Licence-Plate-Detection-using-YOLO-V8/best.pt' source='/content/Licence-Plate-Detection-using-YOLO-V8/demo.mp4'

!python /content/Licence-Plate-Detection-using-YOLO-V8/ultralytics/yolo/v8/detect/predict.py model='/content/Licence-Plate-Detection-using-YOLO-V8/best.pt' source='/content/Licence-Plate-Detection-using-YOLO-V8/lp.jpg'
