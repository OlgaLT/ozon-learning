import requests
import json

URL = "http://localhost:8080"

headers = {
    'Content-Type': 'application/json'
}


class ApiClient:

    def create_group(self, body, path='/v1/groups'):
        payload = json.dumps({
            "foo": body
        })
        response = requests.request("POST",
                                    url=f'{URL}{path}',
                                    headers=headers,
                                    data=payload)
        # response.raise_for_status()
        return response

    def get_groups_list(self, path='/v1/groups'):
        response = requests.request("GET",
                                    url=f'{URL}{path}',
                                    headers=headers)
        return response

    def get_group_describe(self, params, path='/v1/groups/{group_id}'):
        path = path.format(group_id=params)
        response = requests.request("GET",
                                    url=f'{URL}{path}',
                                    headers=headers)
        return response

    def remove_group(self, params, path='/v1/groups/{group_id}'):
        path = path.format(group_id=params)
        response = requests.request("DELETE",
                                    url=f'{URL}{path}',
                                    headers=headers)
        return response
