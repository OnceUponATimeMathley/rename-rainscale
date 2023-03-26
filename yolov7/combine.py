import requests
from functools import partial
import asyncio
from labels import get_model_labels
import config
import time



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

def handle_model_type(url_model, url_model_type, headers, model_name, model_type):
    response = requests.get(url_model, headers=headers, params={'name': model_name}).json()['results']
    assert len(response) == 1
    model_id = response[0]["id"]
    datas = {
        'name' : model_type,
        'model_id': model_id
    }
    return requests.post(url_model_type, headers=headers, json=datas)


def handle_model_group(url_model_type, url_model_group, headers, model_type, model_groups):
    results = []
    for model_group in model_groups:
        response = requests.get(url_model_type, headers=headers, params={'name': model_type}).json()['results']
        assert len(response) == 1
        model_type_id = response[0]["id"]
        datas = {
            'name' : model_group,
            'model_type_id': model_type_id
        }
        res = requests.post(url_model_group, headers=headers, json=datas)
        results.append(res)
    return results

if __name__ == '__main__':
    begin = time.perf_counter()
    url_label = 'http://localhost:3000/api/ai-labels'
    token = 'Token ' + str(config.ADMIN_TOKEN)
    headers = {'Authorization': token}
    labels = config.LABELS
    shape_type_mappings = config.SHAPE_TYPE_MAPPING
    asyncio.run(handle_labels(url_label, headers, labels, shape_type_mappings))

    url_model = 'http://localhost:3000/api/ai-models'
    model_name = config.MODEL_NAME
    asyncio.run(handle_model(url_label, url_model, headers, labels, 
                             shape_type_mappings, model_name))
    
    url_model_type = 'http://localhost:3000/api/ai-model-types'
    model_type = config.MODEL_TYPE
    response = handle_model_type(url_model, url_model_type, 
                                 headers, model_name, model_type)

    print(response.json())

    url_model_group = 'http://localhost:3000/api/ai-model-groups'
    model_groups = config.MODEL_GROUP
    results = handle_model_group(url_model_type, url_model_group, 
                                 headers, model_type, model_groups)
    for response in results:
        print(response.json())

    print("TOTAL TIME: ", time.perf_counter() - begin)

