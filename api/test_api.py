def test_list_users(api_client):
    response = api_client.get('users?page=2')
    assert response.status_code == 200
    json_response = response.json()
    assert json_response['data']   # check if 'data' field is not empty