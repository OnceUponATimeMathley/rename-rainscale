import requests
import config


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
    url_model_type = 'http://localhost:3000/api/ai-model-types'
    url_model_group = 'http://localhost:3000/api/ai-model-groups'
    token = 'Token ' + str(config.ADMIN_TOKEN)
    headers = {'Authorization': token}
    model_type = config.MODEL_TYPE
    model_groups = config.MODEL_GROUP
    results = handle_model_group(url_model_type, url_model_group, 
                                 headers, model_type, model_groups)
    
    for response in results:
        print(response.json())