import requests
from functools import partial
import asyncio
from labels import get_model_labels_async


def send_labels(url, headers, data):
    response = requests.post(url, json=data, headers=headers)
    return response

async def send_labels_async(url, headers, data):
    return await asyncio.to_thread(send_labels, url, headers, data)


async def handle_labels(url, headers, labels, shape_type_mappings):
    print("handle_labels")
    assert len(labels) == len(shape_type_mappings)
    general_send_labels_async = partial(send_labels_async, url, headers)
    datas = [{'name': label, 'shape': shape_type} for label, shape_type in zip(labels, shape_type_mappings)]

    results = await asyncio.gather(*[general_send_labels_async(data) for data in datas])
    return results

def send_model(url, headers, data):
    return requests.post(url, json=data, headers=headers)

async def handle_model(url_label, url_model, headers, labels, shape_type_mappings, model_name):
    print("handle_model: ", model_name)
    labels = await get_model_labels_async(url_label, headers, labels, shape_type_mappings)
    datas = {
        'name': model_name,
        'labels': labels
    }
    response = await asyncio.to_thread(send_model, url_model, headers, datas)
    return response

async def handle_model_types(url_model, url_model_type, headers, model_name, model_types):
    print("handle_model_types: ", model_name)
    response = requests.get(url_model, headers=headers, params={'name': model_name}).json()['results']
    assert len(response) == 1
    model_id = response[0]["id"]
    results = []
    for model_type in model_types:
        datas = {
            'name' : model_type,
            'model_id': model_id
        }
        response = requests.post(url_model_type, headers=headers, json=datas)
        results.append(response)
    return results

async def handle_model_groups(url_model_type, url_model_group, headers, model_types, model_groups):
    print("handle_model_groups")
    results = []
    for model_type, model_group in zip(model_types, model_groups):
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