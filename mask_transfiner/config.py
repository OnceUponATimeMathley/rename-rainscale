ADMIN_TOKEN='375184fe576582f1b44ed3ebb944b90aa0cd0046'
LABELS = ["electronic", "appliance", "food", "furniture", "indoor", "kitchen", "accessory", "animal", "outdoor", "person", "sports", "vehicle", "ceiling", "floor", "food_2", "furniture_2", "rawmaterial", "textile", "wall", "window", "building", "ground", "plant", "sky", "solid", "structural", "water"] * 2
SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS)/2)
MODEL_NAME = "Mask Transfiner"
MODEL_TYPE = "Common Instance Segmentation (Dataset E)"
MODEL_GROUP = ["Instance Segmentation"]