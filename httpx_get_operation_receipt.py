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

create_credit_account_payload = {
  "userId": f"{create_user_response_data['user']['id']}"
}

create_credit_account_response = client.post(url='/accounts/open-credit-card-account', json=create_credit_account_payload)
create_credit_account_response_data = create_credit_account_response.json()

account_id = create_credit_account_response_data['account']['id']
card_id = create_credit_account_response_data['account']['cards'][0]['id']

make_purchase_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": card_id,
  "accountId": account_id,
  "category": "taxi"
}

make_purchase_response = client.post(url='/operations/make-purchase-operation', json=make_purchase_payload)
make_purchase_response_data = make_purchase_response.json()

operation_id = make_purchase_response_data['operation']['id']
get_receipt_response = client.get(url=f'/operations/operation-receipt/{operation_id}')

print(get_receipt_response.json())
