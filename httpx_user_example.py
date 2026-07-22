from httpx import Client
from time import time

client = Client(base_url="http://localhost:8003/api/v1")

payload = {
    "email": f"user{time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = client.post(url='/users', json=payload)
create_user_response_date = create_user_response.json()

print("Create user status: ", create_user_response.status_code)
print("Create user data: ", create_user_response_date)

get_user_response = client.get(url='/users/' + create_user_response_date['user']['id'])

print('Get user status: ', get_user_response.status_code)
print('Get user data: ', get_user_response.json())
