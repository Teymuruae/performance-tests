from httpx import Client
from time import time

create_user_payload = {
    "email": f"user{time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

client = Client(base_url="http://localhost:8003/api/v1")

create_user_response = client.post(url='/users', json=create_user_payload)
create_user_response_data = create_user_response.json()

create_account_payload = {
    "userId": f"{create_user_response_data['user']['id']}"
}

create_account_response = client.post(url='/accounts/open-deposit-account', json=create_account_payload)

print("Create account response: ", create_account_response.json())
print('Create account response status code: ', create_account_response.status_code)
