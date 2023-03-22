import requests
import config


def handle_model_type(url_model, url_model_type, headers, model_name, model_type):
    response = requests.get(url_model, headers=headers, params={'name': model_name}).json()['results']
    assert len(response) == 1
    model_id = response[0]["id"]
    datas = {
        'name' : model_type,
        'model_id': model_id
    }
    return requests.post(url_model_type, headers=headers, json=datas)


if __name__ == '__main__':
    url_model = 'http://localhost:3000/api/ai-models'
    url_model_type = 'http://localhost:3000/api/ai-model-types'
    token = 'Token ' + str(config.ADMIN_TOKEN)
    headers = {'Authorization': token}
    model_type = config.MODEL_TYPE
    model_name = config.MODEL_NAME
    response = handle_model_type(url_model, url_model_type, 
                                 headers, model_name, model_type)
    print(response.json())