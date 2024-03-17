import pytest
import requests


def test_requests(get_url, get_body):

    url = get_url

    response = requests.post(url=url, data=get_body)

    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json['success'] == True


@pytest.mark.parametrize('limit', [1,2,3])
def test_get_entires(get_entiers_url, limit, get_token):
    # params = "?content_type=article&order=-fields.publishedDate&fields.type.sys.contentType.sys.id=articleType&fields.type.fields.slug[nin]=event,news&include=4&limit=2"
    #
    # response = requests.get(url=get_entiers_url + params):
    params = {
        'content_type': 'article',
        'order': '-fields.publishedDate',
        'fields.type.sys.contentType.sys.id': 'articleType',
        'fields.type.fields.slug[nin]': 'event,news',
        'include': 4,
        'limit': limit
    }

    headers = {'Authorization': get_token}
    response = requests.get(url=get_entiers_url, params=params, headers=headers)

    assert response.status_code == 200
