ADMIN_TOKEN='b518d556fc3a15521c31bac604b0be203245f791'
LABELS = ["electronic", "appliance", "food", "furniture", "indoor", "kitchen", "accessory", "animal", "outdoor", "person", "sports", "vehicle", "ceiling", "floor", "food_2", "furniture_2", "rawmaterial", "textile", "wall", "window", "building", "ground", "plant", "sky", "solid", "structural", "water"] * 2
SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS)/2)
MODEL_NAME = "Mask Transfiner"
MODEL_TYPE = "Common Instance Segmentation (Dataset E)"
MODEL_GROUP = ["Instance Segmentation"]