ADMIN_TOKEN='b518d556fc3a15521c31bac604b0be203245f791'
LABELS = ["left eye", "right eye", "mouth left", "mouth right", "nose", "face"]
SHAPE_TYPE_MAPPING = ['points'] * (len(LABELS) - 1) + ['rectangle'] * 1
MODEL_NAME = "RetinaFace"
MODEL_TYPE = "Face & Five Landmark Detection"
MODEL_GROUP = ["Bounding Box Object Detection", "Landmark Point Detection"]