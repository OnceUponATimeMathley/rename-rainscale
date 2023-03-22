import requests
import config

def get_model_labels(url, headers, labels, shape_type_mappings):
    params = {}
    params['label_values'] = ','.join(labels)
    params['shape_values'] = ','.join(shape_type_mappings)
    all_labels = []

    # set the initial page number to 1
    page = 1

    while True:
        # make the API request with the current page number
        params['page'] = page
        response = requests.get(url, headers=headers, params=params)

        # check if there are no more pages to retrieve
        if not response.json()['next']:
            break

        # add the current page's cars to the list
        all_labels.extend(response.json()['results'])

        # move to the next page
        page += 1

    # add the last page's cars to the list
    all_labels.extend(response.json()['results'])
    label_ids = [label_info["id"] for label_info in all_labels]
    return label_ids

if __name__ == '__main__':
    url_label = 'http://localhost:3000/api/ai-labels'
    token = 'Token ' + str(config.ADMIN_TOKEN)
    headers = {'Authorization': token}
    labels = config.LABELS
    shape_type_mappings = config.SHAPE_TYPE_MAPPING

    all_labels = get_model_labels(url_label, headers, labels, shape_type_mappings)
    print(all_labels)







