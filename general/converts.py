import yaml
from dataclasses import dataclass, field
from typing import List, Dict, Tuple


@dataclass
class BaseSettings:
    ADMIN_TOKEN: str
    BASE_URL: str
    DJANGO_LABEL_URL: str
    DJANGO_MODEL_URL: str
    DJANGO_MODEL_TYPE_URL: str
    DJANGO_MODEL_GROUP_URL: str

    def __str__(self) -> str:
        return "\n".join([self.ADMIN_TOKEN, self.BASE_URL, self.DJANGO_LABEL_URL,
                          self.DJANGO_MODEL_URL, self.DJANGO_MODEL_TYPE_URL,
                          self.DJANGO_MODEL_GROUP_URL])

    def getLabelUrl(self):
        return self.BASE_URL + self.DJANGO_LABEL_URL
    
    def getModelUrl(self):
        return self.BASE_URL + self.DJANGO_MODEL_URL
    
    def getModelTypeUrl(self):
        return self.BASE_URL + self.DJANGO_MODEL_TYPE_URL
    
    def getModelGroupUrl(self):
        return self.BASE_URL + self.DJANGO_MODEL_GROUP_URL

@dataclass
class ModelInfo:
    name: str
    labels: List[Dict] = field(default_factory=list)
    modelTypes: List[Dict] = field(default_factory=list)

    def __str__(self) -> str:
        return self.name 
    
    def getModelName(self):
        return self.name
    
    def getModelTypeGroupMapping(self) -> Tuple[List[str], List[str]]:
        model_types = []
        model_groups = []
        for data in self.modelTypes:
            for group in data['modelGroups']:
                model_groups.append(group)
                model_types.append(data['name'])
        return model_types, model_groups
    
    def getModelTypes(self) -> List[str]:
        return [data['name'] for data in self.modelTypes]
    
    def getLabelShapeMapping(self) -> Tuple[List[str], List[str]]:
        labels = []
        shapeTypes = []
        for item in self.labels:
            labels.append(item['name'])
            shapeTypes.append(item['shapeType'])
        return labels, shapeTypes


def readYaml(file_path: str) -> Dict:
    with open(file_path, 'r') as stream:
        try:
            parsed_yaml = yaml.safe_load(stream)
            return parsed_yaml
        except yaml.YAMLError as exc:
            raise ValueError('Configs file error: ', exc)

def getListModelInfo(file_path) -> Tuple[BaseSettings, List[ModelInfo]]:
    model_objs = []
    contents = readYaml(file_path)
    for key, value in contents.items():
        if key == 'settings':
            baseSettings = BaseSettings(
                value['ADMIN_TOKEN'],
                value['BASE_URL'],
                value['DJANGO_LABEL_URL'],
                value['DJANGO_MODEL_URL'],
                value['DJANGO_MODEL_TYPE_URL'],
                value['DJANGO_MODEL_GROUP_URL']
            )
        elif key == 'spec':
            for info in value:
                modelInfo = ModelInfo(
                    info['modelName'],
                    info['labels'],
                    info['modelTypes']
                )
                model_objs.append(modelInfo)
        else:
            pass
    return baseSettings, model_objs












