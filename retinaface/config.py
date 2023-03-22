ADMIN_TOKEN='375184fe576582f1b44ed3ebb944b90aa0cd0046'
LABELS = ["left eye", "right eye", "mouth left", "mouth right", "nose", "face"]
SHAPE_TYPE_MAPPING = ['points'] * (len(LABELS) - 1) + ['rectangle'] * 1
MODEL_NAME = "RetinaFace"
MODEL_TYPE = "Face & Five Landmark Detection"
MODEL_GROUP = ["Bounding Box Object Detection", "Landmark Point Detection"]