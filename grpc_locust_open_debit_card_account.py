from locust import User, wait_time, task
from clients.grpc.gateway.users.client import build_users_gateway_locust_grpc_client, UsersGatewayGRPCClient
from clients.grpc.gateway.accounts.client import build_accounts_gateway_locust_grpc_client, AccountsGatewayGRPCClient
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse


class OpenDebitCardAccountScenarioUser(User):
    host = 'localhost'

    create_user_response: CreateUserResponse
    users_gateway_client: UsersGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient

    wait_time.between(2, 4)

    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)

        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        self.accounts_gateway_client.open_debit_card_account(user_id=self.create_user_response.user.id)
