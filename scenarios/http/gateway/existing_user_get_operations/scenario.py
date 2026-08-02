from locust import events, task
from locust.env import Environment

from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.operations.schema import GetOperationsQuerySchema, GetOperationsSummaryQuerySchema
from seeds.scenarios.existing_user_get_operations import ExistingUserGetOperationsSeedsScenario
from seeds.schema.result import SeedUserResult
from tools.locust.user import LocustBaseUser


@events.init.add_listener
def init(environment: Environment, **kwargs):
    seeds_scenario = ExistingUserGetOperationsSeedsScenario()
    seeds_scenario.build()

    environment.seeds = seeds_scenario.load()


class GetOperationsTaskSet(GatewayHTTPTaskSet):
    seed_user: SeedUserResult
    account_id: str

    def on_start(self) -> None:
        super().on_start()

        self.seed_user = self.user.environment.seeds.get_random_user()
        self.account_id = self.seed_user.credit_card_accounts[0].account_id

    @task(2)
    def get_accounts(self):
        self.accounts_gateway_client.get_accounts(self.seed_user.user_id)

    @task(2)
    def get_operations(self):
        query = GetOperationsQuerySchema(account_id=self.account_id)
        self.operations_gateway_client.get_operations(query)

    @task(1)
    def get_operations_summary(self):
        query = GetOperationsSummaryQuerySchema(account_id=self.account_id)
        self.operations_gateway_client.get_operations_summary(query)

class GetOperationsScenarioUser(LocustBaseUser):
    tasks = [GetOperationsTaskSet]
