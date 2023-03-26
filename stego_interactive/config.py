ADMIN_TOKEN='b518d556fc3a15521c31bac604b0be203245f791'
LABELS = ["electronic", "appliance", "food", "furniture", "indoor", "kitchen", "accessory", "animal", "outdoor", "person", "sports", "vehicle", "ceiling", "floor", "food_2", "furniture_2", "rawmaterial", "textile", "wall", "window", "building", "ground", "plant", "sky", "solid", "structural", "water"] * 2
SHAPE_TYPE_MAPPING = ['polygon'] * int(len(LABELS) / 2) + ['mask'] * int(len(LABELS) / 2)
MODEL_NAME = "STEGO"
MODEL_TYPE = "Click point mode of semantic model (Dataset C)"
MODEL_GROUP = ["Click Point Semantic"]