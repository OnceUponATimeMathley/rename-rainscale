
def printModel(MODEL_NAME, indent=2):
    results = " " * indent + "- modelName: \"" + MODEL_NAME + "\"\n"
    return results

def printLabels(LABELS, SHAPE_TYPE_MAPPING, indent=4):
    results = ""
    results += " " * indent + "labels: [" + "\n"
    for label, shape in zip(LABELS, SHAPE_TYPE_MAPPING):
        dict_val = {}
        dict_val['name'] = label
        dict_val['shapeType'] = shape
        results += " " * (indent + 2) + str(dict_val) + "," + "\n"
    
    results = results[:-2] + "\n" + " " * indent + "]\n"
    return results

def printModelTypeGroups(MODEL_TYPE_GROUPS, indent=4):
    results = " " * indent + "modelTypes:" + "\n"
    for key, value in MODEL_TYPE_GROUPS.items():
        str_val = ""
        str_val += " " * (indent + 2) + "- name: \"" + key + "\"\n"
        str_val += " " * (indent + 4) + "modelGroups:\n"
        for group in value:
            str_val += " " * (indent + 6) + "- \"" + group + "\"\n"
        results += str_val
    return results
    
def main(ADMIN_TOKEN, LABELS, SHAPE_TYPE_MAPPING, MODEL_NAME, MODEL_TYPE_GROUPS):
    results = ""
    model = printModel(MODEL_NAME)
    labels = printLabels(LABELS, SHAPE_TYPE_MAPPING)
    modelTypeGroups = printModelTypeGroups(MODEL_TYPE_GROUPS)
    results = model + labels + modelTypeGroups
    print(results)
    # print(modelTypeGroups)

