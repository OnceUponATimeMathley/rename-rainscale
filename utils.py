
def printModel(MODEL_NAME, indent=2):
    results = " " * indent + "- modelName: " + MODEL_NAME + "\n"
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
    main(ADMIN_TOKEN, LABELS, SHAPE_TYPE_MAPPING, MODEL_NAME, MODEL_TYPE_GROUPS)