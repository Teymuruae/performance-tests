from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients.http.gateway.operations.schema import GetOperationsSummaryQuerySchema

make_top_up_operation_response = build_operations_gateway_http_client().get_operations_summary_api(
        GetOperationsSummaryQuerySchema(
            account_id='731ecc8b-993b-468d-9ab6-0b0c13670265'
        )

)
print(make_top_up_operation_response.request)
print(make_top_up_operation_response.text)
