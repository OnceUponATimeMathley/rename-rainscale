import requests
from functools import partial
import asyncio
from labels import get_model_labels
import config



def send_labels(url, headers, data):
    response = requests.post(url, json=data, headers=headers)
    return response

async def send_labels_async(url, headers, data):
    return await asyncio.to_thread(send_labels, url, headers, data)


async def handle_labels(url, headers, labels, shape_type_mappings):
    assert len(labels) == len(shape_type_mappings)
    general_send_labels_async = partial(send_labels_async, url, headers)
    datas = [{'name': label, 'shape': shape_type} for label, shape_type in zip(labels, shape_type_mappings)]

    results = await asyncio.gather(*[general_send_labels_async(data) for data in datas])
    return results

def send_model(url, headers, data):
    return requests.post(url, json=data, headers=headers)

async def handle_model(url_label, url_model, headers, labels, shape_type_mappings, model_name):
    labels = get_model_labels(url_label, headers, labels, shape_type_mappings)
    datas = {
        'name': model_name,
        'labels': labels
    }

    return await asyncio.to_thread(send_model, url_model, headers, datas)


if __name__ == '__main__':
    url_label = 'http://localhost:3000/api/ai-labels'
    token = 'Token ' + str(config.ADMIN_TOKEN)
    headers = {'Authorization': token}
    labels = config.LABELS
    shape_type_mappings = config.SHAPE_TYPE_MAPPING
    asyncio.run(handle_labels(url_label, headers, labels, shape_type_mappings))

    url_model = 'http://localhost:3000/api/ai-models'
    model_name = config.MODEL_NAME
    asyncio.run(handle_model(url_label, url_model, headers, labels, shape_type_mappings, model_name))

