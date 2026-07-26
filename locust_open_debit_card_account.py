from locust import HttpUser, wait_time, task
from tools.fakers import fake


class OpenDebitCardAccountScenarioUser(HttpUser):
    user_id: int

    wait_time.between(2, 4)

    def on_start(self) -> None:
        create_user_request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }

        create_user_response = self.client.post(url='/api/v1/users', json=create_user_request)

        self.user_id = create_user_response.json()['user']['id']

    @task
    def open_debit_card_account(self):
        open_debit_card_account_request = {
            "userId": self.user_id
        }
        self.client.post(url='/api/v1/accounts/open-debit-card-account', json=open_debit_card_account_request)