if __name__ == '__main__':
    ADMIN_TOKEN='b518d556fc3a15521c31bac604b0be203245f791'
    # MODEL: YOLOv7
    LABELS = ["person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]
    SHAPE_TYPE_MAPPING = ['rectangle'] * len(LABELS)
    MODEL_NAME = "YOLOv7"
    MODEL_TYPE_GROUPS = {
        "Common Object Detection (Dataset A)" : [
            "Bounding Box Object Detection",
            "group 1"
        ], 
        "Test A" : ["group 1"], 
        "Test B": ["group 2"]
    }


    # MODEL: Oriented RCNN 
    LABELS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
              "D", "E", "F", "G", "H", "K", "L", "M", "N", "P", "S", "T",
              "U", "V", "X", "Y", "Z", "0"]   
    SHAPE_TYPE_MAPPING = ['rectangle'] * len(LABELS)
    MODEL_NAME = "Oriented RCNN"
    MODEL_TYPE_GROUPS = {
        "License Plate Detection (Dataset D)" : [
            "Bounding Box Object Detection"
        ]
    }

    # MODEL: CLRNet 
    LABELS = ["line"]
    SHAPE_TYPE_MAPPING = ['rectangle'] * len(LABELS)
    MODEL_NAME = "CLRNet"
    MODEL_TYPE_GROUPS = {
        "Road Lane Line Detection (Dataset G)" : [
            "Polyline Detection"
        ]
    }

    # MODEL: RetinaFace
    LABELS = ["left eye", "right eye", "mouth left", "mouth right", "nose", "face"]
    SHAPE_TYPE_MAPPING = ['points'] * (len(LABELS) - 1) + ['rectangle'] * 1
    MODEL_NAME = "RetinaFace"
    MODEL_TYPE_GROUPS = {
        "Face & Five Landmark Detection" : [
            "Bounding Box Object Detection",
            "Landmark Point Detection"
        ]
    }

    # MODEL: Mask Transfiner
    LABELS = ["electronic", "appliance", "food", "furniture", "indoor", "kitchen", "accessory", "animal", "outdoor", "person", "sports", "vehicle", "ceiling", "floor", "food_2", "furniture_2", "rawmaterial", "textile", "wall", "window", "building", "ground", "plant", "sky", "solid", "structural", "water"] * 2
    SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS)/2)
    MODEL_NAME = "Mask Transfiner"
    MODEL_TYPE_GROUPS = {
        "Common Instance Segmentation (Dataset E)" : [
            "Instance Segmentation"
        ]
    }

    # MODEL: STEGO
    LABELS = ["electronic", "appliance", "food", "furniture", "indoor", "kitchen", "accessory", "animal", "outdoor", "person", "sports", "vehicle", "ceiling", "floor", "food_2", "furniture_2", "rawmaterial", "textile", "wall", "window", "building", "ground", "plant", "sky", "solid", "structural", "water"] * 2
    SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS) / 2)
    MODEL_NAME = "STEGO"
    MODEL_TYPE_GROUPS = {
        "Click point mode of semantic model (Dataset C)" : [
            "Click Point Semantic"
        ]
    }

    # MODEL: BEiT
    LABELS = ["road", "sidewalk", "building", "wall", "fence", "pole", "traffic light car", "traffic light pedestrian", "traffic light other", "traffic sign stop", "traffic sign other", "vegetation", "terrain", "sky", "person", "rider", "car", "truck", "bus", "specific car", "train", "motorcycle", "bicycle", "line solid white - ego lane", "line solid yellow - ego lane", "line solid other - ego lane", "line dashed white - ego lane", "line dashed yellow - ego lane", "line dashed other - ego lane", "line solid white - other lane", "line solid yellow - other lane", "line solid other - other lane", "line dashed white - other lane", "line dashed yellow - other lane", "line dashed other - other lane", "road marking crosswalk", "road marking stopline", "road marking arrow", "road marking diamond", "road marking text stop", "road marking text other", "road marking additional line", "road marking zebla zone", "road marking other", "animal", "gate bar", "tunnel", "nature", "smoke", "dynamic", "static on road", "static in air", "invisible", "splash", "cone"] * 2
    SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS) / 2)
    MODEL_NAME = "BEiT"
    MODEL_TYPE_GROUPS = {
        "Click point mode of semantic model (Dataset M)" : [
            "Click Point Semantic"
        ]
    }


    # MODEL: InSPyReNet
    LABELS = ["person", "bicycle", "car", "motorcycle", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"] * 2
    SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS) / 2)
    MODEL_NAME = "InSPyReNet"
    MODEL_TYPE_GROUPS = {
        "Salient Object Detection (Dataset B)" : [
            "Salient Object Detection"
        ]
    }

    # MODEL: TRACER
    LABELS = ["person", "bicycle", "car", "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"] * 2
    SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS) / 2)
    MODEL_NAME = "TRACER"
    MODEL_TYPE_GROUPS = {
        "Salient Object Detection (Dataset B)" : [
            "Salient Object Detection"
        ]
    }

    # MODEL: TRACER
    LABELS = ["short sleeved shirt", "long sleeved shirt", "short sleeved outwear", "long sleeved outwear", "vest", "sling", "shorts", "trousers", "skirt", "short sleeved dress", "long sleeved dress", "vest dress", "sling dress"]
    SHAPE_TYPE_MAPPING = ['skeleton'] * len(LABELS)
    MODEL_NAME = "KGDet"
    MODEL_TYPE_GROUPS = {
        "Fashion Keypoint Detection (Dataset G)" : [
            "Skeleton-based Keypoints Detection"
        ]
    }

    # MODEL: ByteTrack
    LABELS = ["person"]
    SHAPE_TYPE_MAPPING = ['rectangle'] * len(LABELS)
    MODEL_NAME = "ByteTrack"
    MODEL_TYPE_GROUPS = {
        "Person Tracking Model (Dataset H)" : [
            "Tracking Model"
        ]
    }

    main(ADMIN_TOKEN, LABELS, SHAPE_TYPE_MAPPING, MODEL_NAME, MODEL_TYPE_GROUPS)