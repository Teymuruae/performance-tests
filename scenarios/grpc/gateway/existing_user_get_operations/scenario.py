from locust import events, task
from locust.env import Environment

from clients.grpc.gateway.locust import GatewayGRPCTaskSet
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()

    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayGRPCTaskSet):
    seed_user: SeedUserResult
    account_id: str

    def on_start(self) -> None:
        super().on_start()

        self.seed_user = self.user.environment.seeds.get_next_user()
        self.account_id = self.seed_user.credit_card_accounts[0].account_id

    @task(2)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(self.seed_user.user_id)

    @task(2)
    def get_operations(self):
        self.operations_gateway_client.get_operations(self.account_id)

    @task(1)
    def get_operations_summary(self):
        self.operations_gateway_client.get_operations_summary(self.account_id)


class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
