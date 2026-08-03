from locust import task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from clients.grpc.gateway.users.client import CreateUserResponse
from clients.grpc.gateway.accounts.client import OpenDebitCardAccountResponse
from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    create_user_response: CreateUserResponse | None = None
    open_debit_account_response: OpenDebitCardAccountResponse | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_account(self):
        if not self.create_user_response:
            return

        self.open_debit_account_response = self.accounts_gateway_client.open_debit_card_account(
            self.create_user_response.user.id
        )

    @task
    def issue_physical_card(self):
        self.cards_gateway_client.issue_physical_card(
            self.create_user_response.user.id,
            self.open_debit_account_response.account.id
        )


class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]
