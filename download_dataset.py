from roboflow import Roboflow
rf = Roboflow(api_key="GTxzZjiuCaQuxLugJJyj")
project = rf.workspace("abhipsitas-workspace").project("lego-object-detection-gc7sl")
version = project.version(2)
dataset = version.download("yolov8")